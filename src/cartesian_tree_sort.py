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
    
    # Create nodes for each element
    nodes = [Node(val) for val in arr]
    
    for i in range(1, len(nodes)):
        # Find the right ancestor where new node becomes a right child
        j = i - 1
        while j >= 0 and nodes[j].value <= nodes[i].value:
            j -= 1
        
        # If found a valid ancestor
        if j >= 0:
            # Set current node as right child of this ancestor
            nodes[j].right = nodes[i]
        
        # Set parent for the current node if one exists
        if i > 0:
            parent = j
            nodes[i].left = parent >= 0 and nodes[parent] or None
    
    # Return the root node (last inserted node if no root is present)
    return nodes[len(nodes)-1]

def cartesian_tree_sort(arr):
    """
    Sort an array using Cartesian tree sort algorithm.
    
    Cartesian tree sort works by:
    1. Building a Cartesian tree from the input array
    2. Performing an in-order traversal of the tree
    
    Args:
        arr (list): Input list of integers to be sorted
    
    Returns:
        list: Sorted version of the input array
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-comparable elements
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element list
    if len(arr) <= 1:
        return arr.copy()
    
    # Build Cartesian tree
    tree_root = build_cartesian_tree(arr)
    
    # List to store sorted elements
    sorted_arr = []
    
    def in_order_traversal(node):
        """
        Perform in-order traversal to extract sorted elements.
        
        Args:
            node (Node): Current node in the Cartesian tree
        """
        if not node:
            return
        
        # Traverse left subtree first
        if node.left:
            in_order_traversal(node.left)
        
        # Add current node's value to sorted array
        sorted_arr.append(node.value)
        
        # Traverse right subtree last
        if node.right:
            in_order_traversal(node.right)
    
    # Perform in-order traversal
    in_order_traversal(tree_root)
    
    return sorted_arr