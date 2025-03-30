import unittest
from markdowntohtml import *
from htmlnode import *


class TestMarkdownToHTML(unittest.TestCase):

    def test_paragraphs(self):
        md = """
        This is **bolded** paragraph
        text in a p
        tag here

        This is another paragraph with _italic_ text and `code` here

        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

    def test_codeblock(self):
        md = """
        ```
        This is text that _should_ remain
        the **same** even with inline stuff
        ```
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )
    
    @unittest.skip("")
    def test_quoteblock(self):
        md = """
        > This is a quote block
        > that has _italic_ word
        > and a **bold** word
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,
        "<div><blockquote>\nThis is a quote block that has <i>italic</i> word and a <b>bold</b> word\n</blockquote></div>"
        )

    def test_unordered_list(self):
        md = """
        - one
        - two
        - three
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,""
        "<div><ul><li>one</li><li>two</li><li>three</li></ul></div>"
        )

    def test_ordered_list(self):
        md = """
        1. one
        2. two
        3. three
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, ""
        "<div><ol><li>one</li><li>two</li><li>three</li></ol></div>"
        )

        md2 = """
        1. this **item** has some bold.
        2. this _item_ has some italic.
        3. this `item` has some code.
        """
        node = markdown_to_html_node(md2)
        html = node.to_html()
        self.assertEqual(html, ""
        "<div><ol><li>this <b>item</b> has some bold.</li><li>this <i>item</i> has some italic.</li><li>this <code>item</code> has some code.</li></ol></div>"
        )


    @unittest.skip("")
    def test_headings(self):
        md = """
        # Heading 1
        ## Heading 2
        ### Heading 3
        #### Heading 4
        ##### Heading 5
        ###### Heading 6
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,
        "<div><h1>Heading 1</h1>\n<h2>Heading 2</h2>\n<h3>Heading 3</h3>\n<h4>Heading 4</h4>\n<h5>Heading 5</h5>\n<h6>Heading 6</h6>\n</div>"
        )

if __name__ == "__main__":
    unittest.main