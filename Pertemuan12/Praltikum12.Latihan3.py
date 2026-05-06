# Nama : Mohammad Salman Alfarisy
# NIM : J0403251118
# Kelas : TPL B1
# Praktikum 12 Graph II: Shortest Path

# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================
# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    # Fungsi untuk mencari jarak terpendek dari node start
    # ke seluruh node lain menggunakan algoritma Bellman-Ford.
    
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0
    distances[start] = 0
    
    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for i in range(len(graph) - 1):
        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():
                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
    return distances

hasil = bellman_ford(graph, 'A')
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# Jawaban Analisis:
# 1. Berapa bobot langsung dari A ke B?
#    Jawab: 5
# 2. Berapa total bobot jalur A->C->B?
#    Jawab: 4 + (-2) = 2
# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
#    Jawab: Jalur melalui C (A->C->B) dengan total 2.
# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
#    Jawab: Karena algoritma ini melakukan relaksasi pada semua edge berulang kali (sebanyak V-1 kali), 
#           sehingga mampu menemukan jalur optimal meski terdapat bobot negatif.
# 5. Apa yang dimaksud dengan proses relaksasi edge?
#    Jawab: Proses memperbarui jarak terpendek ke suatu node jika ditemukan jalur yang 
#           lebih pendek melalui edge tertentu.
# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
#    Jawab: Dijkstra lebih cepat tetapi tidak bisa menangani bobot negatif. Bellman-Ford lebih 
#           lambat karena melakukan iterasi berulang, namun mampu menangani bobot negatif.