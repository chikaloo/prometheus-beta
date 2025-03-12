from typing import Dict, List, Set, Optional

class HopcroftKarp:
    """
    Implementation of the Hopcroft-Karp algorithm for maximum matching in bipartite graphs.
    
    The algorithm finds the maximum matching in a bipartite graph efficiently 
    with a time complexity of O(E * sqrt(V)).
    
    Attributes:
        graph (Dict[int, List[int]]): Adjacency list representation of the bipartite graph
        matching (Dict[int, Optional[int]]): Stores the current matching
        dist (Dict[int, int]): Distance array for BFS
    """
    
    def __init__(self, graph: Dict[int, List[int]]):
        """
        Initialize the Hopcroft-Karp algorithm.
        
        Args:
            graph (Dict[int, List[int]]): Adjacency list of the bipartite graph
                where keys are nodes and values are lists of adjacent nodes.
        """
        self.graph = graph
        self.matching: Dict[int, Optional[int]] = {}
        self.dist: Dict[int, int] = {}
    
    def _bfs(self, left_nodes: Set[int]) -> bool:
        """
        Breadth-first search to find augmenting paths.
        
        Args:
            left_nodes (Set[int]): Set of nodes from the left partition
        
        Returns:
            bool: True if an augmenting path exists, False otherwise
        """
        queue = []
        for node in left_nodes:
            # If the node is unmatched
            if self.matching.get(node) is None:
                self.dist[node] = 0
                queue.append(node)
            else:
                # Mark matched nodes as unreachable initially
                self.dist[node] = float('inf')
        
        # Sentinel value to indicate no path found
        self.dist[None] = float('inf')
        
        while queue:
            node = queue.pop(0)
            
            # Skip if a better path exists
            if self.dist[node] < self.dist[None]:
                for neighbor in self.graph.get(node, []):
                    # Check the matched partner of the neighbor
                    partner = self._get_matched_partner(neighbor)
                    
                    # If the partner is not yet assigned a distance
                    if self.dist[partner] == float('inf'):
                        self.dist[partner] = self.dist[node] + 1
                        queue.append(partner)
        
        # Return True if an augmenting path exists
        return self.dist[None] != float('inf')
    
    def _dfs(self, node: Optional[int]) -> bool:
        """
        Depth-first search to find augmenting paths.
        
        Args:
            node (Optional[int]): Current node in the search
        
        Returns:
            bool: True if an augmenting path is found, False otherwise
        """
        # If node is None, we've reached an invalid state
        if node is None:
            return True
        
        # Check neighbors
        for neighbor in self.graph.get(node, []):
            partner = self._get_matched_partner(neighbor)
            
            # Check if this is a valid augmenting path
            if (self.dist[partner] == self.dist[node] + 1 and 
                self._dfs(partner)):
                # Update matching
                self.matching[node] = neighbor
                self.matching[neighbor] = node
                return True
        
        # No augmenting path found
        self.dist[node] = float('inf')
        return False
    
    def _get_matched_partner(self, node: int) -> Optional[int]:
        """
        Get the currently matched partner for a node.
        
        Args:
            node (int): Node to find the matched partner for
        
        Returns:
            Optional[int]: Matched partner or None if unmatched
        """
        return self.matching.get(node)
    
    def maximum_matching(self) -> Dict[int, int]:
        """
        Compute the maximum matching in the bipartite graph.
        
        Returns:
            Dict[int, int]: A dictionary of matched node pairs
        """
        # Reset matching
        self.matching.clear()
        
        # Get all left nodes (assuming first keys are left partition)
        left_nodes = set(self.graph.keys())
        
        # Repeatedly find and augment paths
        while self._bfs(left_nodes):
            for node in left_nodes:
                # If node is unmatched, try to find an augmenting path
                if self.matching.get(node) is None:
                    self._dfs(node)
        
        # Return the maximum matching, preferring lower-indexed nodes
        final_matching = {}
        used_right = set()
        used_left = set()
        for left, right in sorted(self.matching.items()):
            if (left < right and 
                right not in used_right and 
                left not in used_left and 
                right in self.graph.get(left, [])):
                final_matching[left] = right
                used_right.add(right)
                used_left.add(left)
        
        return final_matching

def maximum_matching(graph: Dict[int, List[int]]) -> Dict[int, int]:
    """
    Convenience function to compute maximum matching.
    
    Args:
        graph (Dict[int, List[int]]): Adjacency list of the bipartite graph
    
    Returns:
        Dict[int, int]: A dictionary of matched node pairs
    """
    matcher = HopcroftKarp(graph)
    return matcher.maximum_matching()