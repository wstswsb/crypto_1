from mock import Mock

from models import AInputsOutputsC
from services import SBlockAnalyticsService


class TestSBlockAnalyticsService:
    def setup(self):
        self.default_a = 3
        self.s_block_mock = Mock()
        self.bit_computing_service_mock = Mock()
        self.a_in_out_repository_mock = Mock()
        self.probability_a_c_repository_mock = Mock()

        self.service = SBlockAnalyticsService(
            s_block=self.s_block_mock,
            bit_computing_service=self.bit_computing_service_mock,
            a_in_out_c_repository=self.a_in_out_repository_mock,
            probability_a_c_repository=self.probability_a_c_repository_mock,
        )
        self.service.max_input = 0b1111
        self.service.max_output = 0b0011

    def generate_models(self) -> list[AInputsOutputsC]:
        return [
            AInputsOutputsC(3, 0, 3, 0, 2, 2),
            AInputsOutputsC(3, 1, 2, 1, 0, 1),
            AInputsOutputsC(3, 2, 1, 0, 1, 1),
            AInputsOutputsC(3, 3, 0, 2, 0, 2),
            AInputsOutputsC(3, 4, 7, 2, 3, 1),
            AInputsOutputsC(3, 5, 6, 0, 0, 0),
            AInputsOutputsC(3, 6, 5, 0, 0, 0),
            AInputsOutputsC(3, 7, 4, 3, 2, 1),
            AInputsOutputsC(3, 8, 11, 1, 1, 0),
            AInputsOutputsC(3, 9, 10, 2, 1, 3),
            AInputsOutputsC(3, 10, 9, 1, 2, 3),
            AInputsOutputsC(3, 11, 8, 1, 1, 0),
            AInputsOutputsC(3, 12, 15, 3, 2, 1),
            AInputsOutputsC(3, 13, 14, 3, 3, 0),
            AInputsOutputsC(3, 14, 13, 3, 3, 0),
            AInputsOutputsC(3, 15, 12, 2, 3, 1),

        ]

    def test_count_c(self):
        models = self.generate_models()

        result = self.service.count_c(models)
        assert result[0] == 6
        assert result[1] == 6
        assert result[2] == 2
        assert result[3] == 2

    def test_generate_probabilities_a_c(self):
        models = self.generate_models()
        self.a_in_out_repository_mock \
            .find_by_a \
            .return_value = models

        count_c_value = {
            0: 6, 1: 6,
            2: 2, 3: 2,
        }
        self.service.count_c = Mock(return_value=count_c_value)
        result = self.service.generate_probabilities_a_c(self.default_a)

        c_0_model, c_1_model, c_2_model, c_3_model = result
        assert c_0_model.probability == 6 / 16
        assert c_1_model.probability == 6 / 16
        assert c_2_model.probability == 2 / 16
        assert c_3_model.probability == 2 / 16
