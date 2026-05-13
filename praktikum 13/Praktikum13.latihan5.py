# ==========================================================
# Nama : Mohammad Salman Alfarisy
# NIM : J0403251118
# Kelas : TPL B1
# Praktikum 13 Graph III: Minimum Spanning Tree (MST)
# Tugas Mandiri: Kasus Jaringan Komputer
# ==========================================================

# Representasi weighted graph Kasus 2 [cite: 545-550]
edges_komputer = [
    (3, 'RouterA', 'RouterB'),
    (2, 'RouterA', 'RouterC'),
    (5, 'RouterB', 'RouterD'),
    (1, 'RouterC', 'RouterD'),
    (4, 'RouterB', 'RouterC')
]

# Implementasi Kruskal
edges_komputer.sort()
visited_routers = set()
mst_router = []
total_weight = 0

for weight, u, v in edges_komputer:
    # Syarat agar seluruh router terhubung tanpa cycle (logika sederhana)
    if u not in visited_routers or v not in visited_routers:
        mst_router.append((u, v, weight))
        total_weight += weight
        visited_routers.add(u)
        visited_routers.add(v)

print("Daftar Koneksi MST Jaringan Komputer:")
for u, v, w in mst_router:
    print(f"{u} --- {v} (Bobot: {w})")

print("-" * 30)
print(f"Total Bobot Minimum Jaringan = {total_weight}")

# ==========================================================
# JAWABAN ANALISIS:
# 1. Kasus apa yang dipilih? Kasus 2: Jaringan Komputer[cite: 564].
# 2. Algoritma apa yang digunakan? Algoritma Kruskal[cite: 565].
# 3. Edge mana saja yang dipilih dalam MST? RouterC-RouterD (1), 
#    RouterA-RouterC (2), dan RouterA-RouterB (3)[cite: 566].
# 4. Berapa total bobot MST? 6[cite: 567].
# 5. Mengapa edge tertentu tidak dipilih? Seperti RouterB-RouterC atau RouterB-RouterD 
#    tidak dipilih karena router-router tersebut sudah saling terhubung melalui 
#    RouterA dan RouterC. Menambahkannya hanya akan menambah beban biaya tanpa 
#    memberikan konektivitas baru (membentuk cycle)[cite: 105, 568].
# ==========================================================