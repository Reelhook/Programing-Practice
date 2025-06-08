import sqlite3


def update_record(db_file, record_id, column, new_value):
    """
    Updates a single column of a maintenance record for the given record_id.

    Parameters:
      - db_file: Path to the .db file.
      - record_id: The ID of the record to update.
      - column: The name of the column to update (e.g., 'service_type', 'cost').
      - new_value: The new value to set.
    """
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # You can use parameter substitution to avoid SQL injection
    query = f"UPDATE maintenance SET {column} = ? WHERE id = ?"
    cursor.execute(query, (new_value, record_id))

    conn.commit()
    conn.close()
    print("Record updated successfully.")


# Example usage:
update_record("vehicle_maintenance.db", record_id=3, column="cost", new_value=79.99)
