from abc import ABC, abstractmethod

class Component:
    @abstractmethod
    def update(self):
        pass


class Entity:
    def __init__(self, parent=None, name="", tags=[], components = []):
        self.name = name
        self.tags = tags
        self.parent = parent
        self.components = components

    def addTag(self, tag):
        self.tags.append(tag);
    def addComponent(self, component):
        self.components.append(component);

    def update(self):
        for component in self.components:
            component.update()