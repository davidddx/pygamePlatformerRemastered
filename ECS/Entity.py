from abc import ABC, abstractmethod

class Component:
    @abstractmethod
    def update(self):
        pass


class Entity:
    def __init__(self):
        self.parent = None
        self.components = []

    def addComponent(self, component):
        self.components.append(component);

    def update(self):
        for component in self.components:
            component.update()