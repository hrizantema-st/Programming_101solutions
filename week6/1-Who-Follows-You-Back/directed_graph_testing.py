import unittest
from directed_graph import DirectedGraph


class DirectedGraphTestClass(unittest.TestCase):

    def setUp(self):
        self.test_graph_info = {"a": ["b", "c"], "b": ["c"], "c": ["d"], "d": []}
        self.test_graph = DirectedGraph()
        self.test_graph.graph = self.test_graph_info

    def test_init(self):
        self.assertTrue(isinstance(self.test_graph, DirectedGraph))

    def test_add_node(self):
        self.test_graph.add_node("p")
        self.assertTrue("p" in self.test_graph.graph.keys())

    def test_add_edge(self):
        self.test_graph.add_edge("c", "a")
        self.assertTrue("a" in self.test_graph.graph["c"])

    def test_get_neighbours_for(self):
        self.assertEqual(self.test_graph.get_neighbours_for("a"), ["b", "c"])

    def test_path_between(self):
        self.assertTrue(self.test_graph.path_between("b", "c"))
        self.assertFalse(self.test_graph.path_between("c", "b"))
        self.assertTrue(self.test_graph.path_between("a", "d"))



if __name__ == '__main__':
    unittest.main()
