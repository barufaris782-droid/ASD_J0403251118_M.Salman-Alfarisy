#==============================
# Nama : Mohammad Salman Alfarisy
# NIM : J0403521118
# Kelas : B1
# Latihan 1 :Implementasi node pada binary tree
#==============================

class node :
    def __init__(self, data):
        self.data = data #menyimpan data pada node
        self.left = None #child kiri
        self.right = None #child kanan

#contoh penggunaan
root = node("A") #membuat node root dengan data "A"

#menampilkan isi node
print("Data pada root node: ", root.data)
print("Data kiri root node: ", root.left)
print("Data kanan root node: ", root.right)

# penjelasan :
# Pada contoh di atas, kita membuat sebuah class node yang memiliki atribut data, left, dan right. Atribut data digunakan untuk menyimpan nilai pada node, sedangkan left dan right digunakan untuk menyimpan referensi ke anak kiri dan anak kanan dari node tersebut. Kemudian kita membuat sebuah node root dengan data "A" dan menampilkan isi dari node tersebut. Hasilnya akan menunjukkan data pada root node yaitu "A", serta data kiri dan kanan yang masih bernilai None karena belum ada child yang ditambahkan.