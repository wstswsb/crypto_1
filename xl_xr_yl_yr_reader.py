from models import XlXrYlYrTriad, XlXrYlYr


class XlXrYlYrReader:
    def __init__(self, path_resources: str):
        self.path_resources = path_resources

    def read(self, filename: str) -> list[XlXrYlYrTriad]:
        content = self.read_content(filename)
        return self.parse_triads(content)

    def read_content(self, filename: str) -> str:
        with open(f"{self.path_resources}/{filename}", "r") as file:
            content = file.read()
        return content

    def parse_triads(
            self,
            content: str) -> list[XlXrYlYrTriad]:
        raw_triads = self.parse_raw_triads(content)
        return [
            self.parse_raw_triad(raw_triad)
            for raw_triad in raw_triads
        ]

    def parse_raw_triads(self, content: str):
        triads = [
            item
            for item in content.split(" ---  ---  ---  --- \n")
            if '0' in item or '1' in item
        ]
        return triads

    def parse_raw_triad(self, raw_triad: str):
        lines = raw_triad.split("\n")
        triad_args: list[XlXrYlYr] = [
            self.parse_line(line)
            for line in lines[:-1]
        ]
        return XlXrYlYrTriad(*triad_args)

    def parse_line(self, line: str) -> XlXrYlYr:
        numbers = [
            self.parse_num(num)
            for num
            in line.split("---")[:-1]]
        return XlXrYlYr(*numbers)

    def parse_num(self, num: str) -> int:
        return int(num.strip(), 2)
