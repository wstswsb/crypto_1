import json

from models import XlXrYlYr


class XlXrYlYrPresenter:
    def present(self, model: XlXrYlYr) -> str:
        return json.dumps({
            "XL": f"{model.xl:>09_b}",
            "XR": f"{model.xr:>09_b}",
            "YL": f"{model.yl:>09_b}",
            "YR": f"{model.yr:>09_b}",
        }, indent=4)
