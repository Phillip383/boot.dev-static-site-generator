from htmlnode import *
from splitblocks import *
from splitnodes import *
from parentnode import *
from texttotextnodes import *
from leafnode import *
from textnode import *
import re

def markdown_to_html_node(markdown) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        if len(block) == 0:
            continue
        try:
            node = create_node(block)
            children.append(node)
        except Exception as e:
            print(e)
    return ParentNode(tag="div", children=children)

def create_code_html_node(block) -> HTMLNode:
    block = block.strip("```").lstrip("\n")
    text_node = TextNode(text=block, text_type=TextType.CODE)
    return ParentNode(tag="pre", children=[LeafNode(tag="code", value=text_node.text)])

def create_paragraph_html_node(block) -> HTMLNode:
    block = block.replace("\n", " ")
    children = text_to_children(block)
    return ParentNode(tag="p", children=children)

def create_ordered_list_html_node(block) -> HTMLNode:
    blocks = block.split("\n")

    children = []
    for b in blocks:
        t = b[b.find(" "):].strip()
        children.append(ParentNode(tag="li", children=text_to_children(t)))
    return ParentNode(tag="ol", children=children)

def create_unordered_list_html_node(block) -> HTMLNode:
    blocks = block.split("\n")

    children = []
    for b in blocks:
        t = b[b.find(" "):].strip()
        children.append(ParentNode(tag="li", children=text_to_children(t)))
    return ParentNode(tag="ul", children=children)

def create_heading_html_node(block) -> HTMLNode:
    #use this as like h{heading_count} in the tag
    #probably need to do this on a child of the block.
    heading_count = block.count("#")
    return HTMLNode()

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
def text_to_children(text):
    children_text_nodes = text_to_textnodes(text)
    children = []
    for node in children_text_nodes:
        children.append(TextNode.text_node_to_html_node(node))
    return children

if __name__ == "__main__":
    print(markdown_to_html_node("""
    1. one
    2. two
    3. three
    """
    ).to_html())
