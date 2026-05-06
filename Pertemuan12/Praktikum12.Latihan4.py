# Nama : Mohammad Salman Alfarisy
# NIM : J0403251118
# Kelas : TPL B1
# Praktikum 12 Graph II: Shortest Path

# ===================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# ==================================================
import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
            
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

hasil = dijkstra(graph, 'Gerbang')
print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

# Jawaban Analisis:
# 1. Lokasi mana yang paling dekat dari Gerbang?
#    Jawab: Kantin (2 menit)
# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
#    Jawab: 7 menit (Jalur: Gerbang -> Kantin -> Lab -> Aula, yaitu 2 + 4 + 1 = 7)
# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
#    Jawab: Tidak selalu. Contohnya di sini, untuk ke Aula, kita harus melewati beberapa titik 
#           (Gerbang -> Kantin -> Lab -> Aula) agar total waktunya minimal (7), 
#           dibandingkan jalur langsung dari Kantin ke Aula (7) yang totalnya 9 jika lewat Gerbang.
# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
#    Jawab: Karena bobot pada graf (waktu tempuh) selalu bernilai positif, sehingga algoritma 
#           Dijkstra efisien dan akurat untuk kasus ini.