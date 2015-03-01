from selenium.webdriver.common.by import By


class DomElement:
    def __init__(self, driver, selector=None):
        self.driver = driver
        self.selector = selector

    def element(self):
        '''Get selenium WebElement'''

        selector = self.selector
        if isinstance(selector, str) and selector.startswith('//'):
            selector = (By.XPATH, selector)

        if isinstance(selector, tuple):
            return self.driver.find_element(*selector)

        return selector

    def __call__(self):
        return self.element()
