class Node:
    def __init__(self, key, data):
        # The node's key
        self.key = key
        # The node's data
        self.data = data
        # The node's left child
        self.left = None
        # The node's right child
        self.right = None

    def __str__(self):
        "String representation."
        return self.ToString()

    def ToString(self):
        "String representation."
        return "Key: {0}\nValue: {1}".format(self.key, self.data)