class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert_rec(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert_rec(root.right, key)

    def search(self, key):
        return self._search_rec(self.root, key)

    def _search_rec(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self._search_rec(root.left, key)
        return self._search_rec(root.right, key)

    def find_min(self):
        return self._find_min_rec(self.root)

    def _find_min_rec(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current.val

    def find_max(self):
        return self._find_max_rec(self.root)

    def _find_max_rec(self, root):
        current = root
        while current.right is not None:
            current = current.right
        return current.val

input_values = [20, 9, 25, 5, 12, 15, 30]
bst = BinarySearchTree()

for value in input_values:
    bst.insert(value)


print("Minimum value:", bst.find_min())
print("Maximum value:", bst.find_max())


search_value_1 = 12
search_value_2 = 18
print(f"Search {search_value_1}: {'Found' if bst.search(search_value_1) else 'Not found'}")
print(f"Search {search_value_2}: {'Found' if bst.search(search_value_2) else 'Not found'}")