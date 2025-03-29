import unittest
from splitblocks import *

class TestSplitBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
        This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
    )

        md2 = """
        Another **markdown** example with _italic_ text and some images and links.

        The link for the best developer help is [google](https://www.google.com)
        ![google is amazing](https://google.jpeg)

        LinkedIn is also a great resource to learn development.
        [LinkedIn](https://www.linkedin.com)
        ![LinkedIn is chill](https://linkedin.jpeg)

        yet Boot.dev regins supreme.
        [Boot.dev](https://www.boot.dev)
        ![boot.dev](https://boot.dev.jpeg)
        """
        blocks2 = markdown_to_blocks(md2)
        self.assertEqual(blocks2,[
            "Another **markdown** example with _italic_ text and some images and links.",
            "The link for the best developer help is [google](https://www.google.com)\n![google is amazing](https://google.jpeg)",
            "LinkedIn is also a great resource to learn development.\n[LinkedIn](https://www.linkedin.com)\n![LinkedIn is chill](https://linkedin.jpeg)",
            "yet Boot.dev regins supreme.\n[Boot.dev](https://www.boot.dev)\n![boot.dev](https://boot.dev.jpeg)"
        ])

if __name__ == "__main__":
    unittest.main
