

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props == None:
            return
        formatted_string = str()
        for prop in self.props:
            formatted_string += f" {prop}=\"{self.props[prop]}\""
        return formatted_string
    
    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"

