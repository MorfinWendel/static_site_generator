class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        prop_string = ""
        if self.props:
            for prop in self.props:
                prop_string += f' {prop}="{self.props[prop]}"'
        return prop_string
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("No tag")
        if not self.children:
            raise ValueError("No children")

        html_children = ""
        for child in self.children:
            html_children += child.to_html()

        html_string = f'<{self.tag}{self.props_to_html()}>{html_children}</{self.tag}>'
        return html_string

    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})" 

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("No value")
        if not self.tag:
            return self.value
        html_string = f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        return html_string

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

