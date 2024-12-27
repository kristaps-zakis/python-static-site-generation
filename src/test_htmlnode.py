import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(props={"href": "https://www.boot.dev", "target": "_blank"}).props_to_html()
        node2 = HTMLNode(props={"href": "https://www.boot.dev", "target": "_blank"}).props_to_html()
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode(props={"href": "https://www.boot.dev", "target": "_blank"}).props_to_html()
        node2 = HTMLNode(props={"href": "https://www.boot.dev", "target": "_self"}).props_to_html()
        self.assertNotEqual(node, node2)

    def test_has_link_eq(self):
        node = HTMLNode(props={"href": "https://www.boot.dev", "target": "_blank"}).props_to_html()
        node2 = HTMLNode(props={"href": "https://www.boot.dev", "target": "_blank"}).props_to_html()
        self.assertEqual(node, node2)

    def test_no_taq_eq(self):
        node = LeafNode("a",  "ppp", props={"href": "https://www.boot.dev", "target": "_blank"}).to_html()
        node2 = LeafNode("a", "ppp", props={"href": "https://www.boot.dev", "target": "_blank"}).to_html()

        self.assertEqual(node, node2)

    # def test_parent_empty_eq(self):
    #     node = ParentNode("div", LeafNode(None, "Normal text").to_html).to_html()
    #     node2 = ParentNode("div", LeafNode(None, "Normal text").to_html()).to_html()
    #     print(node)
    #     self.assertNotEqual(node, node2)

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

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

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()