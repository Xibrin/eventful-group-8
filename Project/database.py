from abc import ABC, abstractmethod
import mysql


class Database(ABC):

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