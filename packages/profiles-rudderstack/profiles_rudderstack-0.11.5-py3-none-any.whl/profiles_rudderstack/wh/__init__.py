#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Module for handling various warehouse connections"""

from typing import Union

from profiles_rudderstack.wh.connector_base import connector_classes
from profiles_rudderstack.wh.redshift_pb_connector import RedShiftConnector
from profiles_rudderstack.wh.snowflake_connector import SnowflakeConnector
from profiles_rudderstack.wh.databricks_connector import DatabricksConnector
from profiles_rudderstack.wh.bigquery_connector import BigqueryConnector

# SnowflakeConnector not used currently in profiles_rudderstack


def ProfilesConnector(config: dict, **kwargs) -> Union[RedShiftConnector, SnowflakeConnector, DatabricksConnector, BigqueryConnector]:
    """Creates a connector object based on the config provided

    Args:
        config: A dictionary containing the credentials and database information for the connector.
        **kwargs: Additional keyword arguments to pass to the connector.

    Returns:
        ConnectorBase: Connector object.

    Raises:
        Exception: Connector not found
    """

    warehouse_type = config.get("type").lower()
    connector = connector_classes.get(warehouse_type, None)
    if connector is None:
        raise Exception(f"Connector {warehouse_type} not found")

    creds = {
        "user": config.get("user"),
        "password": config.get("password"),
        "account_identifier": config.get("account"),
        "warehouse": config.get("warehouse"),
        "host": config.get("host"),
        "port": config.get("port"),
    }

    if "role" in config:
        creds["role"] = config.get("role")
    if "access_token" in config:
        creds['access_token'] = config.get("access_token")
    if "http_endpoint" in config:
        creds['http_endpoint'] = config.get("http_endpoint")
    if "credentials" in config:
        creds['credentials'] = config.get("credentials")

    db_config = {
        "database": config.get("dbname"),
        "schema": config.get("schema")
    }

    if "catalog" in config:
        db_config['catalog'] = config.get("catalog")

    if "project_id" in config:
        db_config['project_id'] = config.get("project_id")

    connector = connector(creds, db_config, **kwargs)
    return connector
