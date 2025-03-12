import pytest
from src.dinic_max_flow import DinicMaxFlow

def test_basic_max_flow():
    """Test a simple graph with a known max flow."""
    graph = {
        0: {1: 10, 2: 10},
        1: {2: 2, 3: 4, 4: 8},
        2: {4: 9},
        3: {5: 10},
        4: {3: 6, 5: 10},
        5: {}
    }
    dinic = DinicMaxFlow(graph)
    assert dinic.max_flow(0, 5) == 19

def test_single_path_flow():
    """Test a graph with a single path."""
    graph = {
        0: {1: 5},
        1: {2: 5},
        2: {}
    }
    dinic = DinicMaxFlow(graph)
    assert dinic.max_flow(0, 2) == 5

def test_multiple_paths():
    """Test a graph with multiple possible paths."""
    graph = {
        0: {1: 10, 2: 10},
        1: {2: 2, 3: 4, 4: 8},
        2: {4: 9},
        3: {5: 10},
        4: {3: 6, 5: 10},
        5: {}
    }
    dinic = DinicMaxFlow(graph)
    assert dinic.max_flow(0, 5) == 19

def test_no_flow_graph():
    """Test a graph with zero max flow."""
    graph = {
        0: {},
        1: {}
    }
    dinic = DinicMaxFlow(graph)
    assert dinic.max_flow(0, 1) == 0

def test_source_equals_sink():
    """Verify behavior when source and sink are the same."""
    graph = {
        0: {1: 10},
        1: {}
    }
    dinic = DinicMaxFlow(graph)
    assert dinic.max_flow(0, 0) == 0

def test_invalid_nodes():
    """Test handling of invalid source or sink nodes."""
    graph = {
        0: {1: 10},
        1: {}
    }
    dinic = DinicMaxFlow(graph)
    
    with pytest.raises(ValueError, match="Source or sink node not in graph"):
        dinic.max_flow(2, 0)
    
    with pytest.raises(ValueError, match="Source or sink node not in graph"):
        dinic.max_flow(0, 2)

def test_complex_multi_path_flow():
    """Test a more complex graph with multiple paths."""
    graph = {
        0: {1: 3, 2: 3},
        1: {2: 1, 3: 4},
        2: {3: 2, 4: 2},
        3: {4: 1, 5: 3},
        4: {5: 4},
        5: {}
    }
    dinic = DinicMaxFlow(graph)
    assert dinic.max_flow(0, 5) == 4