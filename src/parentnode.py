from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("No Tag")
        if  isinstance(self.children, list) == False:
            raise ValueError("No Children")
        children_str = str()
        for child in self.children:
            children_str += child.to_html()

        return f"<{self.tag}>{children_str}</{self.tag}>"
        