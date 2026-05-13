# ==========================================================
# Nama : Mohammad Salman Alfarisy
# NIM : J0403251118
# Kelas : TPL B1
# Praktikum 13 Graph III: Minimum Spanning Tree (MST)
# Studi Kasus: Jaringan Kabel Antar Gedung
# ==========================================================

# Data hubungan gedung (Weighted Graph) [cite: 506-511]
# GedungA-GedungB=4, GedungA-GedungC=2, GedungB-GedungD=3, GedungC-GedungD=1, GedungA-GedungD=5
edges_gedung = [
    (1, 'GedungC', 'GedungD'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (4, 'GedungA', 'GedungB'),
    (5, 'GedungA', 'GedungD')
]

edges_gedung.sort()
connected_nodes = set()
mst_kabel = []
total_biaya = 0

# Menggunakan logika Kruskal sederhana untuk efisiensi biaya
for biaya, u, v in edges_gedung:
    if u not in connected_nodes or v not in connected_nodes:
        mst_kabel.append((u, v, biaya))
        total_biaya += biaya
        connected_nodes.add(u)
        connected_nodes.add(v)

print("Rancangan Jaringan Kabel Minimum Biaya:")
for u, v, biaya in mst_kabel:
    print(f"{u} terhubung ke {v} dengan biaya {biaya}")

print("-" * 30)
print(f"Total Biaya Minimum = {total_biaya}")

# ==========================================================
# JAWABAN ANALISIS:
# 1. Algoritma apa yang digunakan? Algoritma Kruskal.
# 2. Edge mana saja yang dipilih? GedungC-GedungD (1), GedungA-GedungC (2), 
#    dan GedungB-GedungD (3).
# 3. Berapa total biaya minimum? 6.
# 4. Mengapa MST cocok digunakan pada kasus ini? Karena tujuannya adalah 
#    menghubungkan seluruh gedung (node) agar saling terkoneksi dengan 
#    biaya (bobot) total yang paling minimal tanpa adanya kabel yang mubazir.
# ==========================================================