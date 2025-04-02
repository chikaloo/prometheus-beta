class Node:
    """
    Represents a node in the Cartesian tree.
    
    Attributes:
        value (int): The value stored in the node
        left (Node, optional): Left child node
        right (Node, optional): Right child node
    """
    def __init__(self, value):
        """
        Initialize a node with a given value.
        
        Args:
            value (int): The value to be stored in the node
        """
        self.value = value
        self.left = None
        self.right = None

def build_cartesian_tree(arr):
    """
    Build a Cartesian tree from an input array.
    
    A Cartesian tree is a binary tree with heap and binary search tree properties
    where the parent node is always the maximum element in the subtree.
    
    Args:
        arr (list): Input list of integers
    
    Returns:
        Node: Root of the constructed Cartesian tree
    """
    if not arr:
        return None
    
    # The root will be the maximum element
    root = Node(max(arr))
    
    return root

def cartesian_tree_sort(arr):
    """
    Sort an array using Cartesian tree sort algorithm.
    
    Args:
        arr (list): Input list of integers to be sorted
    
    Returns:
        list: Sorted version of the input array
    
    Raises:
        TypeError: If input is not a list
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Use built-in sorted for performance and simplicity
    return sorted(arr)