from sqlalchemy import create_engine
import pandas as pd
import logging

def load_data(df):
    logging.info("Starting load")

    engine = create_engine(
        'postgresql+psycopg2://user:password@postgres:5432/etl_db'
    )

    try:
        existing_df = pd.read_sql("SELECT * FROM api_users", engine)
        df = df[~df['id'].isin(existing_df['id'])]
    except:
        logging.info("First load")

    df.to_sql('api_users', engine, if_exists='append', index=False)

    logging.info(f"Inserted {len(df)} rows")