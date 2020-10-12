def insertionSort(array):
   for index in range(1,len(array)):
     currentvalue = array[index]
     position = index
     while position>0 and array[position-1]>currentvalue:
         array[position]=array[position-1]
         position = position-1
     array[position]=currentvalue
   return array

array = [9,6,4,1,2,3,8]
print(f"Array awal : {array}")
print(f"Hasil insertion sort : {insertionSort(array)}")
