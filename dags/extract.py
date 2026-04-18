import requests
import pandas as pd
import logging

def extract_data():
    logging.info("Starting API extraction")

    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("API failed")

    data = response.json()

    df = pd.DataFrame(data)
    df = df[['id', 'name', 'username', 'email']]

    logging.info(f"Extracted {len(df)} records")

    return df