import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_empty(self):
        # Test case: Node with no props
        node_no_props = HTMLNode(tag="p", value="Test")
        self.assertEqual(node_no_props.props_to_html(), "")

        # Test case: Node with empty props
        node_none_props = HTMLNode(tag="p", value="Test", props=None)
        self.assertEqual(node_none_props.props_to_html(), "")

    def test_props_to_html_single(self):
        # Test case: Node with a single prop

        node_single_prop = HTMLNode(tag="p", value="Test", props={
                                    "href": "https://example.com"})
        expected = ' href="https://example.com"'
        self.assertEqual(node_single_prop.props_to_html(), expected)

    def test_props_to_html_multiple(self):
        node_multiple_props = HTMLNode(tag="p", value="Test", props={
                                       "href": "https://example.com", "src": "image.jpg"})
        expected = ' href="https://example.com" src="image.jpg"'
        self.assertEqual(node_multiple_props.props_to_html(), expected)

    def test_values(self): 
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

if __name__ == "__main__":
    unittest.main()