import mysql
from user
from abc import ABCMeta, abstractmethod

class Database(metaclass= ABCMeta):

    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def get(self):
        pass
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def delete(self):
        pass


