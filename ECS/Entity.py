from abc import ABC, abstractmethod

class Component:
    def __init__(self):
        self.name = ""

    @abstractmethod
    def update(self):
        pass


class Entity:
    def __init__(self, name="", tags=[], components = []):
        self.name = name
        self.tags = tags
        self.components = components

    def addTag(self, tag):
        self.tags.append(tag);
    def addComponent(self, component):
        self.components.append(component);

    def getComponent(self, componentname):
        for component in self.components:
            if component.name == componentname:
                return component;


    def update(self):
        for component in self.components:
            component.update()