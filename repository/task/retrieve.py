import app


def get(id):
    return app.localDB.get(id)

