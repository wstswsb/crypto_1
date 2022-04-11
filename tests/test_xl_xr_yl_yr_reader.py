from structure import xl_xr_yl_yr_reader
from mock import Mock


class TestXlXrYlYrReader:
    def setup(self):
        self.reader = xl_xr_yl_yr_reader
        self.reader.path_resources += "/test"
        self.filename = "xl_xr_yl_yr.txt"

    def test_parse_triads(self):
        self.reader.read_content = Mock(
            return_value=self.expected_content_for_parse_triads
        )
        result = self.reader.read(self.filename)
        triad = result[0]
        assert triad.xl_xr_yr_yl_1.xl == 0b01011101
        assert triad.xl_xr_yr_yl_1.xr == 0b01111100
        assert triad.xl_xr_yr_yl_1.yl == 0b11001010
        assert triad.xl_xr_yr_yl_1.yr == 0b10111010

        assert triad.xl_xr_yr_yl_2.xl == 0b00001010
        assert triad.xl_xr_yr_yl_2.xr == 0b00010011
        assert triad.xl_xr_yr_yl_2.yl == 0b10011101
        assert triad.xl_xr_yr_yl_2.yr == 0b11010101

        assert triad.delta_xl_xr_yr_yl.xl == 0b01010111
        assert triad.delta_xl_xr_yr_yl.xr == 0b01101111
        assert triad.delta_xl_xr_yr_yl.yl == 0b01010111
        assert triad.delta_xl_xr_yr_yl.yr == 0b01101111

    @property
    def expected_content_for_parse_triads(self):
        return "01011101 --- 01111100 --- 11001010 --- 10111010 --- \n" \
               "00001010 --- 00010011 --- 10011101 --- 11010101 --- \n" \
               "01010111 --- 01101111 --- 01010111 --- 01101111 --- \n" \
               " ---  ---  ---  --- \n" \
               " ---  ---  ---  --- \n" \
               " ---  ---  ---  --- \n"
