import sqlite3
import pandas as pd

class DBHandler:
    def __init__(self, db_path):
        self.db_path = db_path

    def run_query(self, query):
        try:
            with sqlite3.connect(self.db_path) as conn:
                df = pd.read_sql_query(query, conn)
            return df
        except Exception as e:
            # Return a DataFrame with error message
            return pd.DataFrame({"Error": [str(e)]})

    def get_schema(self):
        schema = ""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tables = cursor.fetchall()
                for (table,) in tables:
                    schema += f"\nTable: {table}\n"
                    cursor.execute(f"PRAGMA table_info({table});")
                    columns = cursor.fetchall()
                    for col in columns:
                        schema += f" - {col[1]} ({col[2]})\n"
        except Exception as e:
            schema += f"Error retrieving schema: {str(e)}\n"
        return schema
