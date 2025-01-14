import unittest
from converter import text_node_to_html_node
from htmlnode import LeafNode
from textnode import TextNode, TextType

class TestConverter(unittest.TestCase):
    def test_text_node_to_html_node_normal(self):
        text_node = TextNode("test text", TextType.NORMAL, None)
        converted_node = LeafNode(None, "test text", None)
        self.assertEqual(text_node_to_html_node(text_node), converted_node)

    def test_text_node_to_html_node_bold(self):
        text_node = TextNode("test text", TextType.BOLD, None)
        converted_node = LeafNode("b", "test text", None)
        self.assertEqual(text_node_to_html_node(text_node), converted_node)

    def test_text_node_to_html_node_italic(self):
        text_node = TextNode("test text", TextType.ITALIC, None)
        converted_node = LeafNode("i", "test text", None)
        self.assertEqual(text_node_to_html_node(text_node), converted_node)

    def test_text_node_to_html_node_code(self):
        text_node = TextNode("test text", TextType.CODE, None)
        converted_node = LeafNode("code", "test text", None)
        self.assertEqual(text_node_to_html_node(text_node), converted_node)

    def test_text_node_to_html_node_link(self):
        text_node = TextNode("test text", TextType.LINK, "www.google.com")
        converted_node = LeafNode("a", "test text", {"href":"www.google.com"})
        self.assertEqual(text_node_to_html_node(text_node), converted_node)

    def test_text_node_to_html_node_image(self):
        text_node = TextNode("test text", TextType.IMAGE, "www.google.com")
        converted_node = LeafNode("img", "", {"src":"www.google.com", "alt": "test text"})
        self.assertEqual(text_node_to_html_node(text_node), converted_node)

if __name__ == "__main__":
    unittest.main()
