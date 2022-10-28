FROM apache/airflow:slim-2.3.3-python3.8
COPY requirements.txt .
RUN pip install -r requirements.txt