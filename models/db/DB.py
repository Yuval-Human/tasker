class DB:
    def __init__(self):
        self.database = {}

    def store(self, obj):
        self.database.update(obj)

    def get(self, key):
        return self.database.get(key)
