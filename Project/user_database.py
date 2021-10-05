import database
import mysql


class UserDatabase(database.Database):

    def __init__(self, table):
        super().__init__(table)

    def add(self, user):
        return

    def get(self):
        return None

    def update(self):
        return

    def delete(self, user):
        return
