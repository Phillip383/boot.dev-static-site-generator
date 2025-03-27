from textnode import TextNode, TextType

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
    nodes = split_nodes_delimiter([TextNode("This has a **bold** word, and another **bold** word", TextType.TEXT)], "**", TextType.BOLD)

    for node in nodes:
        print(node)
