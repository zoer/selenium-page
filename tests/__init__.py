import unittest

from .test_container import TestContainer
from .test_element import TestElement

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestContainer))
    suite.addTest(unittest.makeSuite(TestElement))
    return suite
