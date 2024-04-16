import logging
from typing import List, Dict, Tuple, Union

from rich.progress import track

from bigeye_sdk.model.enums import MatchType
from bigeye_sdk.functions.search_and_match_functions import wildcard_search, fuzzy_match
from bigeye_sdk.functions.table_functions import fully_qualified_table_to_elements
from bigeye_sdk.generated.com.bigeye.models.generated import (
    Table,
    Integration,
    TableauWorkbook,
    Source,
    Schema,
    Delta,
    TableColumn,
    DataNodeType,
    LineageNodeV2,
    LineageEdgeV2,
    DataNode,
    LineageRelationship,
)
from bigeye_sdk.log import get_logger
from bigeye_sdk.client.datawatch_client import DatawatchClient
from bigeye_sdk.model.protobuf_enum_facade import SimpleDataNodeType

log = get_logger(__file__)


class LineageController:
    def __init__(self, client: DatawatchClient):
        self.client = client
        self.sources_by_name_ix: Dict[str, Source] = self.client.get_sources_by_name()

    def get_table_by_name(self, entity_name: str) -> Table:
        warehouse, schema, entity_name = fully_qualified_table_to_elements(entity_name)
        table: Table = self.client.get_tables(
            schema=[schema], table_name=[entity_name]
        ).tables[0]
        return table

    def get_tableau_workbook_by_name(
        self, entity_name: str, integration_name: str
    ) -> TableauWorkbook:
        integration: Integration = [
            i for i in self.client.get_integrations() if i.name == integration_name
        ][0]
        workbook = [
            w
            for w in self.client.get_integration_entities(integration_id=integration.id)
            if w.name == entity_name
        ][0]
        return workbook

    def create_node_by_name(self, entity_name: str, integration_name: str) -> DataNode:
        """Create a lineage node for an entity"""
        if not integration_name:
            table = self.get_table_by_name(entity_name=entity_name)
            log.info(f"Creating lineage node for table: {entity_name}")
            entity_id = table.id
            node_type = SimpleDataNodeType.TABLE.to_datawatch_object()

        else:
            workbook = self.get_tableau_workbook_by_name(
                entity_name=entity_name, integration_name=integration_name
            )
            log.info(f"Creating lineage node for entity: {workbook.name}")
            entity_id = workbook.id
            node_type = SimpleDataNodeType.TABLEAU.to_datawatch_object()

        return self.client.create_data_node(
            node_type=node_type, node_entity_id=entity_id
        )

    def delete_node_by_name(self, entity_name: str, integration_name: str):
        """Delete a lineage node for an entity"""
        if not integration_name:
            table = self.get_table_by_name(entity_name=entity_name)
            node_id = table.data_node_id
            log.info(f"Deleting lineage node for table: {table.name}")
        else:
            workbook = self.get_tableau_workbook_by_name(
                entity_name=entity_name, integration_name=integration_name
            )
            node_id = workbook.data_node_id
            log.info(f"Deleting lineage node for table: {workbook.name}")

        self.client.delete_data_node(data_node_id=node_id)

    def create_relation_from_name(
        self, upstream_table_name: str, downstream_table_name: str
    ) -> LineageRelationship:
        """Create a lineage relationship for 2 entities"""
        warehouse, u_schema, u_table_name = fully_qualified_table_to_elements(
            upstream_table_name
        )
        warehouse, d_schema, d_table_name = fully_qualified_table_to_elements(
            downstream_table_name
        )

        upstream: Table = self.client.get_tables(
            schema=[u_schema], table_name=[u_table_name]
        ).tables[0]
        downstream: Table = self.client.get_tables(
            schema=[d_schema], table_name=[d_table_name]
        ).tables[0]

        log.info(
            f"Creating relationship from {upstream_table_name} to {downstream_table_name}"
        )

        return self.client.create_table_lineage_relationship(
            upstream_data_node_id=upstream.data_node_id,
            downstream_data_node_id=downstream.data_node_id,
        )

    def delete_relationships_by_name(self, entity_name: str, integration_name: str):
        """Deletes all relationships for a node by name."""
        if integration_name:
            workbook = self.get_tableau_workbook_by_name(
                entity_name=entity_name, integration_name=integration_name
            )
            node_id = workbook.data_node_id
            log.info(
                f"Deleting all lineage relationships for workbook: {workbook.name}"
            )
        else:
            table = self.get_table_by_name(entity_name=entity_name)
            node_id = table.data_node_id
            log.info(f"Deleting all lineage relationships for table: {table.name}")

        self.client.delete_lineage_relationship_for_node(data_node_id=node_id)

    def get_schemas_from_selector(self, selector: str) -> List[Schema]:
        # Split selectors into patterns
        source_pattern, schema_pattern, table_pattern = fully_qualified_table_to_elements(selector)

        # Only take source ids that match pattern
        source_ids = [
            source.id
            for source_name, source in self.sources_by_name_ix.items()
            if source_name
            in wildcard_search(search_string=source_pattern, content=[source_name])
        ]

        # Only take schemas from those sources that match pattern
        schemas_by_name_ix: Dict[str, Schema] = {
            s.name: s for s in self.client.get_schemas(warehouse_id=source_ids).schemas
        }
        schemas = [
            schema
            for schema_name, schema in schemas_by_name_ix.items()
            if schema_name
            in wildcard_search(search_string=schema_pattern, content=[schema_name])
        ]
        return schemas

    def get_tables_from_selector(self, selector: str) -> List[Table]:
        # Split selectors into patterns
        source_pattern, schema_pattern, table_pattern = fully_qualified_table_to_elements(selector)
        # Get schemas
        schema_ids = [schema.id for schema in self.get_schemas_from_selector(selector)]

        # Only take tables from those schemas that match pattern
        tables_by_id_ix: Dict[str, Table] = {
            t.id: t for t in self.client.get_tables(schema_id=schema_ids).tables
        }

        tables = [
            table
            for table_id, table in tables_by_id_ix.items()
            if table.name
            in wildcard_search(search_string=table_pattern, content=[table.name])
        ]

        return tables

    @staticmethod
    def infer_relationships_from_lists(upstream, downstream, match_type: MatchType = MatchType.STRICT):
        matching = []
        if match_type == MatchType.STRICT:
            for u in upstream:
                matching_downstream = [d for d in downstream if d.name.lower() == u.name.lower()]
                if matching_downstream:
                    for md in matching_downstream:
                        matching.append((u, md))
        elif match_type == MatchType.FUZZY:
            for u in upstream:
                matching_downstream = fuzzy_match(
                    search_string=u.name.lower(),
                    contents=[d.name.lower() for d in downstream],
                    min_match_score=95,
                )
                if matching_downstream:
                    for match in matching_downstream:
                        md_table = [md for md in downstream if md.name.lower() == match[1]]
                        for mdt in md_table:
                            matching.append(
                                (
                                    u,
                                    mdt,
                                )
                            )
        return matching

    def create_edges(self,
                     upstream: Union[Schema, Table, TableColumn],
                     downstream: Union[Schema, Table, TableColumn],
                     node_type: DataNodeType):
        if upstream.data_node_id and downstream.data_node_id:
            self.client.create_lineage_edge(upstream_data_node_id=upstream.data_node_id,
                                            downstream_data_node_id=downstream.data_node_id)
        elif upstream.data_node_id and not downstream.data_node_id:
            d_node = self.client.create_data_node(node_type=node_type, node_entity_id=downstream.id)
            self.client.create_lineage_edge(upstream_data_node_id=upstream.data_node_id,
                                            downstream_data_node_id=d_node.id)
        elif not upstream.data_node_id and downstream.data_node_id:
            u_node = self.client.create_data_node(node_type=node_type, node_entity_id=upstream.id)
            self.client.create_lineage_edge(upstream_data_node_id=u_node.id,
                                            downstream_data_node_id=downstream.data_node_id)
        else:
            u_node = self.client.create_data_node(node_type=node_type, node_entity_id=upstream.id)
            d_node = self.client.create_data_node(node_type=node_type, node_entity_id=downstream.id)
            self.client.create_lineage_edge(upstream_data_node_id=u_node.id,
                                            downstream_data_node_id=d_node.id)

    def create_relations_from_deltas(self, deltas: List[Delta]):
        for d in deltas:
            target_ids = [dc.target_table_id for dc in d.comparison_table_configurations]

            if len(target_ids) > 1:
                log.warning(f'We are unable to determine the proper lineage for deltas with more than 1 target. '
                            f'Please review the `bigeye lineage infer-relations` command for an alternative option.')
            else:
                source_table = self.client.get_tables(ids=[d.source_table.id]).tables[0]
                target_table = self.client.get_tables(ids=target_ids).tables[0]
                try:
                    self.infer_column_level_lineage_from_tables(tables=[(source_table, target_table)])
                except Exception as e:
                    log.warning(f'Failed to create lineage relationship between upstream table: {source_table.name} '
                                f'and downstream table: {target_table.name}. Exception: {e}')

    def execute_lineage_workflow_from_selector(self, selector: str):
        # Split selectors into patterns
        source_pattern, schema_pattern, table_pattern = fully_qualified_table_to_elements(
            selector
        )

        # Only take source ids that match pattern
        source_ids = [
            source.id
            for source_name, source in self.sources_by_name_ix.items()
            if source_name
            in wildcard_search(search_string=source_pattern, content=[source_name])
        ]

        for sid in source_ids:
            self.client.execute_lineage_workflow(sid)

    def get_matching_tables_from_selectors(self,
                                           upstream_selector: str,
                                           downstream_selector: str,
                                           match_type: MatchType = MatchType.STRICT) -> List[Tuple[Table, Table]]:
        upstream_tables = self.get_tables_from_selector(upstream_selector)
        downstream_tables = self.get_tables_from_selector(downstream_selector)
        matching_tables: List[Tuple[Table, Table]] = self.infer_relationships_from_lists(
            upstream=upstream_tables,
            downstream=downstream_tables,
            match_type=match_type
        )
        return matching_tables

    def _get_all_columns_with_data_node_id(self,
                                           matching_tables: List[Tuple[Table, Table]]) -> Dict[int, TableColumn]:
        # Columns do not have a data_node_id from the get_tables request so for now we have to get all columns
        # and make that request once, index the columns by id for use later on.
        all_column_ids = []
        for mt in matching_tables:
            for uc in mt[0].columns:
                all_column_ids.append(uc.id)
            for dc in mt[1].columns:
                all_column_ids.append(dc.id)
        all_columns = self.client.get_columns(column_ids=all_column_ids).columns
        columns_ix_by_id: Dict[int, TableColumn] = {c.column.id: c.column for c in all_columns}

        return columns_ix_by_id

    def infer_column_level_lineage_from_tables(self, tables: List[Tuple[Table, Table]]):
        # Get all columns and their data node id for use later on
        columns_ix_by_id = self._get_all_columns_with_data_node_id(tables)
        
        count_successful_relations = 0
        logging.disable(level=logging.INFO)
        for match in track(tables, description="Generating Lineage..."):
            upstream = match[0]
            downstream = match[1]
            try:
                matching_columns: List[
                    Tuple[TableColumn, TableColumn]
                ] = self.infer_relationships_from_lists(
                    upstream=upstream.columns, downstream=downstream.columns
                )
                if not matching_columns and upstream.data_node_id != downstream.data_node_id:
                    self.create_edges(upstream, downstream, DataNodeType.DATA_NODE_TYPE_TABLE)

                for mc in matching_columns:
                    up_column = mc[0]
                    down_column = mc[1]
                    try:
                        # this is ugly but required b/c data node id for columns not returned as part of get tables
                        up_column.data_node_id = columns_ix_by_id[up_column.id].data_node_id
                        down_column.data_node_id = columns_ix_by_id[down_column.id].data_node_id
                        if up_column.data_node_id != down_column.data_node_id:
                            self.create_edges(
                                upstream=up_column,
                                downstream=down_column,
                                node_type=DataNodeType.DATA_NODE_TYPE_COLUMN,
                            )
                    except Exception as e:
                        log.warning(
                            f"Failed to create relationship between upstream column: {up_column.name} and "
                            f"downstream column: {down_column.name}. Exception {e}"
                        )
        
                count_successful_relations += 1
            except Exception as e:
                log.warning(
                    f"Failed to create relationship between upstream table: {upstream.name} and downstream table: "
                    f"{downstream.name}. Exception: {e}"
                )
        logging.disable(level=logging.NOTSET)
        log.info(
            f"Successfully created {count_successful_relations} of {len(tables)}"
            f" table relationships."
        )
