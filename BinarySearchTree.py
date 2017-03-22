from Node import Node

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    # Returns the number of nodes in the BST.
    def length(self):
        return self.size

    # Determines if the BST contains the given key.
    def has_key(self, key):
        return self.bstSearch(self.root, key) is not None

    # Returns the value associated with the key.
    def valueOf(self, key):
        node = self.bstSearch(self.root, key)
        # The search process starts from the root.
        assert node is not None, "Invalid key."     # if node=None, the function stops and message is printed.
        return node.value                            
    
    # This method recursively searches the tree for a target key.
    #  This method returns the address of node or None when:
    #  (1) the BST is empty    or    (2) target doesn't exist.
    def bstSearch(self, subtree, target):
        if subtree is None:                         # base case
            return None
        elif target < subtree.key:                  # target is left of the subtree root.
            return self.bstSearch(subtree.left, target)
        elif target > subtree.key:                  # target is right of the subtree root.
            return self.bstSearch(subtree.right, target)
        else:                                       # base case
            return subtree

    # This method returns the address of the node  containing the minimum key.
    def bstMinimum(self, subtree):
        if subtree is None:
            return None         # This method returns None when the tree is empty.
        else:   # When the tree is not empty.
            if subtree.left is None:
                return subtree
            else:
                return self.bstMinimum(subtree.left)

    # Adds a new entry to BST or replaces the value of an existing key.
    def add(self, key, value):
        node = self.bstSearch(self.root, key)          # Find the node containing the key, if it exists.
        if node is not None:                # If the key is already in the tree, update its value.
            node.value = value
            return False
        else:                              # Otherwise, add a new entry.
            self.root = self.bstInsert(self.root, key, value)  # Starting from the root.
            self.size += 1
        return True

    # This method inserts a new item, recursively.
    def bstInsert(self, subtree, key, value):
        if subtree is None:
            subtree = Node(key, value)
        elif key < subtree.key:
            subtree.left = self.bstInsert(subtree.left, key, value)
        elif key > subtree.key :
            subtree.right = self.bstInsert(subtree.right, key, value)
        return subtree

    # Removes the node associated with the given key.
    def remove(self, key):
        node = self.bstSearch(self.root, key)       # The search process starts from the root.
        assert node is not None, "Invalid  key."    # if node=None, the function stops and message is printed.
        self.root = self.bstRemove(self.root, key)  # The key exists
        self.size -= 1

    # This method removes an existing item recursively.
    def bstRemove(self, subtree, target):
        # Search for the item in the tree.
        if target < subtree.key:
            subtree.left = self.bstRemove(subtree.left, target)
            return subtree
        elif target > subtree.key:
            subtree.right = self.bstRemove(subtree.right, target)
            return subtree       # We found the node containing the item.
        else:
            if subtree.left is None and subtree.right is None:
                return None
            elif subtree.left is None or subtree.right is None:
                if subtree.left is not None:
                    return subtree.left
                else:
                    return subtree.right
            else:
                successor = self.bstMinimum(subtree.right)
                subtree.key = successor.key
                subtree.value = successor.value
                subtree.right = self.bstRemove(subtree.right, successor.key)
                return subtree
