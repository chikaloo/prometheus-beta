import pytest
from src.bipartite_graph import is_bipartite

def test_simple_bipartite_graph():
    """Test a simple bipartite graph"""
    graph = [
        [1, 3],    # vertex 0 connected to 1 and 3
        [0, 2],    # vertex 1 connected to 0 and 2
        [1, 3],    # vertex 2 connected to 1 and 3
        [0, 2]     # vertex 3 connected to 0 and 2
    ]
    assert is_bipartite(graph) == True

def test_non_bipartite_graph():
    """Test a graph that is not bipartite"""
    graph = [
        [1, 2, 3],  # vertex 0 connected to 1, 2, and 3
        [0, 2],     # vertex 1 connected to 0 and 2
        [0, 1, 3],  # vertex 2 connected to 0, 1, and 3
        [0, 2]      # vertex 3 connected to 0 and 2
    ]
    assert is_bipartite(graph) == False

def test_empty_graph_raises_error():
    """Test that empty graph raises a ValueError"""
    with pytest.raises(ValueError):
        is_bipartite([])

def test_single_vertex_graph():
    """Test a graph with a single vertex"""
    graph = [[]]
    assert is_bipartite(graph) == True

def test_disconnected_bipartite_graph():
    """Test a graph with multiple disconnected bipartite components"""
    graph = [
        [1],       # first component: 0-1
        [0],
        [3],       # second component: 2-3
        [2]
    ]
    assert is_bipartite(graph) == True

def test_disconnected_non_bipartite_graph():
    """Test a graph with multiple disconnected components, some non-bipartite"""
    graph = [
        [1, 2],    # first component: not bipartite
        [0, 2],
        [0, 1],
        [4, 5],    # second component: bipartite
        [3, 5],
        [3, 4]
    ]
    assert is_bipartite(graph) == False