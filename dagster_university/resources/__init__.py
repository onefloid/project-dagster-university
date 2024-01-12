from dagster_duckdb import DuckDBResource
from dagster_dbt import DbtCliResource
from dagster import EnvVar

import os

from ..assets.constants import DBT_DIRECTORY


## Lesson 6 and go over .env file 
database_resource = DuckDBResource(
    database=EnvVar("DUCKDB_DATABASE"),
)

dbt_resource = DbtCliResource(
    project_dir=os.fspath(DBT_DIRECTORY)
)