import psycopg2
import pandas as pd
import os
import logging

from config.config import TRANSFORMED_DATA_PATH

logging.basicConfig(level=logging.INFO)

def load_data():
    try:
        logging.info("🚀 LOAD STARTED")

        path = TRANSFORMED_DATA_PATH

        # ✅ Check file exists
        if not os.path.exists(path):
            raise Exception("❌ transformed.csv not found")

        # ✅ Read CSV
        df = pd.read_csv(path)
        logging.info(f"CSV Loaded: {df.shape}")

        # ✅ Connect to PostgreSQL
        conn = psycopg2.connect(
            host="postgres",
            database="etl_db",
            user="postgres",
            password="postgres",
            port="5432"
        )

        cursor = conn.cursor()

        # ✅ Create table if not exists
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS api_users (
                id INT PRIMARY KEY,
                name TEXT,
                email TEXT
            );
        """)

        # ✅ Insert data (IDEMPOTENT - no duplicates)
        for _, row in df.iterrows():
            cursor.execute(
                """
                INSERT INTO api_users (id, name, email)
                VALUES (%s, %s, %s)
                ON CONFLICT (id) DO NOTHING
                """,
                (int(row['id']), row['name'], row['email'])
            )

        # ✅ Commit changes
        conn.commit()

        # ✅ Close connection
        cursor.close()
        conn.close()

        logging.info("✅ Data inserted successfully (no duplicates)")

    except Exception as e:
        logging.error(f"❌ ERROR: {str(e)}")
        raise