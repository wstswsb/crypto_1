from .sqlite_repository import SqliteRepository
from models import KeyAndCount


class K_1_X_Repository(SqliteRepository):
    def __init__(self,
                 db_path: str,
                 table_name: str,
                 table_generation_script: str):
        super().__init__(
            None,
            db_path,
            table_name,
            table_generation_script
        )

    def insert_one(self, key: int):
        query = f"INSERT INTO {self.table_name} VALUES (?)"
        self.cursor.execute(query, (key,))
        self.connection.commit()

    def insert_many(self, keys: list[int]):
        query = f"INSERT INTO {self.table_name} VALUES (?)"
        keys = [(item,) for item in keys]
        self.cursor.executemany(query, keys)
        self.connection.commit()

    def count_keys(self):
        query = f"SELECT key, COUNT(key) as count_key " \
                f"FROM {self.table_name} " \
                f"GROUP by key " \
                f"ORDER BY count_key DESC "
        self.cursor.execute(query)
        return [KeyAndCount(*item) for item in self.cursor.fetchall()]


