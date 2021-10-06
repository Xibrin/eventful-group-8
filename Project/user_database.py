import database
import mysql.connector


class UserDatabase(database.Database):
    __class_instance = None

    def __init__(self, table):
        if UserDatabase.__class_instance:
            raise RuntimeError()
        else:
            UserDatabase.__class_instance = self
            super().__init__(table)

    def add(self, user):
        return

    def get(self):
        return None

    def update(self):
        return

    def delete(self, user):
        return
