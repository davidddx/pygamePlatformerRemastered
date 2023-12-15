from abc import ABC, abstractmethod

class Entity:
    def __init__(self):
        self.parent = None
        self.children = []

    @abstractmethod
    def update(self):
        pass