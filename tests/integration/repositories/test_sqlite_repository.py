from structure import s_block_1_a_in_out_c_repository
from models import AInputsOutputsC


class TestSqliteAInputsOutputsCRepository:

    def setup(self):
        self.repository = s_block_1_a_in_out_c_repository

        self.translator = self.repository.translator
        self.cursor = self.repository.cursor
        self.table_name = self.repository.table_name
        self.db_path = self.repository.db_path

    def teardown(self):
        self.cursor.execute(f"DELETE FROM {self.table_name};")

    def test_init(self):
        query = "SELECT name FROM sqlite_master WHERE type='table';"

        self.cursor.execute(query)
        tables = [item[0] for item in self.cursor.fetchall()]
        assert self.repository.table_name in tables

    def test_insert_one(self):
        model = AInputsOutputsC(*range(6))
        self.repository.insert_one(model)

        query = f"SELECT a, input_1, input_2, output_1, output_2, c " \
                f"FROM {self.table_name}"
        raw_model = self.cursor.execute(query).fetchone()
        stored_model = self.translator.from_db_tuple(raw_model)

        assert stored_model == model

    def test_insert_many(self):
        models = [
            AInputsOutputsC(*range(6)),
            AInputsOutputsC(*range(1, 7)),
        ]

        self.repository.insert_many(models)
        query = f"SELECT a, input_1, input_2, output_1, output_2, c " \
                f"FROM {self.table_name}"
        raw_models = self.cursor.execute(query).fetchall()
        stored_models = [
            self.translator.from_db_tuple(raw_model)
            for raw_model
            in raw_models
        ]
        assert stored_models == models
