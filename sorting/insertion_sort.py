def insertion_sort(array):
	for index_array in range(1, len(array)):
		current_value = array[index_array]
		position = index_array
		while position > 0 and array[position-1] > current_value:
			array[position] = array[position-1]
			position = position-1
		array[position] = current_value
	return array

array_awal = [9, 6, 4, 1, 2, 3, 8]
print(f"Array awal : {array_awal}")
array_sort = insertion_sort(array_awal)
print(f"Hasil insertion sort : {array_sort}")
