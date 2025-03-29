from htmlnode import *
from splitblocks import *
from splitnodes import *
from parentnode import *
from texttotextnodes import *
from leafnode import *

def markdown_to_html_node(markdown) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        try:
            node = create_node(block)
            children.append(node)
        except Exception as e:
            print(e)
    return ParentNode(tag="div", children=children)

def create_code_html_node(block) -> HTMLNode:
    print(block)
    block = block.strip("```").lstrip("\n")
    text_node = TextNode(text=block, text_type=TextType.CODE)
    return ParentNode(tag="pre", children=[LeafNode(tag="code", value=text_node.text)])

def create_paragraph_html_node(block) -> HTMLNode:
    ...

def create_ordered_list_html_node(block) -> HTMLNode:
    ...

def create_unordered_list_html_node(block) -> HTMLNode:
    ...

def create_heading_html_node(block) -> HTMLNode:
    ...

def create_quote_html_node(block) -> HTMLNode:
    ...

def create_node(block: str):
    tp = block_to_block_type(block)
    match tp:
        case BlockType.paragraph:
            return create_paragraph_html_node(block)
        case BlockType.code:
            return create_code_html_node(block)
        case BlockType.quote:
            return create_quote_html_node(block)
        case BlockType.ordered_list:
            return create_ordered_list_html_node(block)
        case BlockType.unordered_list:
            return create_unordered_list_html_node(block)
        case BlockType.heading:
            return create_heading_html_node(block)
        case _:
            raise Exception("Block Type couldn't be determined")
         

#should return a list of html nodes.
#if the block type is we don't need to format
#the text as if it's a paragraph.
def text_to_children(text):
    ...

if __name__ == "__main__":
    print(markdown_to_html_node("""
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """
    ).to_html())