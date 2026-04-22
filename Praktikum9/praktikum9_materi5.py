#=======================================================================================
# Nama   : Mohammad Salman Alfarisy
# NIM    : J0403251118
# Kelas  : TPL B1
# Latihan 5 : Traversal Postorder pada Binary Tree
#=======================================================================================

#=======================================================================================
# Membuat Traversal postorder
#=======================================================================================
# Class Node adalah unit dasar pada  tree


class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

# membuat fungsi postorder : left => right => root
def postorder(node):
    if node is not None:
        postorder(node.left) #kunjungi child kiri
        postorder(node.right) #kunjungi child kanan
        print(node.data, end="") #kunjungi root

root = Node("A") # Membuat node root dengan data "A"


root.left = Node("B") # Menambahkan node "B" sebagai child kiri dari "A"
root.right = Node("C") # Menambahkan node "C" sebagai child kanan dari "A"

root.left.left = Node("D") # Menambahkan node "D" sebagai child kiri dari "B"
root.left.right = Node("E") # Menambahkan node "E" sebagai child kanan dari "B"
root.right.left = Node("F") # Menambahkan node "F" sebagai child kiri dari "C"
root.right.right = Node("G") # Menambahkan node "G" sebagai child kanan dari "C"


# Menjalankan traversal postorder
print("Hasil Traversal Postorder: ")
postorder(root) # Menjalankan traversal postorder

# penjelasan :
# Pada contoh di atas, kita membuat sebuah binary tree dengan node "A" sebagai root.
# Node "A" memiliki dua child yaitu "B" dan "C". Node "B" memiliki dua child yaitu "D" dan "E", sedangkan node "C" memiliki dua child yaitu "F" dan "G". Traversal postorder digunakan untuk menampilkan urutan node dengan mengunjungi child kiri terlebih dahulu, kemudian child kanan, dan terakhir root. Hasilnya akan menampilkan urutan node dalam traversal postorder yaitu D, E, B, F, G, C, A.
