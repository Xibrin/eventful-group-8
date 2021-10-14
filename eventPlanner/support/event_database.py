import database
import mysql.connector


class EventDatabase(database.Database):
    __class_instance = None

    def __init__(self, table):
        if EventDatabase.__class_instance:
            raise RuntimeError()
        else:
            EventDatabase.__class_instance = self
            super().__init__()
            self.table = table
            # TODO: Add statement to CREATE table IF NOT EXISTS
            super().close()

    def add(self, event):
        return

    def get(self):
        return None

    def update(self):
        return

    def delete(self, event):
        return

