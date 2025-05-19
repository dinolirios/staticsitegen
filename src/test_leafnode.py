import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!", {"href": "https://boot.dev"})
        self.assertEqual(node.to_html(), '<a href="https://boot.dev">Hello, world!</a>')

    def test_leaf_to_html_empty(self):
        node = LeafNode("p", "")
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()