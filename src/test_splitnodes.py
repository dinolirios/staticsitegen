import unittest

from textnode import TextNode, TextType

from splitnodes_delimiter import *

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_one_delimiter(self):
        """
        Tests splitting with one pair of delimiters.
        """
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0], TextNode("This is text with a ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("code block", TextType.CODE))
        self.assertEqual(new_nodes[2], TextNode(" word", TextType.TEXT))

    def test_split_multiple_delimiters(self):
        """
        Tests splitting with multiple pairs of the same delimiter.
        """
        node = TextNode("`code1` text `code2` more text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 4) # Corrected expected length
        self.assertEqual(new_nodes[0], TextNode("code1", TextType.CODE))
        self.assertEqual(new_nodes[1], TextNode(" text ", TextType.TEXT))
        self.assertEqual(new_nodes[2], TextNode("code2", TextType.CODE))
        self.assertEqual(new_nodes[3], TextNode(" more text", TextType.TEXT))

    def test_split_delimiter_at_start_and_end(self):
        """
        Tests splitting when the delimiter is at the beginning and end of the text.
        """
        node = TextNode("`code block`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0], TextNode("code block", TextType.CODE))

    def test_split_delimiter_only(self):
        """
        Tests splitting with only delimiters and no content.
        """
        node = TextNode("``", TextType.TEXT) # Represents an empty code block
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0], TextNode("", TextType.CODE))

    def test_split_multiple_nodes_mixed_types(self):
        """
        Tests splitting a list containing mixed node types.
        Only TEXT nodes should be split.
        """
        node1 = TextNode("text **bold** text", TextType.TEXT)
        node2 = TextNode("already bold", TextType.BOLD)
        node3 = TextNode("more text _italic_ text", TextType.TEXT)
        node4 = TextNode("already code", TextType.CODE)

        old_nodes = [node1, node2, node3, node4]
        # First split by bold
        nodes_after_bold = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(len(nodes_after_bold), 6)

        self.assertEqual(nodes_after_bold[0], TextNode("text ", TextType.TEXT))
        self.assertEqual(nodes_after_bold[1], TextNode("bold", TextType.BOLD))
        self.assertEqual(nodes_after_bold[2], TextNode(" text", TextType.TEXT))
        self.assertEqual(nodes_after_bold[3], node2)
        self.assertEqual(nodes_after_bold[4], node3)
        self.assertEqual(nodes_after_bold[5], node4)

        # Then split the result by italic
        nodes_after_italic = split_nodes_delimiter(nodes_after_bold, "_", TextType.ITALIC)
        self.assertEqual(len(nodes_after_italic), 8)

        self.assertEqual(nodes_after_italic[0], nodes_after_bold[0])
        self.assertEqual(nodes_after_italic[1], nodes_after_bold[1])
        self.assertEqual(nodes_after_italic[2], nodes_after_bold[2])
        self.assertEqual(nodes_after_italic[3], nodes_after_bold[3])
        self.assertEqual(nodes_after_italic[4], TextNode("more text ", TextType.TEXT))
        self.assertEqual(nodes_after_italic[5], TextNode("italic", TextType.ITALIC))
        self.assertEqual(nodes_after_italic[6], TextNode(" text", TextType.TEXT))
        self.assertEqual(nodes_after_italic[7], nodes_after_bold[5])


    def test_split_no_delimiter(self):
        """
        Tests splitting when the delimiter is not present.
        """
        node = TextNode("This is just text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0], node)

if __name__ == "__main__":
    unittest.main()