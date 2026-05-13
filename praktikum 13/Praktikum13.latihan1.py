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
    # Jika u dan v berada di set yang berbeda (tidak membentuk cycle)
    if ds.union(u, v):
        mst.append((u, v, weight))
        total_weight += weight

# 6. Cetak Hasil
print("Minimum Spanning Tree (MST):")
for u, v, weight in mst:
    print(f"Edge {u} - {v} dengan bobot {weight}")

print("-" * 30)
print(f"Total bobot MST = {total_weight}")

# 1. Apa perbedaan graph awal dan spanning tree? 
# 2. Mengapa spanning tree tidak boleh memiliki cycle? 
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit? 

# Jawaban Analisis:
# 1. Graph awal memiliki semua edge yang menghubungkan node, sedangkan spanning tree hanya memiliki subset edge yang menghubungkan semua node tanpa membentuk cycle.
# 2. Spanning tree tidak boleh memiliki cycle karena jika ada cycle, maka kita bisa menghapus salah satu edge dalam cycle tersebut tanpa memutuskan koneksi antar node, sehingga tidak efisien dan tidak memenuhi syarat sebagai tree.
# 3. Jumlah edge spanning tree selalu lebih sedikit karena spanning tree hanya memiliki (n-1) edge untuk menghubungkan n node, sedangkan graph awal bisa memiliki lebih banyak edge yang menghubungkan node-node tersebut.
