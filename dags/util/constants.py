from datetime import datetime, timedelta
from enum import Enum
from os import getenv

secrets_path = getenv("SECRETS_PATH")

gcp_project = "avid-water-361600"
# gcs_bucket = BUCKET

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2021, 5, 6),
    "email": ["ops@partnerstack.com"],
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}


# class conn_id(Enum):
#     gcs = "google_cloud_default"
#     gcp = "google_cloud_default"
#     big_query = "google_cloud_default"
#     akashi = "akashi"
#     slack_connection = "slack_connection"


class schedule(Enum):
    daily_5pm_UTC = "0 17 * * *"
    daily_12pm_UTC = "0 12 * * *"
    every_15_mins = "*/15 * * * *"
