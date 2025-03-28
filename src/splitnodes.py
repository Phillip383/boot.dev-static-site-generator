from textnode import TextNode, TextType
import re

def extract_markdown_images(text):
    alt_matches = re.findall(r"!\[(.*?)\]", text)
    src_matches = re.findall(r"\((.*?)\)", text)
    return (alt_matches[0], src_matches[0])

def extract_markdown_links(text):
    alt_text_matches = re.findall(r"\[(.*?)\]", text)
    url_matches = re.findall(r"\((.*?)\)", text)
    return (alt_text_matches[0], url_matches[0])

def split_nodes_image(nodes):
    node_values = []
    for node in nodes:
        node_values = re.split(r"(!.*?\))", node.text)
    
    new_nodes = []
    for value in node_values:
        if len(value) == 0:
            continue

        if "!" in value:
            data = extract_markdown_images(value)
            new_nodes.append(TextNode(data[0], TextType.IMAGE, data[1]))
        else:
            new_nodes.append(TextNode(value, TextType.TEXT))

    return new_nodes

def split_nodes_link(nodes):
    node_values = []
    for node in nodes:
        node_values = re.split(r"(\[.*?\))", node.text)
    new_nodes = []
    for value in node_values:
        if len(value) == 0:
            continue

        if "[" in value:
            data = extract_markdown_links(value)
            new_nodes.append(TextNode(data[0], TextType.LINK, data[1]))
        else:
            new_nodes.append(TextNode(value, TextType.TEXT))
            
    return new_nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    old_nodes_copy = old_nodes.copy()
    new_nodes = []
    #for each node
    for node in old_nodes_copy:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            remaining_text = node.text
            while delimiter in remaining_text:
                start_index = remaining_text.find(delimiter)
            
                if start_index == -1:
                    break
                
                if start_index > 0:
                    new_nodes.append(TextNode(remaining_text[:start_index], TextType.TEXT))
                
                remaining_after_open_delim = remaining_text[start_index + len(delimiter):]
                closing_delim = remaining_after_open_delim.find(delimiter)

                if closing_delim == -1:
                    raise Exception("Improper markdown syntax")

                if closing_delim > -1:
                    new_nodes.append(TextNode(remaining_after_open_delim[:closing_delim], text_type))

                remaining_text = remaining_after_open_delim[closing_delim + len(delimiter):]
            
            if len(remaining_text) > 0:
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes

if __name__ == "__main__":
    ...
