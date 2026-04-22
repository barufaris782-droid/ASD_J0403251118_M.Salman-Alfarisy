#=======================================================================================
# Nama   : Mohammad Salman Alfarisy
# NIM    : J0403251118
# Kelas  : TPL B1
# Latihan 4 : Traversal Preorder pada Binary Tree
#=======================================================================================

#=======================================================================================
# Membuat Traversal preorder
#=======================================================================================
# Class Node adalah unit dasar pada  tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

# membuat fungsi preorder : root => left => right
def preorder(node):
    if node is not None:
        print(node.data, end="") #kunjungi root
        preorder(node.left) #kunjungi child kiri
        preorder(node.right) #kunjungi child kanan

root = Node("A") # Membuat node root dengan data "A"

# Membuat child level 1
root.left = Node("B") # Menambahkan node "B" sebagai child kiri dari "A"
root.right = Node("C") # Menambahkan node "C" sebagai child kanan dari "A"

# Membuat child level 2
root.left.left = Node("D") # Menambahkan node "D" sebagai child kiri dari "B"
root.left.right = Node("E") # Menambahkan node "E" sebagai child kanan dari "B"

# Menjalankan traversal preorder
print("Hasil Traversal Preorder: ") # Menjalankan traversal preorder
preorder(root) # Menjalankan traversal preorder

# penjelasan :
# Pada contoh di atas, kita membuat sebuah binary tree dengan node "A" sebagai root. Node "A" memiliki dua child yaitu "B" dan "C". Node "B" memiliki dua child yaitu "D" dan "E", sedangkan node "C" tidak memiliki child. Traversal preorder digunakan untuk menampilkan urutan node dengan mengunjungi root terlebih dahulu, kemudian child kiri, dan terakhir child kanan. Hasilnya akan menampilkan urutan node dalam traversal preorder yaitu A, B, D, E, C.