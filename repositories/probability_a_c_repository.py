from .sqlite_repository import SqliteRepository
from models import ProbabilityAC


class ProbabilityACRepository(SqliteRepository):
    def insert_one(self, model: ProbabilityAC):
        query = f"INSERT INTO {self.table_name} VALUES" \
                f"(:a, :c, :probability)"

        self.cursor.execute(query, self.translator.to_dict(model))
        self.connection.commit()
        return self.cursor.lastrowid

    def insert_many(self, list_models: list[ProbabilityAC]):
        query = f"INSERT INTO {self.table_name} VALUES" \
                f"(:a, :c, :probability)"

        list_models = [self.translator.to_dict(model) for model in list_models]
        self.cursor.executemany(query, list_models)
        self.connection.commit()

    def find_four_most_probability(self) -> list[ProbabilityAC]:
        query = f"SELECT a, c, probability FROM {self.table_name} " \
                f"ORDER BY probability DESC LIMIT 4"
        self.cursor.execute(query)
        return [
            self.translator.from_db_tuple(item)
            for item in self.cursor.fetchall()
        ]
