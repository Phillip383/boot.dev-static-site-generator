import unittest

from splitnodes import split_nodes_delimiter
from textnode import *
class TestSplitNodes(unittest.TestCase):

    def test_bold(self):
        node_list = split_nodes_delimiter([TextNode("This has a **bold** word", TextType.TEXT)], "**", TextType.BOLD)
        self.assertEqual(node_list, [TextNode("This has a ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" word", TextType.TEXT)])

    def test_double_bold(self):
        node_list = split_nodes_delimiter([
            TextNode("This has a **bold** word, and another **bold** word", TextType.TEXT)
        ], "**", TextType.BOLD)

        self.assertEqual(node_list, [
            TextNode("This has a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word, and another ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT)
        ])

    def test_italic(self):
        node_list = split_nodes_delimiter([
            TextNode("This has a _italic_ word", TextType.TEXT)
        ], "_", TextType.ITALIC)

        self.assertEqual(node_list, [
            TextNode("This has a ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT)
        ])

    def test_double_italic(self):
        node_list = split_nodes_delimiter([
            TextNode("This has a _italic_ word, and another _italic_ word", TextType.TEXT)
        ], "_", TextType.ITALIC)

        self.assertEqual(node_list, [
            TextNode("This has a ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word, and another ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT)
        ])


    def test_code(self):
        node_list = split_nodes_delimiter([
            TextNode("This has a `code block`", TextType.TEXT)
        ], "`", TextType.CODE)

        self.assertEqual(node_list, [
            TextNode("This has a ", TextType.TEXT),
            TextNode("code block", TextType.CODE)
        ])

    def test_double_code(self):
        node_list = split_nodes_delimiter([
            TextNode("This has a `code block`, and another `code block`", TextType.TEXT)
        ], "`", TextType.CODE)

        self.assertEqual(node_list, [
            TextNode("This has a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(", and another ", TextType.TEXT),
            TextNode("code block", TextType.CODE)
        ])




if __name__ == "__main__":
    unittest.main

