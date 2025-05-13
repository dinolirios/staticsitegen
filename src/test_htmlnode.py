import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("div", "Hello, World!", [], {"class": "greeting"})
        node2 = HTMLNode("div", "Hello, World!", [], {"class": "greeting"})
        self.assertEqual(node, node2)

    def test_not_equal_tag(self):
        node1 = HTMLNode("div", "Hello", [], {})
        node2 = HTMLNode("span", "Hello", [], {})
        self.assertNotEqual(node1, node2)

    def test_not_equal_value(self):
        node1 = HTMLNode("div", "Hello", [], {})
        node2 = HTMLNode("div", "World", [], {})
        self.assertNotEqual(node1, node2)
    
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            'class="greeting" href="https://boot.dev"',
        )
    
