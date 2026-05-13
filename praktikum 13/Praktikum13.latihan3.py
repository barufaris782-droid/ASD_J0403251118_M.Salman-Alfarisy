# ==========================================================
# Nama : Mohammad Salman Alfarisy
# NIM : J0403251118
# Kelas : TPL B1
# Praktikum 13 Graph III: Minimum Spanning Tree (MST)
# Implementasi Algoritma Prim (Minimum Spanning Tree)
# ==========================================================

import heapq

# 1. Representasi Graph menggunakan Adjacency List (Dictionary) [cite: 270, 439]
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start_node):
    visited = {start_node} 
    priority_queue = [] # Heap untuk menyimpan edge potensial
    
    # Masukkan semua edge dari node awal ke priority queue [cite: 300, 473]
    for neighbor, weight in graph[start_node].items():
        heapq.heappush(priority_queue, (weight, start_node, neighbor))
    
    mst = []
    total_weight = 0
    
    while priority_queue:
        weight, u, v = heapq.heappop(priority_queue) 
        
        # Jika node tujuan belum dikunjungi, tambahkan ke MST [cite: 306, 483]
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            
            # Tambahkan edge dari node yang baru dikunjungi ke queue [cite: 310, 486]
            for neighbor, next_weight in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (next_weight, v, neighbor))
                    
    return mst, total_weight

# Eksekusi Algoritma
mst_result, total = prim(graph, 'A')

# Cetak Hasil 
print("Minimum Spanning Tree (MST) - Algoritma Prim:")
for u, v, weight in mst_result:
    print(f"Edge {u} - {v} dengan bobot {weight}")

print("-" * 30)
print(f"Total bobot MST = {total}")

# ==========================================================
# JAWABAN ANALISIS:
# 1. Node awal apa yang digunakan? Node 'A'.
# 2. Edge mana yang dipilih pertama kali? Edge A-C dengan bobot 2.
# 3. Bagaimana Prim menentukan edge berikutnya? Dengan mencari edge dengan bobot 
#    terkecil yang menghubungkan node yang sudah dikunjungi dengan node yang 
#    belum dikunjungi.
# 4. Berapa total bobot MST yang dihasilkan? Total bobotnya adalah 6.
# 5. Apa perbedaan pendekatan Prim dan Kruskal? Kruskal memilih edge global terkecil 
#    (fokus pada edge), sedangkan Prim tumbuh secara bertahap dari satu node awal 
#    (fokus pada node).
# ==========================================================