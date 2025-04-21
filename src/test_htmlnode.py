import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


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


class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),
                         "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_nested_parent_nodes(self):
        node = ParentNode("div", [
            LeafNode("h1", "Title"),
            ParentNode("section", [
                LeafNode("p", "First paragraph."),
                LeafNode("p", "Second paragraph.")
            ])
        ])
        expected = "<div><h1>Title</h1><section><p>First paragraph.</p><p>Second paragraph.</p></section></div>"
        self.assertEqual(node.to_html(), expected)


if __name__ == "__main__":
    unittest.main()
