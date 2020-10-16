def linear_search(array, search):
    for data in array:
        if(data == search):
            return True
    return False

array = [3, 8, 1, 2, 9, 0, 4, 5]
search = 9

print(f"Array : {array}")
print(f"Mencari data {search} di array: ", linear_search(array, search))
print(f"Mengubah variabel search dengan 10")
search = 10
print(f"Mencari data {search} di array: ", linear_search(array, search))