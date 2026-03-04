# ====================================================
# Nama : Mohammad Salman Alfarisy
# NIM : J0403521118
# Kelas : TPL B1
# ====================================================


#====================================================
# Materi Rekursif: Call Stack (tumpukan panggilan fungsi)
# input 3
# Masuk 1 - 2 - 3
# Keluar 3 - 2 - 1
# ====================================================

input_n = int(input("Masukkan angka untuk dihitung: "))
def hitung(n):
    if n == 0: #base case
        print("\nSelesai\n")
        return 1
    
    print("Masuk: ", n)
    hitung(n-1) #recursive case
    print("Keluar: ", n)

print ("\n============== Program Tracing ==============\n")
hitung(input_n)
