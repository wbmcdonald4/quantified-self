from os import getenv

import requests

class Oura():
    def __init__(self):
        self.access_token = getenv("OURA_TOKEN")
        self.headers = {
        "Authorization": f"Bearer {self.access_token}"
        }

    def get_sleep_score(self, start_date, end_date):
        params = {
            'start_date': start_date,
            'end_date': end_date,
            }
        r = requests.get('https://api.ouraring.com/v2/usercollection/daily_sleep', params=params, headers=self.headers)
        return r.json()['data']