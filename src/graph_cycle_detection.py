from typing import Dict, List, Set

def detect_cycle_in_directed_graph(graph: Dict[int, List[int]]) -> bool:
    """
    Detect if a directed graph contains a cycle using depth-first search.
    
    Args:
        graph (Dict[int, List[int]]): Adjacency list representation of the graph.
                                      Keys are nodes, values are lists of adjacent nodes.
    
    Returns:
        bool: True if a cycle is detected, False otherwise.
    
    Raises:
        ValueError: If the graph is empty or not a valid adjacency list.
    
    Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges
    Space Complexity: O(V) for the recursion stack and visited sets
    """
    # Validate input
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    def dfs(node: int, path_set: Set[int], visited: Set[int]) -> bool:
        """
        Depth-first search to detect cycles in the graph.
        
        Args:
            node (int): Current node being explored
            path_set (Set[int]): Set of nodes in the current DFS path
            visited (Set[int]): Set of all visited nodes
        
        Returns:
            bool: True if a cycle is detected, False otherwise
        """
        # Mark the current node as visited and add to current path
        visited.add(node)
        path_set.add(node)
        
        # Explore all neighbors
        for neighbor in graph.get(node, []):
            # If neighbor not visited, recursively check
            if neighbor not in visited:
                if dfs(neighbor, path_set, visited):
                    return True
            # If neighbor is in current path, cycle detected
            elif neighbor in path_set:
                return True
        
        # Remove node from current path
        path_set.remove(node)
        
        return False
    
    # Check for cycles starting from each unvisited node
    visited: Set[int] = set()
    for node in graph:
        if node not in visited:
            path_set: Set[int] = set()
            if dfs(node, path_set, visited):
                return True
    
    return False