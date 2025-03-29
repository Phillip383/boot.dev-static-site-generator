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
        
    # Test Block Types
    def test_block_types(self):
        block1 = block_to_block_type("```This is a code Block```")
        self.assertEqual(block1, BlockType.code)

        block2 = block_to_block_type("# heading 1")
        self.assertEqual(block2, BlockType.heading)

        block3 = block_to_block_type("##### heading 5")
        self.assertEqual(block3, BlockType.heading)

        block4 = block_to_block_type("> This is a quote block with\n> 2 lines")
        self.assertEqual(block4, BlockType.quote)

        block5 = block_to_block_type("- This is a unordered list\n- with 3 list\n- elements ")
        self.assertEqual(block5, BlockType.unordered_list)

        block6 = block_to_block_type("1. This is an ordered list\n2. with 3 list\n3. elements")
        self.assertEqual(block6, BlockType.ordered_list)

        block7 = block_to_block_type("```This should be a paragraph because it does not have closing ticks")
        self.assertEqual(block7, BlockType.paragraph)

        block8 = block_to_block_type("1. This is a failed ordered list\n3. with 2 elements")
        self.assertEqual(block8, BlockType.paragraph)

        block9 = block_to_block_type("- THis is a failed unordered list\n-because it's missing white space.")
        self.assertEqual(block9, BlockType.paragraph)

        block10 = block_to_block_type("> This is a failed quote\nbecause every line doesn't start with >")
        self.assertEqual(block10, BlockType.paragraph)


if __name__ == "__main__":
    unittest.main
