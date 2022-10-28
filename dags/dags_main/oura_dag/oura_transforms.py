import pandas as pd

from util.df_providers import df_to_bq
from util.oura import Oura


destination_table="oura.sleep_score"

def create_dataframe(data):
    df = pd.DataFrame(data)
    return df

def transform_dataframe(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.reset_index()
    df = df.rename(columns={'index':'id'})
    df=df.drop(columns='contributors')
    return df

def main():
    oura_session = Oura()
    data = oura_session.get_sleep_score("2022-01-01", "2023-01-01")
    
    df = create_dataframe(data)
    df = transform_dataframe(df)

    df_to_bq(df, destination_table)