import textnode as tn

def main():
    tnode_dummy = tn.TextNode("This is some anchor text", tn.TextType.LINK, "https://www.boot.dev")
    print(tnode_dummy)




main()