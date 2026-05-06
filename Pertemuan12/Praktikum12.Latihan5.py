# Nama : Mohammad Salman Alfarisy
# NIM : J0403251118
# Kelas : TPL B1
# Praktikum 12 Graph II: Shortest Path

import heapq

# Representasi Graph
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Jakarta': {'Bandung': 7},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Bandung': {}
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

# Eksekusi
hasil = dijkstra(graph, 'Bogor')

print("Jarak terpendek dari Bogor:")
for kota, jarak in hasil.items():
    print(f"Bogor -> {kota} = {jarak}")

# Jawaban Analisis:
# 1. Node awal yang digunakan apa?
#    Jawab: Bogor
# 2. Node mana yang memiliki jarak paling kecil dari node awal?
#    Jawab: Depok (dengan jarak 2)
# 3. Node mana yang memiliki jarak paling besar dari node awal?
#    Jawab: Bandung (dengan jarak 8, via Depok -> Bandung 2+6 atau via Jakarta 4+7? 
#           Sebenarnya 2+6=8. Jalur lewat Jakarta: Bogor->Depok->Jakarta->Bandung = 2+2+7=11. 
#           Jadi 8 adalah yang terpendek untuk Bandung.)
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
#    Jawab: Dijkstra memulai dari Bogor (0). Ia melihat tetangga: Jakarta (5) dan Depok (2). 
#           Ia memilih Depok karena paling kecil. Dari Depok, ia melihat Jakarta (Depok ke Jakarta 2). 
#           Jarak Bogor ke Jakarta menjadi lebih pendek (2+2=4). Kemudian ia lanjut ke Bandung 
#           dari Depok (2+6=8) atau Jakarta (4+7=11). Ia memilih yang paling kecil yaitu 8.