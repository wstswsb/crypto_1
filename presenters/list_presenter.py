class ListPresenter:
    def __init__(self, item_presenter):
        self.item_presenter = item_presenter

    def present(self, models: list) -> str:
        return ",\n".join(
            [
                self.item_presenter.present(model)
                for model
                in models
            ]
        )
