import unittest

from splitnodes import *
from textnode import *
class TestSplitNodes(unittest.TestCase):
    
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )

    def test_split_links(self):
        node = TextNode(
            "This is a text with an [link](https://www.google.com) and another [second link](www.bing.com)", 
            TextType.TEXT,
            )
        new_nodes = split_nodes_link([node])
        self.assertEqual([
            TextNode("This is a text with an ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://www.google.com"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second link", TextType.LINK, "www.bing.com")
        ], 
        new_nodes,
    )

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
    
    def test_extract_link(self):
        data = extract_markdown_links("this is a link in markdown [a link to a cool website](www.coolwebsite.com)")
        self.assertEqual(data, (
            "a link to a cool website", "www.coolwebsite.com"
        ))

    def test_extract_image(self):
        data = extract_markdown_images("This is an image in markdown ![a cool image](/pics/coolstuff/cool.jpg)")
        self.assertEqual(data, (
            "a cool image", "/pics/coolstuff/cool.jpg"
        ))



if __name__ == "__main__":
    unittest.main

