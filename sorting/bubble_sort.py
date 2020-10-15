def bubble_sort(array):
    for step in range(0, len(array)):
        for index, item in enumerate(array):
            if (index+1 < len(array)) and (item > array[index+1]):
                array[index], array[index+1] = array[index+1], item
    return array

array_awal = [9, 6, 4, 1, 2, 3, 8]
print(f"Array awal : {array_awal}")
array_sort = bubble_sort(array_awal)
print(f"Hasil bubble sort : {array_sort}")