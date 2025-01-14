from htmlnode import LeafNode
from textnode import TextNode, TextType

def text_node_to_html_node(textnode):
    tag = None
    value = None
    props = {}
    match textnode.text_type:
        case TextType.NORMAL:
            value = textnode.text
        case TextType.BOLD:
            tag = "b"
            value = textnode.text
        case TextType.ITALIC:
            tag = "i"
            value = textnode.text
        case TextType.CODE:
            tag = "code"
            value = textnode.text
        case TextType.LINK:
            tag = "a"
            value = textnode.text
            props["href"] = textnode.url
        case TextType.IMAGE:
            tag = "img"
            value = ""
            props["src"] = textnode.url
            props["alt"] = textnode.text
        case _:
            raise ValueError("Incorrect TextType")
    return LeafNode(tag, value, props) 
