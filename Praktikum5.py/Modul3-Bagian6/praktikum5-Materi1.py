#====================================================
#Nama    : Muhammad Salman Alfarisy
#NIM     : J0403251118
#Kelas   : TPL B1
#====================================================

#====================================================
# Praktikum 5: Fungsi Rekursif (fungsi yang memanggil dirinya sendiri)
# Contoh kasus: Faktorial, Fibonacci, dll
# Base Case: kondisi dimana fungsi berhenti memanggil dirinya sendiri => 0 berhenti
# Recursive Case: kondisi dimana fungsi memanggil dirinya sendiri dengan parameter yang lebih sederhana => 3! = 3 x 2 x 1
# ====================================================

def faktorial(n):
    if n == 0: #base case
        return 1
    
    #recursive case
    return n* faktorial(n-1) #n-1*n-2*n-3*...*1

print ("============== Program Faktorial ==============")
print ("Hasil Faktorial : ",faktorial(6)) #5*4*3*2*1 = 120
