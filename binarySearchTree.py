class BSTNode:
    """
    Implentation for the node of a Binary Search Tree
    
    key: the key of the node
    value: the value of the node
    parent: pointer to the parent node
    left: pointer to the left child
    right: pointer to the right child
    
    return: null
    """ 
    def __init__(self, key, value, parent=None, left=None, right=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

class BST:
    """
    Implentation of a Binary Search Tree
    """
    def __init__(self):
        self.root = None
        
    def find_recursive(self, node, key):
        """
        Recursively search for the key from the node
        
        node: a BST Node
        key: a key value
        return: the node with the key if the key exists, 
                Null if the key is not found
        """
        if None == node or key == node.key:
            return node
        elif key < node.key:
            return self.find_recursive(node.left, key)
        else:
            return self.find_recursive(node.right, key)
    
    def find_iterative(self, node, key):
        """
        Iteratively search for the key from the node
        
        node: a BST Node
        key: a key value
        return: the node with the key if the key exists, 
                Null if the key is not found
        """
        current_node = node
        while current_node:
            if key == current_node.key:
                return current_node
            elif key < current_node.key:
                current_node = current_node.left
            else: 
                current_node = current_node.right
        return None
        
    def search(self, key):
        """
        Find the node with the key
        """
        return self.find_iterative(self.root, key)
        
    def insert(self, key, value):
        """
        Insert the (key, value) to the BST
        
        key: the key to insert
        value: the value to insert
        return: True if insert successfully;
            otherwise return False
        """
        if self.root == None:
            self.root = BSTNode(key, value)
            return True
            
        current_node = self.root
        while current_node:
            if key == current_node.key:
                print "The key does exist!"
                return False
            elif key < current_node.key:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = BSTNode(key, value, current_node)
                    return True
            else:
                if current_node.right:
                    current_node.right = BSTNode(key, value, current_node)
                    return True
                    
    def remove_node(self, node):
        """ 
        Remove a node from the tree. Used to implement delete if the node
        exists in the tree.
        
        node: The node to remove
        return: null
        """
        # the node has two children
        if node.left and node.right: 
            # Find its in-order successor
            successor = node.right
            while successor.left:
                successor = successor.left
            # Copy the node
            node.key = successor.key
            node.value = successor.value
            # Remove the successor
            self.remove_node(successor)
        # the node only has a left child
        elif node.left: 
            self.replace_node(node, node.left)
        # the node only has a right child
        elif node.right:
            self.replace_node(node, None)
        
    def delete(self, key):
        """
        Delete the node with the key
        
        key: a key value
        return: True if the node is deleted successfully; 
                otherwise false
        """
        node = self.search(key)
        if node: 
            self.remove_node(node)
            
    def traverse_in_order(node, callback_function):
        """
        Function to traverse the tree from the node recursively. 
        """
        if node is None:
            return
        traverse_in_order(node.left, callback_function)
        callback_function(node)
        traverse_in_order(node.right, callback_function)
        
    def sort_by_BST(values):
        """
        Sort the given list of values using BST 
        
        values: a list of values
        return: a sorted list
        """
        result = []
        bst = BST()
        # Insert the values into the BST
        for v in values:
            bst.insert(v, 0)
        # Traverse the bst with the callback function that inserts the key of each node into result
        traverse_in_order(bst.root, lambda n: result.append(n.key))
        return result
            