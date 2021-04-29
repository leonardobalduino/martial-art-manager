from flask_smorest import Blueprint as BaseBlueprint


class Blueprint(BaseBlueprint):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
