
from splitnodes import *

def text_to_textnodes(text):
    nodes = split_nodes_delimiter([TextNode(text, TextType.TEXT)], "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

if __name__ == "__main__":
    nodes = text_to_textnodes("This is _text_ with an **bold** word and some `code` and a [link](https://boot.dev) and a ![image](https://image.png)")
    print("\n")
    print("#####################################################")
    print("This is _text_ with an **bold** word and some `code` and a [link](https://boot.dev) and a ![image](https://image.png)")
    for node in nodes:
        print(node)
