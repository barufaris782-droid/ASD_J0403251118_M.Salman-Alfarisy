#=======================================================================================
# Nama   : Mohammad Salman Alfarisy
# NIM    : J0403251118
# Kelas  : TPL B1
# Latihan 6 : struktur organisasi perusahaan
#=======================================================================================

#=======================================================================================
# Membuat struktur organisasi perusahaan
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


root = Node("Direktur") # Membuat node root dengan data "Direktur"

#child level 1
root.left = Node("Manajer A") # Menambahkan node "Manajer"
root.right = Node("Manajer B") # Menambahkan node "Manajer"

#child level 2
root.left.left = Node("Staff 1") # Menambahkan node " Staff 1"
root.left.right = Node("Staff 2") # Menambahkan node "Staff 2"

root.right.right = Node("Staff 3") # Menambahkan node "Staff 3"

# Menjalankan traversal preorder
print("Struktur Organisasi Perusahaan: ")
preorder(root) # Menjalankan traversal preorder


# penjelasan :
# Pada contoh di atas, kita membuat struktur organisasi perusahaan dengan menggunakan binary tree. Node "Direktur" adalah root dari tree, dan memiliki dua child
# yaitu "Manajer A" dan "Manajer B". "Manajer A" memiliki dua child yaitu "Staff 1" dan "Staff 2", sedangkan "Manajer B" memiliki satu child yaitu "Staff 3". Traversal preorder
# digunakan untuk menampilkan struktur organisasi dengan mengunjungi root terlebih dahulu, kemudian child kiri, dan terakhir child kanan. Hasilnya akan menampilkan urutan posisi dalam struktur organisasi perusahaan.
