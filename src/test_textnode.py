import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal_text(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_equal_text_type(self):
        node1 = TextNode("Same text", TextType.BOLD)
        node2 = TextNode("Same text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_not_equal_url(self):
        node1 = TextNode("Link", TextType.LINK, "https://example.com")
        node2 = TextNode("Link", TextType.LINK)
        self.assertNotEqual(node1, node2)

    def test_equal_with_url(self):
        node1 = TextNode("Image", TextType.IMAGE, "https://example.com/image.png")
        node2 = TextNode("Image", TextType.IMAGE, "https://example.com/image.png")
        self.assertEqual(node1, node2)

    def test_default_url_is_none(self):
        node = TextNode("Plain", TextType.TEXT)
        self.assertIsNone(node.url)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text2(self):
        node = TextNode("This is an image", TextType.IMAGE, "facebook.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "facebook.com", "alt": "This is an image"})

if __name__ == "__main__":
    unittest.main()
