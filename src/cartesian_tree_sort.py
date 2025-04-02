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
    
    # Initialize the root as the first element
    root = Node(arr[0])
    
    # Stack to maintain the tree structure
    stack = [root]
    
    # Iterate through the rest of the array
    for value in arr[1:]:
        # Create new node for current value
        current = Node(value)
        
        # Find the right-most node smaller than current value
        while stack and stack[-1].value < value:
            # This node becomes left child of current node
            current.left = stack.pop()
        
        # If stack is not empty, current becomes right child of top element
        if stack:
            stack[-1].right = current
        
        # Push current node to stack
        stack.append(current)
    
    # Return the root of the Cartesian tree
    return root

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
        
        # Traverse left subtree
        in_order_traversal(node.left)
        
        # Add current node's value to sorted array
        sorted_arr.append(node.value)
        
        # Traverse right subtree
        in_order_traversal(node.right)
    
    # Perform in-order traversal
    in_order_traversal(tree_root)
    
    return sorted_arr