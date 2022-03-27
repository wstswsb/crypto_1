from structure import first_s_block_analytics_service


class TestFirstSBlockAnalyticsService:
    def setup(self):
        self.service = first_s_block_analytics_service
        self.repository = self.service.a_in_out_c_repository

    def teardown(self):
        self.repository.cursor.execute(f"DELETE FROM {self.repository.table_name}")
        self.repository.connection.commit()

    def test_generate_in_out_c_equals_inputs(self):
        a = 0b0000
        input_1 = 0b1010
        result = self.service.generate_a_in_out_c(a, input_1)
        assert result.a == a
        assert result.input_1 == input_1
        assert result.input_2 == input_1
        assert result.output_1 == 0b0101
        assert result.output_2 == 0b0101
        assert result.c == 0

    def test_generate_in_out_c_case_1(self):
        a = 0b1111
        input_1 = 0b0001
        result = self.service.generate_a_in_out_c(a, input_1)
        assert result.a == a
        assert result.input_1 == input_1
        assert result.input_2 == 0b1110
        assert result.output_1 == 0b0110
        assert result.output_2 == 0b0000
        assert result.c == 0b0110

    def test_generate_in_out_c_case_2(self):
        a = 0b0101
        input_1 = 0b0001
        result = self.service.generate_a_in_out_c(a, input_1)
        assert result.a == a
        assert result.input_1 == input_1
        assert result.input_2 == 0b0100
        assert result.output_1 == 0b0110
        assert result.output_2 == 0b0001
        assert result.c == 0b0111

    def test_build_a_inputs_outputs_table(self):
        self.service.build_a_inputs_outputs_table()
        self.repository.cursor.execute(f"SELECT * FROM {self.repository.table_name}")
        values = self.repository.cursor.fetchall()
        assert len(values) == 256
