#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Databricks Connector."""

import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from databricks.sql import connect

from logging import Logger
from profiles_rudderstack.wh.connector_base import ConnectorBase, register_connector


@register_connector
class DatabricksConnector(ConnectorBase):
    def __init__(self, creds: dict, db_config: dict, **kwargs) -> None:
        super().__init__(creds, db_config, **kwargs)
        self.logger = Logger("DatabricksConnector")
        connection_string = f"databricks://token:{creds['access_token']}@{creds['host']}?http_path={creds['http_endpoint']}&catalog={db_config['catalog']}&schema={db_config['schema']}"
        self.engine = create_engine(connection_string)
        self.connection = Session(self.engine)
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
            df.to_sql(name=table_name, con=self.engine, schema=schema, index=False,
                      if_exists=if_exists)  # not the best method to achieve this (performance wise)

        except Exception as e:
            self.logger.error(f"Error while writing to Databricks: {e}")

            # Check for non existing schema
            err_str = f"table '{table_name}' does not exist".lower()
            if err_str in str(e).lower():
                self.create_table(df, table_name, schema)
                # Try again
                self.logger.info("Trying again")
                self.write_to_table(df, table_name, schema, if_exists)
