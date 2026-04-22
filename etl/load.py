import psycopg2
import pandas as pd
import os
from config.config import TRANSFORMED_DATA_PATH
def load_data():
    try:
        print("===== LOAD START =====")

        path = TRANSFORMED_DATA_PATH

        # ✅ Check file exists
        if not os.path.exists(path):
            raise Exception("❌ transformed.csv not found")

        # ✅ Read CSV
        df = pd.read_csv(path)
        print("CSV Loaded:", df.shape)

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
                id INT,
                name TEXT,
                email TEXT
            );
        """)

        # ✅ Insert data row by row
        for _, row in df.iterrows():
            cursor.execute(
                "INSERT INTO api_users (id, name, email) VALUES (%s, %s, %s)",
                (int(row['id']), row['name'], row['email'])
            )

        # ✅ Commit and close
        conn.commit()
        cursor.close()
        conn.close()

        print("✅ Data inserted successfully")

    except Exception as e:
        print("❌ ERROR:", str(e))
        raise