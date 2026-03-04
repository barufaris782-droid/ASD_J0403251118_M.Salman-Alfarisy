
#============================================
#Nama   : Muhammad Aditya Firmansyah
#NIM    : J0403251035
#Kelas  : B2
#============================================

#============================================
#Latihan 3
#============================================

def insertion_sort(data):

    #melihat data awal
    print("Data Awal: ", data)
    print("-" * 19)

    #loop mulai dari data ke 2 (index array ke 1)
    for i in range(1, len(data)):

        key = data[i] #simpan nilai yang disisipkan
        j = i - 1 #index elemen terakhir di bagian kiri

        print("iterasi ke- ", i)
        print("Nilai Key =", key)
        print("Bagian Kiri (Terurut): ", data[:i])
        print("Bagian Kanan (Belum terurut): ", data[i:])
        
        #Geser
        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1
        #sisipkan key ke posisi yang benar
        data[j+1] = key

        print("Setelah disisipkan :", data)
        print("-" * 19)

    return data
data = [5, 2, 4, 6, 1, 3]
print("Hasil sorting: ", insertion_sort(data))


# '''
# Soal : 
# 1. Tuliskan isi list setelah iterasi i = 1. 
# 2. Tuliskan isi list setelah iterasi i = 3. 
# 3. Berapa kali pergeseran terjadi pada iterasi i = 4? 

# Jawaban :
# 1. [2, 5, 4, 6, 1, 3]
# 2. [2, 4, 5, 6, 1, 3]
# 3. 4 kali pergeseran
# '''
