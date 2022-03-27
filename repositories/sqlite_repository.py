import sqlite3

from translators import BaseTranslator


class SqliteRepository:
    def __init__(
            self,
            translator: BaseTranslator,
            db_path: str,
            table_name: str,
            table_generation_script: str):
        self.translator = translator
        self.table_name = table_name
        self.db_path = db_path

        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

        self.create_table(table_generation_script)

    def create_table(self, table_generation_script: str):
        self.cursor.execute(table_generation_script)

    def generate_questions_marks(self, number: int) -> str:
        return ",".join(["?" for _ in range(number)])
