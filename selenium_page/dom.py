from selenium.remote import WebElement

class DomElement:
    def __init__(self, driver_or_elemenet, parent):
        self.driver_or_elemenet = driver_or_elemenet
        self.parent = parent

    def has_class(self, cls):
        pass

    def attr(self, name):
        pass

    def driver(self):
        return self.driver._parent

    def xpath(self, *args, **kwargs):
        self.driver_or_elemenet.find_element_by_xpath(*args, **kwargs)

    def __getattr__(self, name):
        if hasattr(self.driver_or_elemenet, name):
            return self._proxy_to_driver

    def _proxy_to_driver(self, *args, **kwargs):
        pass

class DriverAttributeProxy:
    def __init__(self, name, driver_or_element, parent):
        self.driver_or_element = driver_or_element
        self.name = name
        self.parent = paretn

    def __call__(self, *args, **kwargs):
        ret = self.driver_or_element(*args, **kwargs)

        if isinstance(ret, WebElement):
            return DomElement(self.driver_or_element, parent)

        return ret
