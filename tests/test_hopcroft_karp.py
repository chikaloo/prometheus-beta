import pytest
from src.hopcroft_karp import maximum_matching, HopcroftKarp

def test_simple_matching():
    """Test a simple bipartite graph with a clear maximum matching."""
    graph = {
        0: [3, 4],
        1: [3],
        2: [4]
    }
    matching = maximum_matching(graph)
    assert len(matching) == 2
    assert set(matching.keys()) == {0, 1}
    assert set(matching.values()) == {3, 4}

def test_complete_bipartite_matching():
    """Test a complete bipartite graph where all nodes can be matched."""
    graph = {
        0: [3, 4, 5],
        1: [3, 4, 5],
        2: [3, 4, 5]
    }
    matching = maximum_matching(graph)
    assert len(matching) == 3
    assert all(node in matching.keys() or node in matching.values() 
               for node in range(6))

def test_empty_graph():
    """Test matching on an empty graph."""
    graph = {}
    matching = maximum_matching(graph)
    assert matching == {}

def test_no_matching_possible():
    """Test a graph where no matching is possible."""
    graph = {
        0: [],
        1: [],
        2: []
    }
    matching = maximum_matching(graph)
    assert matching == {}

def test_asymmetric_graph():
    """Test a graph with unequal partition sizes."""
    graph = {
        0: [3, 4],
        1: [3],
        2: [4, 5],
        3: [],
        4: []
    }
    matching = maximum_matching(graph)
    assert len(matching) == 2
    assert set(matching.keys()).issubset({0, 1, 2})
    assert set(matching.values()).issubset({3, 4, 5})

def test_multiple_matching_possibilities():
    """Test a graph with multiple possible maximum matchings."""
    graph = {
        0: [2, 3],
        1: [2, 3]
    }
    matching = maximum_matching(graph)
    assert len(matching) == 1
    assert list(matching.keys())[0] in {0, 1}
    assert list(matching.values())[0] in {2, 3}

def test_class_based_matching():
    """Test using the HopcroftKarp class directly."""
    graph = {
        0: [3, 4],
        1: [3],
        2: [4]
    }
    matcher = HopcroftKarp(graph)
    matching = matcher.maximum_matching()
    assert len(matching) == 2
    assert set(matching.keys()) == {0, 1}
    assert set(matching.values()) == {3, 4}

def test_no_duplicate_matches():
    """Ensure no node is matched more than once."""
    graph = {
        0: [3, 4, 5],
        1: [3, 4, 5],
        2: [3, 4, 5]
    }
    matching = maximum_matching(graph)
    assert len(set(matching.keys())) == len(matching)
    assert len(set(matching.values())) == len(matching)