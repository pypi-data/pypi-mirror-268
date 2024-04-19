import mysql.connector


class MySQLConnection:
    def __init__(self, host: str, username: str, password: str, database: str):
        config = {
            'user': username,
            'password': password,
            'host': host,
            'database': database,
            'raise_on_warnings': False
        }
        self._cnx = mysql.connector.connect(**config)
        self._cursor = self._cnx.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self._cnx

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def execute(self, query, data):
        self.cursor.execute(query, data)

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def select(self, table_name: str, columns: list, values: list, select_columns: list = None) -> list:
        sql_template = "SELECT {sel_cols} FROM {table} WHERE {cols}"
        sql = sql_template.format(
            table=table_name,
            sel_cols=", ".join(select_columns) if select_columns else "*",
            cols="=%s AND ".join(columns) + "=%s;"
        )
        self.execute(sql, values)
        columns = self.cursor.description
        return [dict(zip([column[0] for column in columns], row)) for row in self.cursor.fetchall()]

    def insert(self, table_name: str, columns: list, values: list):
        query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s' for _ in values])})"
        self.execute(query, values)
        self.commit()

    def custom_query(self, query: str) -> list:
        self.cursor.execute(query)
        columns = self.cursor.description
        return [{columns[index][0]: column for index, column in enumerate(value)} for value in self.cursor.fetchall()]

    def update(self, table_name: str, params: dict, conditions: dict):
        query = f"UPDATE {table_name} SET "
        updates = [f"{column} = %s" for column in params]
        query += ", ".join(updates)

        values = list(params.values())

        if conditions and isinstance(conditions, dict):
            query += " WHERE "
            conditions_str = [f"{col} = %s" for col in conditions]
            query += " AND ".join(conditions_str)
            values += list(conditions.values())

        self.execute(query, values)
        self.connection.commit()

    def get_last_error(self, error_log_table_name: str, err_id_col: str, err_id: int,
                       error_type_col: str, error_type: str,
                       error_message_col: str, error_message: str,
                       error_script_path: str,
                       error_occurrence_timestamp,
                       error_repeat_minutes_range_local: int) -> dict:
        query = f"""
            SELECT * FROM {error_log_table_name} 
            WHERE {err_id_col} = {err_id}
            AND {error_type_col} = "{error_type}"
            AND {error_message_col} = "{error_message}"
            AND script_path = "{error_script_path}"
            AND error_is_handled = 0
            AND error_first_occurrence_timestamp_utc BETWEEN DATE_SUB('{error_occurrence_timestamp}', INTERVAL {error_repeat_minutes_range_local} MINUTE) AND '{error_occurrence_timestamp}'
            ORDER BY id DESC LIMIT 1;"""
        result = self.custom_query(query)
        return result[0] if result else None
