# ==========================================================
# Nama : Mohammad Salman Alfarisy
# NIM : J0403251118
# Kelas : TPL B1
# Praktikum 13 Graph III: Minimum Spanning Tree (MST)
# Implementasi Algoritma Kruskal (Minimum Spanning Tree)
# ==========================================================

class DisjointSet:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        
    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False

# 1. Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# 2. Ambil semua node unik
nodes = set()
for _, u, v in edges:
    nodes.add(u)
    nodes.add(v)

# 3. Urutkan edge berdasarkan bobot terkecil
edges.sort()

# 4. Inisialisasi struktur data
ds = DisjointSet(nodes)
mst = []
total_weight = 0

# 5. Iterasi melalui edge yang sudah terurut
for weight, u, v in edges:
    if ds.union(u, v):
        mst.append((u, v, weight))
        total_weight += weight

# 6. Cetak Hasil
print("Minimum Spanning Tree (MST) - Algoritma Kruskal:")
for u, v, weight in mst:
    print(f"Edge {u} - {v} dengan bobot {weight}")

print("-" * 30)
print(f"Total bobot MST = {total_weight}")

# ==========================================================
# JAWABAN ANALISIS:
# 1. Edge mana yang dipilih pertama kali? Edge C-D dengan bobot 1.
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu? Karena Kruskal 
#    adalah algoritma greedy yang bertujuan meminimalkan total biaya dengan 
#    mengambil bobot terkecil secara global terlebih dahulu.
# 3. Berapa total bobot MST yang dihasilkan? Total bobotnya adalah 6.
# 4. Mengapa edge tertentu tidak dipilih? Karena edge tersebut (seperti A-B atau A-D) 
#    akan membentuk cycle karena node-node tersebut sudah terhubung melalui 
#    jalur lain dalam MST.
# ==========================================================