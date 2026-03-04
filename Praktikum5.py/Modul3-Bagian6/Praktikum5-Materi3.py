# ====================================================
# Nama : Mohammad Salman Alfarisy
# NIM : J0403521118
# Kelas : TPL B1
# ====================================================


#====================================================
# Materi Rekursif: Menjumlahkan elemen list menggunakan rekursif
# ====================================================

def jumlahkan_list(lst, index=0):
    if index == len(lst): #base case: jika index mencapai panjang list, berhenti
        return 0
    
    #recursive case: jumlahkan elemen saat ini dengan hasil penjumlahan sisa list
    return lst[index] + jumlahkan_list(lst, index + 1)

print ("============== Program Penjumlahan List ==============")
my_list = [1, 2, 3, 4, 5]
print ("Hasil Penjumlahan List : ",jumlahkan_list(my_list, 0)) #1+2+3+4+5 = 15