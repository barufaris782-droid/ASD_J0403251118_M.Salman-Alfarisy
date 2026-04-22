#=================
# Nama : Mohammad Salman Alfarisy
# NIM : J0403251118
# Kelas : TPL B1
# Latihan 1 : Membuat Binary Search Tree
#=================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None  

# alur fungsi insert pada binary search tree
def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
       root.left = insert(root.left, data)
    elif data > root.data:
       root.right = insert(root.right, data)
    return root

#mengisi data ke dalam binary search tree
root = None
data_list = [10, 5, 15, 3, 7, 12, 18]

for data in data_list:
    root = insert(root, data)

print("Binary Search Tree telah dibuat dengan data:", data_list)

#=================
# Latihan 2 : Traversal inorder pada Binary Search Tree
#=================

# alur fungsi inorder traversal pada binary search tree
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)

print("Traversal inorder pada Binary Search Tree:")
inorder_traversal(root)
print()

# ==================
# Latihan 3: Searching pada Binary Search Tree
# ==================

# alur fungsi search pada binary search tree
def search(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    if key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)

key = 40

if search(root, key):
    print(f"Data {key} ditemukan dalam Binary Search Tree.")
else: 
    print(f"Data {key} tidak ditemukan dalam Binary Search Tree.")