from .container import ObjectsContainer

class BaseObject(ObjectsContainer):

    def click(self):
        self.element().click()

ObjectsContainer.add_handler('base', BaseObject)
