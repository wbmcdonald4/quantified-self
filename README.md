# quantified-self
This guide assumes familiarity with BigQuery & Google Cloud Platform. If you are not familiar, refer to [this guide](https://cloud.google.com/bigquery/docs/how-to) to try it out, you might even get a free trial!


### Quick Start Guide
To get started with setting up a local airflow instance, follow the steps below.

1. clone the repo

2. create `.env` file with relevant environment variables in the root directory. Example:

```
# repo settings
AIRFLOW_UID=50000
SECRETS_PATH="/opt/airflow/secrets"

# personal tokens
OURA_TOKEN={YOUR_API_TOKEN}
```

3. create a `secrets` directory, and add your `credentials.json` that you get from creating a service account on Google Cloud Platform (Make sure the file is named credentials.json)

4. run `docker-compose up airflow-init` if it's your first time

5. run `docker-compose up`

6. visit https://localhost:8080/home

7. login with `username: airflow; password: airflow`

8. Voila! You're in. Now you can play around with the Airflow interface, and try adding your own custom dags. 
