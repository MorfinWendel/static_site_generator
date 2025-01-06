import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

example_props = {
    "href": "https://www.google.com", 
    "target": "_blank",
}


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode("p", "Test value", None, example_props)
        prop_string = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), prop_string)

    def test_props_none(self):
        node = HTMLNode("p", "Test value", None, None)
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode("p", "Test value", None, example_props)
        to_compare = f"HTMLNode(p, Test value, children: None, {node.props})" 
        self.assertEqual(repr(node), to_compare)

class TestParentNode(unittest.TestCase):
    def test_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        to_compare = "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), to_compare)

    def test_nested_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "Italic text"),
                        LeafNode(None, "Normal text"),
                    ]),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        to_compare = "<p><b>Bold text</b><p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p><i>Italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), to_compare)
    
    def test_no_children(self):
        node = ParentNode("p", None, None)
        self.assertRaises(ValueError, node.to_html)

    def test_no_tag(self):
        node = ParentNode(None, LeafNode("b", "Bold text"), None)
        self.assertRaises(ValueError, node.to_html)

class TestLeafNode(unittest.TestCase):
    def test_repr(self):
        node = LeafNode("p", "Test value", example_props)
        to_compare = f"LeafNode(p, Test value, {example_props})" 
        self.assertEqual(repr(node), to_compare)

    def test_html(self):
        node = LeafNode("a", "Test value", example_props)
        to_compare = '<a href="https://www.google.com" target="_blank">Test value</a>'
        self.assertEqual(node.to_html(), to_compare)

if __name__ == "__main__":
    unittest.main()
