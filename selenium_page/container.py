import inspect
from .element import DomElement

__all__ = ['ObjectsCollection', 'ObjectsContainer']

class ObjectsCollection:

    def __init__(self, driver, parent):
        self.driver = driver
        self.objects = {}
        self.parent = parent

    def append(self, name, selector=None, kind=None, parent=None):
        if inspect.isclass(kind):
            klass = kind
        else:
            klass = self.parent.__class__

        object_parent = parent or self.parent
        self.objects[name] = klass(self.driver, selector, object_parent)

    def __call__(self, name):
        return self.objects.get(name)


class ObjectsContainer:
    _handlers = {}

    def __init__(self, driver, selector=None, parent=None):
        self.driver = driver
        self.selector = selector
        self.parent = parent
        self.element = DomElement(self.driver, self.selector)

    def __getattr__(self, name):
        if name.startswith('add_'):
            name = name[4:]

            if not hasattr(self, name):
                setattr(self, name, ObjectsCollection(self.driver, self))

            return getattr(self, name).append

        raise AttributeError('Object hasn\'t attribute named "%s" ' % name)

    @staticmethod
    def add_handler(name, handler):
        ObjectsContainer._handlers[name] = handler
