#==============================================
#Nama: Mohammad Salman Alfarisy
#NIM:J0403521118
#Kelas: TPL B1
#==============================================

#==============================================
#Merge Sort tanpa Tracing
#==============================================
def merge_sort(data):
    if len(data) <= 1:
        return data
        #Divide: Membagi data menjadi 2 bagian
    mid = len(data) // 2
    left_half = data[:mid] #slicing kiri
    right_half = data[mid:] #slicing kanan

    #Recursive call
    l_sort = merge_sort(left_half)
    r_sort = merge_sort(right_half)

    merged = merge(l_sort, r_sort)
    return merged

def merge(left_half, right_half):

    result = []
    i = 0
    j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1

    # Append any remaining elements from either list
    result.extend(left_half[i:])
    result.extend(right_half[j:])

    return result
angka = [38, 27, 43, 3, 9, 82, 10]
print("Data awal:", angka)
sorted_angka = merge_sort(angka)
print("Data setelah diurutkan:", sorted_angka)
