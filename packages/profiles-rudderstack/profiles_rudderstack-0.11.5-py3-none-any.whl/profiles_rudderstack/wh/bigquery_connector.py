#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bigquery connector."""

import pandas as pd
from logging import getLogger

from sqlalchemy import create_engine

from profiles_rudderstack.wh.connector_base import ConnectorBase, register_connector

@register_connector
class BigqueryConnector(ConnectorBase):
    def __init__(self, creds: dict, db_config: dict, **kwargs) -> None:
        super().__init__(creds, db_config, **kwargs)
        self.logger = getLogger("bigquery_connector")
        self.engine = create_engine('bigquery://', credentials_info=creds['credentials'])
        self.connection = self.engine.connect()
        self.creds = creds
        self.db_config = db_config

    def write_to_table(
        self,
        df: pd.DataFrame,
        table_name: str,
        schema: str = None,
        if_exists: str = "append",
    ):
        
        if "." in table_name:
            schema, table_name = table_name.split(".")
        try:
            # pandas takes care of quoting the relation name so we need to remove the custom quotes from the relation names that we add on WHT side.
            df.to_sql(name=table_name.replace("`", ""), con=self.engine, schema=schema.replace("`", ""), index=False, if_exists=if_exists)

        except Exception as e:
            self.logger.error(f"Error while writing to warehouse: {e}")

            # Check for non-existing schema
            err_str = f"table '{table_name}' does not exist".lower()
            if err_str in str(e).lower():
                self.create_table(df, table_name, schema)
                # Try again`
                self.logger.info("Trying again")
                self.write_to_table(df, table_name, schema, if_exists)
