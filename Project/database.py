from abc import ABC, abstractmethod
import os
import mysql.connector


class Database(ABC):

    def __init__(self):
        self.database = "Something"  # TODO: Think of a name
        self.connection = mysql.connector.connect(
            user=os.getenv("MYSQL_USERNAME"),
            password=os.getenv("MYSQL_PASSWORD")
        )
        self.cursor = self.connection.cursor()
        # TODO: Add statement to CREATE database IF NOT EXISTS

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

    def open(self):
        self.connection = mysql.connector.connect(
            user=os.getenv("MYSQL_USERNAME"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=self.database
        )
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()
