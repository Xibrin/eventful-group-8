import database
import mysql


class EventDatabase(database.Database):

    def __init__(self, table):
        super().__init__(table)

    def add(self, event):
        return

    def get(self):
        return None

    def update(self):
        return

    def delete(self, event):
        return
