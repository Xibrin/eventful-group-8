from abc import ABC, abstractmethod
import mysql.connector


class Database(ABC):

    def __init__(self, table):
        self.table = table

    @abstractmethod
    def add(self, to_add):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self, to_remove):
        pass
