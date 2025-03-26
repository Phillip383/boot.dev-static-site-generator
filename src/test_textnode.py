import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)

        node3 = TextNode("This is a text node", TextType.ITALIC)
        node4 = TextNode("This is another text node", TextType.BOLD)
        self.assertEqual(node, node2)
        self.assertNotEqual(node3, node4)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node: HTMLNode = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode(text="This is a bold node", text_type=TextType.BOLD)
        html_node: HTMLNode = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        node = TextNode(text="This is a italic node", text_type=TextType.ITALIC)
        html_node: HTMLNode = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic node")

    def test_code(self):
        node = TextNode(text="This is a code node", text_type=TextType.CODE)
        html_node: HTMLNode = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")
    
    def test_link(self):
        node = TextNode(text="This is a link node",url="www.test.com", text_type=TextType.LINK)
        html_node: HTMLNode = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props["href"], "www.test.com")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.to_html(), "<a href=\"www.test.com\">This is a link node</a>")

    def test_img(self):
        node = TextNode(text="This is a image node", url="/home/pics/test.png", text_type=TextType.IMAGE)
        html_node: HTMLNode = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props["src"], "/home/pics/test.png")
        self.assertEqual(html_node.props["alt"], "This is a image node")
        self.assertEqual(html_node.to_html(), "<img src=\"/home/pics/test.png\" alt=\"This is a image node\"></img>")

if __name__ == "__main__":
    unittest.main()
