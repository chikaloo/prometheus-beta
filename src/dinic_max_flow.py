from typing import List, Dict
from collections import deque

class DinicMaxFlow:
    def __init__(self, graph: Dict[int, Dict[int, int]]):
        """
        Initialize Dinic's algorithm for maximum flow.
        
        :param graph: Adjacency list representation of the graph
                      Format: {node: {neighbor: capacity}}
        """
        self.graph = graph
        self.nodes = set(graph.keys())
        for node in graph:
            self.nodes.update(graph[node].keys())
    
    def _bfs(self, source: int, sink: int) -> Dict[int, int]:
        """
        Perform Breadth-First Search to build level graph.
        
        :param source: Source node
        :param sink: Sink node
        :return: Level of each node or None if sink is unreachable
        """
        level = {node: -1 for node in self.nodes}
        level[source] = 0
        
        queue = deque([source])
        
        while queue:
            current = queue.popleft()
            
            for neighbor, capacity in self.graph[current].items():
                if level[neighbor] == -1 and capacity > 0:
                    level[neighbor] = level[current] + 1
                    queue.append(neighbor)
        
        return level if level[sink] != -1 else None
    
    def _dfs(self, node: int, sink: int, flow: int, level: Dict[int, int], 
             flow_so_far: Dict[tuple, int]) -> int:
        """
        Depth-First Search to find augmenting paths.
        
        :param node: Current node
        :param sink: Sink node
        :param flow: Maximum flow possible
        :param level: Level graph from BFS
        :param flow_so_far: Tracks used capacities
        :return: Augmented flow
        """
        if node == sink:
            return flow
        
        for neighbor, capacity in self.graph[node].items():
            residual_capacity = capacity - flow_so_far.get((node, neighbor), 0)
            
            if (level[neighbor] == level[node] + 1 and 
                residual_capacity > 0):
                
                curr_flow = min(flow, residual_capacity)
                
                temp_flow = self._dfs(neighbor, sink, curr_flow, 
                                      level, flow_so_far)
                
                if temp_flow > 0:
                    flow_so_far[(node, neighbor)] = \
                        flow_so_far.get((node, neighbor), 0) + temp_flow
                    flow_so_far[(neighbor, node)] = \
                        flow_so_far.get((neighbor, node), 0) - temp_flow
                    
                    return temp_flow
        
        return 0
    
    def max_flow(self, source: int, sink: int) -> int:
        """
        Compute the maximum flow from source to sink using Dinic's algorithm.
        
        :param source: Source node
        :param sink: Sink node
        :return: Maximum flow value
        """
        if source not in self.nodes or sink not in self.nodes:
            raise ValueError("Source or sink node not in graph")
        
        if source == sink:
            return 0
        
        max_flow = 0
        flow_so_far = {}
        
        while True:
            # Build level graph
            level = self._bfs(source, sink)
            
            if level is None:
                break
            
            # Find augmenting paths
            while True:
                path_flow = self._dfs(source, sink, float('inf'), 
                                      level, flow_so_far)
                
                if path_flow == 0:
                    break
                
                max_flow += path_flow
        
        return max_flow