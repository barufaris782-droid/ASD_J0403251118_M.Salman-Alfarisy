#==============================
# Nama : Mohammad Salman Alfarisy
# NIM : J0403521118
# Kelas : B1
# Latihan 1 :Implementasi node pada binary tree
#==============================

class node:
    def __init__(self, data):
        self.data = data           # Menyimpan nilai utama pada node
        self.left = None           # Menyiapkan slot kosong untuk anak kiri
        self.right = None          # Menyiapkan slot kosong untuk anak kanan

# --- MEMBUAT STRUKTUR POHON ---
root = node("A")                   # Membuat akar utama (level 0) dengan data "A"

root.left = node("B")              # Menghubungkan node "B" ke cabang kiri "A"
root.right = node("C")             # Menghubungkan node "C" ke cabang kanan "A"

root.left.left = node("D")         # Menghubungkan node "D" ke cabang kiri "B"
root.left.right = node("E")        # Menghubungkan node "E" ke cabang kanan "B"
root.right.left = node("F")        # Menghubungkan node "F" ke cabang kiri "C"
root.right.right = node("G")       # Menghubungkan node "G" ke cabang kanan "C"

# --- MENAMPILKAN DATA (OUTPUT) ---
print(root.data)                   # Output: A (Data di pusat/root)
print(root.left.data)              # Output: B (Data di kiri root)
print(root.right.data)             # Output: C (Data di kanan root)

print(root.left.left.data)         # Output: D (Data di kiri dari B)
print(root.left.right.data)        # Output: E (Data di kanan dari B)
print(root.right.left.data)        # Output: F (Data di kiri dari C)
print(root.right.right.data)       # Output: G (Data di kanan dari C)

# Penjelasan:
# Pada contoh di atas, kita membuat sebuah binary tree dengan node "A" sebagai root. Node "A" memiliki dua child yaitu "B" dan "C". Node "B" memiliki dua child yaitu "D" dan "E", sedangkan node "C" memiliki dua child yaitu "F" dan "G". Struktur ini membentuk sebuah pohon biner yang terdiri dari 7 node. Setiap node menyimpan data dan memiliki referensi ke anak kiri dan anak kanan, yang memungkinkan kita untuk mengakses semua node dalam pohon tersebut.