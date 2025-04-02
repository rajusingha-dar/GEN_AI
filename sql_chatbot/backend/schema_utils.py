from backend.db_config import get_db_connection

def get_db_schema_summary():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Get table names
    cursor.execute("SHOW TABLES")
    tables = [row[0] for row in cursor.fetchall()]

    schema_summary = []

    for table in tables:
        cursor.execute(f"DESCRIBE {table}")
        columns = [col[0] for col in cursor.fetchall()]
        schema_summary.append(f"{table}({', '.join(columns)})")

    cursor.close()
    conn.close()

    return "Database Tables:\n" + "\n".join(schema_summary)
