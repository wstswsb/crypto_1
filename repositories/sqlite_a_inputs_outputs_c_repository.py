from .sqlite_repository import SqliteRepository
from models import AInputsOutputsC


class AInputsOutputsCRepository(SqliteRepository):
    def insert_one(self, model: AInputsOutputsC) -> int:
        query = f"INSERT INTO {self.table_name} VALUES" \
                f"(:a, :input_1, :input_2, :output_1, :output_2, :c)"

        self.cursor.execute(query, self.translator.to_dict(model))
        self.connection.commit()
        return self.cursor.lastrowid

    def insert_many(self, list_models: list[AInputsOutputsC]):
        query = f"INSERT INTO {self.table_name} VALUES" \
                f"(:a, :input_1, :input_2, :output_1, :output_2, :c)"

        list_models = [self.translator.to_dict(model) for model in list_models]
        self.cursor.executemany(query, list_models)
        self.connection.commit()

    def find_by_a(self, a: int) -> list[AInputsOutputsC]:
        query = f"SELECT a, input_1, input_2, output_1, output_2, c " \
                f"FROM {self.table_name} " \
                f"WHERE a=? ORDER BY c"
        self.cursor.execute(query, (a,))
        models = [
            self.translator.from_db_tuple(item)
            for item in self.cursor.fetchall()
        ]
        return models

    def find_by_a_and_c(self, a: int, c: int) -> list[AInputsOutputsC]:
        query = f"SELECT a, input_1, input_2, output_1, output_2, c " \
                f"FROM {self.table_name} " \
                f"WHERE (a=?) AND (c=?)"
        self.cursor.execute(query, (a, c))
        models = [
            self.translator.from_db_tuple(item)
            for item in self.cursor.fetchall()
        ]
        return models
