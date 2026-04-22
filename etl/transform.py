import pandas as pd
import logging
from config.config import EXTRACTED_DATA_PATH, TRANSFORMED_DATA_PATH
def transform_data():
    logging.info("Starting transformation")

    df = pd.read_csv(EXTRACTED_DATA_PATH)

    if df.empty:
        raise ValueError("Data is empty")

    df['email'] = df['email'].str.lower()

    # 🔥 SAVE TRANSFORMED FILE
    df.to_csv(TRANSFORMED_DATA_PATH, index=False)

    logging.info("Transformation completed")