from infraless.controllers.base import Base


def load(app):
    app.handler.register(Base)
