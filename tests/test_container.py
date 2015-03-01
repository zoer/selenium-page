import unittest
import selenium_page as sp

class TestObject(sp.ObjectsContainer): pass

class TestContainer(unittest.TestCase):
    def setUp(self):
        self.container = sp.ObjectsContainer(None)

    def test_pass_container_by_reference(self):
        cnt = self.container
        cnt.add_link('test', '//xpath', sp.ObjectsContainer)

        link = cnt.link('test')
        self.assertIsInstance(link, sp.ObjectsContainer)
        self.assertEqual('//xpath', link.selector)
        self.assertEqual(cnt, link.parent)

    def test_pass_container_by_string(self):
        cnt = self.container

        handlers = {
                'base': sp.BaseObject
                }
        for name, cls in handlers.items():
            cnt.add_object(name, kind=cls)
            self.assertIsInstance(cnt.object(name), cls)

    def test_pass_container_with_empty_type(self):
        cnt = self.container

        cnt.add_link('test', '//div/a')
        self.assertIsInstance(cnt.link('test'), cnt.__class__)

    def test_pass_specific_parent(self):
        cnt = self.container

        foo = object()
        cnt.add_link('test', '//div/a', parent=foo)
        self.assertEqual(cnt.link('test').parent, foo)

if __name__ == '__main__':
    unittest.main()
