import pytest
from src.graph_cycle_detection import detect_cycle_in_directed_graph

def test_simple_cycle():
    """Test a simple graph with a cycle"""
    graph = {
        0: [1],
        1: [2],
        2: [0]
    }
    assert detect_cycle_in_directed_graph(graph) == True

def test_no_cycle():
    """Test a graph without a cycle"""
    graph = {
        0: [1],
        1: [2],
        2: [3],
        3: []
    }
    assert detect_cycle_in_directed_graph(graph) == False

def test_self_loop():
    """Test a graph with a self-loop"""
    graph = {
        0: [0]
    }
    assert detect_cycle_in_directed_graph(graph) == True

def test_complex_graph_with_cycle():
    """Test a more complex graph with a cycle"""
    graph = {
        0: [1, 2],
        1: [2],
        2: [3],
        3: [1]
    }
    assert detect_cycle_in_directed_graph(graph) == True

def test_complex_graph_without_cycle():
    """Test a more complex graph without a cycle"""
    graph = {
        0: [1, 2],
        1: [3],
        2: [4],
        3: [4],
        4: []
    }
    assert detect_cycle_in_directed_graph(graph) == False

def test_empty_graph():
    """Test that an empty graph raises a ValueError"""
    with pytest.raises(ValueError):
        detect_cycle_in_directed_graph({})

def test_single_node_graph():
    """Test a graph with a single node without edges"""
    graph = {0: []}
    assert detect_cycle_in_directed_graph(graph) == False

def test_disconnected_graph_with_cycle():
    """Test a disconnected graph with a cycle"""
    graph = {
        0: [1],
        1: [0],
        2: [3],
        3: [4],
        4: [2]
    }
    assert detect_cycle_in_directed_graph(graph) == True