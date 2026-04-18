import logging

def transform_data(df):
    logging.info("Starting transformation")

    if df.empty:
        raise ValueError("Data is empty")

    df['email'] = df['email'].str.lower()

    logging.info("Transformation completed")

    return df