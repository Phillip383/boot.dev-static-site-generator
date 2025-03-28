import unittest
from texttotextnodes import *
from textnode import *

class TestTextToTextNodes(unittest.TestCase):
    def test_eq(self):
        nodes = text_to_textnodes(
        "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        self.assertEqual(
        [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ], nodes)

    def test_eq_rev(self):
        print("Testing Reverse")
        nodes1 = text_to_textnodes(
            "This is _text_ with an **bold** word and some `code` and a [link](https://boot.dev) and a ![image](https://image.png)")
        self.assertEqual([
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.ITALIC),
            TextNode(" with an ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word and some ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://image.png"),
        ], nodes1)


if __name__ == "__main__":
    unittest.main
