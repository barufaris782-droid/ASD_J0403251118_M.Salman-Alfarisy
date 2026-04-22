#=======================================================================================
# Nama   : Mohammad Salman Alfarisy
# NIM    : J0403251118
# Kelas  : TPL B1
# Latihan 3 : Traversal inorder pada Binary Tree
#=======================================================================================

#=======================================================================================
# Membuat Traversal inorder
#=======================================================================================
# Class Node adalah unit dasar pada  tree
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

# membuat fungsi inorder : left => root => right
def inorder(node):
    if node is not None:
        inorder(node.left) #kunjungi child kiri
        print(node.data, end="") #kunjungi root
        inorder(node.right) #kunjungi child kanan

root = Node("A") # Membuat node root dengan data "A"

# Membuat child level 1
root.left = Node("B") # Menambahkan node "B" sebagai child kiri dari "A"
root.right = Node("C") # Menambahkan node "C" sebagai child kanan dari "A"

# Membuat child level 2
root.left.left = Node("D") # Menambahkan node "D" sebagai child kiri dari "B"
root.left.right = Node("E") # Menambahkan node "E" sebagai child kanan dari "B"

# Menjalankan traversal inorder
print("Hasil Traversal Inorder: ") # Menjalankan traversal inorder
inorder(root) # Menjalankan traversal inorder

# penjelasan :
# Pada contoh di atas, kita membuat sebuah binary tree dengan node "A" sebagai root. Node "A" memiliki dua child yaitu "B" dan "C". Node "B" memiliki dua child yaitu "D" dan "E", sedangkan node "C" tidak memiliki child. Traversal inorder digunakan untuk menampilkan urutan node dengan mengunjungi child kiri terlebih dahulu, kemudian root, dan terakhir child kanan. Hasilnya akan menampilkan urutan node dalam traversal inorder yaitu D, B, E, A, C.