from selenium.webdriver.common.by import By
import unittest
from unittest.mock import MagicMock, Mock
import selenium_page as sp


class TestElement(unittest.TestCase):
    def setUp(self):
        self.driver = Mock()
        self.driver.find_element = MagicMock(return_value=True)

    def test_selectors(self):
        expected = (By.XPATH, '//div')
        selectors = ('//div', expected)

        for selector in selectors:
            dom = sp.DomElement(self.driver, selector)
            self.assertTrue(dom.element())
            self.driver.find_element.assert_called_with(*expected)

    def test_custom_selector(self):
        selector = object()
        dom = sp.DomElement(self.driver, selector)
        self.assertEqual(dom.element(), selector)

    def test_alias(self):
        dom = sp.DomElement(self.driver)
        dom.element = MagicMock(return_value=True)

        self.assertEqual(dom(), True)
        dom.element.assert_called_with()


if __name__ == '__main__':
    unittest.main()
