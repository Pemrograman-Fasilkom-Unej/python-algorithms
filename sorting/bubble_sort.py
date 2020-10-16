def bubble_sort(array):
    for step in range(len(array)):
        flagged = False
        for index, item in enumerate(array):
            # keluar loop ketika index berikutnya melebihi/sama dengan panjang array
            if (index+1 >= len(array)):
                break
            if item > array[index+1]:
                # tukar nilai saat ini, dengan nilai berikutnya ketika lebih besar
                array[index], array[index+1] = array[index+1], item
                # tandai jika ada perubahan
                flagged = True
        # kalau tidak ada yang berubah dalam step saat ini, STOP dari semua iterasi
        if not flagged:
            break
    # kembalikan jumlah langkah yang dilewati dan array hasil sorting
    return step, array

array_awal = [1, 2, 3, 4, 5, 6]
#array_awal = [9, 6, 4, 1, 0, 2, 3, 0, 8, 8]
print(f"Array awal : {array_awal}")
jumlah_langkah, array_sort = bubble_sort(array_awal)
print(f"Hasil bubble sort : {array_sort}")
print(f"Jumlah Iterasi : {jumlah_langkah}")