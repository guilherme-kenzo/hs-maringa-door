import sqlite3


DB_TYPES_TO_PYTHON_TYPES = {
    "NULL": None,
    "INTEGERS": int,
    "REAL": float,
    "TEXT": str,
    "BLOB": object,
}


class DB:
    def __init__(self, db_file: str):
        self.db_file: str = db_file
        self.table: str = None
        self.conn: sqlite3.Connection = self._make_con()
        self.fields: list[tuple[str, str]]  # a list of tuples
        # [0] the name of the field and [1] the type of the field

    def _make_con(self):
        return sqlite3.connect(self.db_file)

    def get(self, id: str):
        raise NotImplementedError

    def remove(self, id: str):
        raise NotImplementedError

    def search(self, *args, **kwargs):
        raise NotImplementedError

    def make_table_if_not_exists(self):
        query = f"""
            CREATE TABLE IF NOT EXISTS {self.table} ({''.join(i for i in self.fields)});
        """
        cursor = self.conn.cursor()
        cursor.execute(query)
        response = self.conn.commit()
        cursor.close()
        return response

    def validate_data(self, raise_on_error=True, **kwargs):
        """Validates data checking the type of each of the keyword arguments.

        Each of the keyword arguments will be compared to their types entry in the
        DB_TYPES_TO_PYTHON_TYPES dictionary.

        Args:
            raise_on_error (bool, optional): _description_. Defaults to True.

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        for field, type_ in self.fields:
            if not isinstance(kwargs[field], DB_TYPES_TO_PYTHON_TYPES[field]):
                if raise_on_error:
                    raise ValueError(
                        (
                            f"Type {type_} of field {field} does not match the type "
                            f"of the field ({DB_TYPES_TO_PYTHON_TYPES[field]})."
                        )
                    )
                return False
        return True


class User(DB):
    def __init__(self, db_file: str):
        super().__init__(db_file)
        self.table = "users"
        self.fields = [("name", "TEXT"), ("email", "TEXT"), ("password", "TEXT")]

    def get(self, id: str):
        """Gets a user by its id.

        This method is implements direct sql query to the 'users'
        table.
        """
        query = f"""SELECT * FROM {self.table} WHERE id=?"""
        cursor = self.conn.cursor()
        cursor.execute(query, (id,))
        user = cursor.fetchone()
        cursor.close()
        return user

    def remove(self, id: str):
        """Remove a user by its id.

        This method is implements direct sql query to the 'users'
        table.
        """
        query = f"""DELETE * FROM {self.table} WHERE id=?"""
        cursor = self.conn.cursor()
        cursor.execute(query, (id,))
        cursor.close()
        return id

    def search(self, email: str = None, name: str = None):
        """Searches users by their email OR (XOR) name.

        This method is implements direct sql query to the 'users'
        table search, using the 'like' operator. Only normalization
        performed is to lower the text case.
        """
        email = email.lower()
        name = email.lower()
        query = f"""SELECT * FROM {self.table} WHERE email=?"""
        cursor = self.conn.cursor()
        cursor.execute(query, (id,))
        users = cursor.fetchall()
        query = f"""SELECT * FROM {self.table} WHERE name=?"""
        cursor.execute(query, (id,))
        users = users.extend(cursor.fetchall())
        cursor.close()
        return users
