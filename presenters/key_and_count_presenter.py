from models import KeyAndCount


class KeyAndCountPresenter:
    def present(self, model: KeyAndCount) -> str:
        return f"key = {hex(model.key)} \t count = {model.count}"
