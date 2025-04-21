import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node_paragraph = LeafNode("p", "Hello, world!")
        self.assertEqual(node_paragraph.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_with_props(self):
        node_with_href = LeafNode(
            "a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node_with_href.to_html(),
                         '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_none_tag(self):
        node_no_tag = LeafNode(None, "Just text")
        self.assertEqual(node_no_tag.to_html(), "Just text")

    def test_leaf_to_html_raises_value_error_when_value_is_none(self):
        with self.assertRaises(ValueError):
            LeafNode("div", None)

    def test_leaf_to_html_strong(self):
        node_strong = LeafNode("strong", "Bold text")
        self.assertEqual(node_strong.to_html(), "<strong>Bold text</strong>")

    def test_leaf_to_html_span_with_class(self):
        node_with_class = LeafNode("span", "Highlight", {"class": "highlight"})
        self.assertEqual(node_with_class.to_html(),
                         '<span class="highlight">Highlight</span>')
