import logging

import pandas as pd
from google.oauth2 import service_account

from util.constants import gcp_project, secrets_path


def bq_to_df(query: str) -> pd.DataFrame:
    logging.info(f"SQL: {query}")
    df = pd.read_gbq(query, project_id=gcp_project, dialect="standard")
    return df


def df_to_bq(df: pd.DataFrame, destination_table: str) -> None:
    logging.info(f"\nLoading table to BQ {destination_table}: \n{df.head()}")

    credentials = service_account.Credentials.from_service_account_file(
        f"{secrets_path}/credentials.json",
    )

    df.to_gbq(
        project_id=gcp_project,
        destination_table=destination_table,
        if_exists="replace",
        chunksize=10_000,
        credentials=credentials,
    )