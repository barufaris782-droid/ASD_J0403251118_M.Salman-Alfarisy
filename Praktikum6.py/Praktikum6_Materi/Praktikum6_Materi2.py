#=========================================
#Insertion Sort (Ascending) dengan Tracing
#Nama: Mohammad Salman Alfarisy
#NIM:J0403521118
#Kelas: TPL B1
#=========================================

def insertion_sort(data):

    #melihat data awal
    print("Data awal:", data)
    print("="*50)
#Loop mulai data ke 2 (index 1) sampai akhir
    for i in range(1, len(data)):
        key = data[i] #elemen yang akan disisipkan
        j = i - 1 #indeks elemen sebelum key

        print("Iterasi ke-", i)
        print("Key yang akan disisipkan:", key)
        print("Bagian Kiri(terurut):", data[:i])
        print("Bagian Kanan(belum terurut):", data[i:])

        #geser elemen yang lebih besar dari key ke kanan
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j] #geser elemen ke kanan
            j -= 1
        
        data[j + 1] = key #sisipkan key di posisi yang benar

        print("Setelah Disisipkan:", data)
#Contoh penggunaan
data = [5 , 2, 4, 6, 1, 3]
insertion_sort(data)