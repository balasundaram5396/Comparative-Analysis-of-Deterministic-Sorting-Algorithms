import random
import time

#INSERTION SORT
def insertionSort(arr):
   for i in range(1,len(arr)):
       if arr[i] >= arr[i-1]:
           continue
       for j in range(i):
           if arr[i] < arr[j]:
               arr[j],arr[j+1:i+1] = arr[i],arr[j:i]
               break
#MERGE SORT
def mergeSort(arr): 
	if len(arr) >1: 
		middle = len(arr)//2 
		left = arr[:middle] 
		right = arr[middle:] 

		mergeSort(left)
		mergeSort(right) 

		i = j = k = 0
		while i < len(left) and j < len(right): 
			if left[i] < right[j]: 
				arr[k] = left[i] 
				i+=1
			else: 
				arr[k] = right[j] 
				j+=1
			k+=1

		while i < len(left): 
			arr[k] = left[i] 
			i+=1
			k+=1
		
		while j < len(right): 
			arr[k] = right[j] 
			j+=1
			k+=1

#HEAP SORT
def build_min_heap(array):
    for i in reversed(range(len(array)//2)):
        min_heapify(array, i)

def min_heapify(array, i):
    left = 2 * i + 1
    right = 2 * i + 2
    length = len(array) - 1
    smallest = i
    if left <= length and array[i] > array[left]:
        smallest = left
    if right <= length and array[smallest] > array[right]:
        smallest = right
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        min_heapify(array, smallest)

def heapSort(arr):
    array = arr[:]
    build_min_heap(array)
    sorted_array = []
    for i in range(len(array)):
        array[0], array[-1] = array[-1], array[0]
        sorted_array.append(array.pop())
        min_heapify(array, 0)
    return sorted_array

#IN-PLACE QUICK SORT
def partition(arr,low,high):
   i = ( low-1 )         
   pivot = arr[high]
 
   for j in range(low , high):
       if   arr[j] <= pivot:
           i = i+1
           arr[i],arr[j] = arr[j],arr[i]

   arr[i+1],arr[high] = arr[high],arr[i+1]
   return ( i+1 )
 
def quick(arr,low,high):
   if low < high:
       pi = partition(arr,low,high)
       quickSort(arr, low, pi-1)
       quickSort(arr, pi+1, high)

def quickSort(arr):
    quick(arr,0,len(arr)-1)

#QUICK SORT USING MEDIAN AS PIVOT
def swap(arr,a,b):
   arr[a],arr[b] = arr[b],arr[a]
def partition(arr,start,end):
   med = ((end - 1) - start) // 2
   med = med + start
   left = start + 1
   if (arr[med] - arr[end-1])*(arr[start]-arr[med]) >= 0:
       swap(arr,start,med)
   elif (arr[end - 1] - arr[med]) * (arr[start] - arr[end - 1]) >=0:
        swap(arr,start,end - 1)
   pivot = arr[start]
   for right in range(start,end):
       if pivot > arr[right]:
           swap(arr,left,right)
           left = left + 1
   swap(arr,start,left-1)
   return left-1
def quick(arr,left,right):
   if left < right:
       split = partition(arr,left,right)
       quick(arr,left,split)
       quick(arr,split+1,right)
def mquickSort(arr):
   quick(arr,0,len(arr))

#main
size = int(input("Enter number range to sort:\neg. 100,500,1000,2000,5000,...,50000\n"))
def Random_input_gen(start, size): 
    input_list = [] 
  
    for n in range(size): 
        input_list.append(random.randint(start, size)) 
    return input_list

arr = Random_input_gen(1,size)
choice = int(input("Enter your choice:\n 1. Sorting of random numbers\n 2. Sorting when input array is already sorted\n 3. Sorting when input array is reversely sorted\n"))
if(choice == 1):
###---------------------------------------------------------------INSERTION SORT---------------------------------------------------------------###
	start = time.time()
	insertionSort(arr)
	end = time.time()
	print("Execution time of Insertion Sort:",end - start,"secs")
	#print(arr)
###-------------------------------------------------------------------MERGE SORT---------------------------------------------------------------###
	start = time.time()
	mergeSort(arr)
	end = time.time()
	print("Execution time of Merge Sort:",end - start,"secs")
	#print(arr)
###------------------------------------------------------------------HEAP SORT-----------------------------------------------------------------###
	start = time.time()
	heapSort(arr)
	end = time.time()
	print("Execution time of Heap Sort:",end - start,"secs")
	#print(arr)
###-----------------------------------------------------------------QUICK SORT-----------------------------------------------------------------###
	start = time.time()
	quickSort(arr)
	end = time.time()
	print("Execution time of Quick Sort:",end - start,"secs")
	#print(arr)
###---------------------------------------------------------QUICK SORT FOR MEDIAN OF 3---------------------------------------------------------###
	if(size <= 10):
		print("Calling Insertion sort since array size is less than or equal to 10\n")
		start = time.time()
		insertionSort(arr)
		end = time.time()
		print("Execution time of Insertion Sort :",end - start,"secs")
	else:
		start = time.time()
		mquickSort(arr)
		end = time.time()
		print("Execution time of Quick Sort for Median of 3:",end - start,"secs")
		#print(arr)

elif (choice == 2):
	arr_sort = sorted(arr)
###---------------------------------------------------------------INSERTION SORT---------------------------------------------------------------###
	start = time.time()
	insertionSort(arr_sort)
	end = time.time()
	print("Execution time of Insertion Sort:",end - start,"secs")
	#print(arr_sort)
###-------------------------------------------------------------------MERGE SORT---------------------------------------------------------------###
	start = time.time()
	mergeSort(arr_sort)
	end = time.time()
	print("Execution time of Merge Sort:",end - start,"secs")
	#print(arr_sort)
###------------------------------------------------------------------HEAP SORT-----------------------------------------------------------------###
	start = time.time()
	heapSort(arr_sort)
	end = time.time()
	print("Execution time of Heap Sort:",end - start,"secs")
	#print(arr_sort)
###-----------------------------------------------------------------QUICK SORT-----------------------------------------------------------------###
	start = time.time()
	quickSort(arr_sort)
	end = time.time()
	print("Execution time of Quick Sort:",end - start,"secs")
	#print(arr_sort)
###---------------------------------------------------------QUICK SORT FOR MEDIAN OF 3---------------------------------------------------------###
	if(size <= 10):
		print("Calling Insertion sort since array size is less than or equal to 10\n")
		start = time.time()
		insertionSort(arr_sort)
		end = time.time()
		print("Execution time of Insertion Sort :",end - start,"secs")
	else:
		start = time.time()
		mquickSort(arr_sort)
		end = time.time()
		print("Execution time of Quick Sort for Median of 3:",end - start,"secs")
		#print(arr_sort)

else:
	arr_rev = sorted(arr,reverse = True)
###---------------------------------------------------------------INSERTION SORT---------------------------------------------------------------###
	start = time.time()
	insertionSort(arr_rev)
	end = time.time()
	print("Execution time of Insertion Sort:",end - start,"secs")
	#print(arr_rev)
###-------------------------------------------------------------------MERGE SORT---------------------------------------------------------------###
	start = time.time()
	mergeSort(arr_rev)
	end = time.time()
	print("Execution time of Merge Sort:",end - start,"secs")
	#print(arr_rev)
###------------------------------------------------------------------HEAP SORT-----------------------------------------------------------------###
	start = time.time()
	heapSort(arr_rev)
	end = time.time()
	print("Execution time of Heap Sort:",end - start,"secs")
	#print(arr_rev)
###-----------------------------------------------------------------QUICK SORT-----------------------------------------------------------------###
	start = time.time()
	quickSort(arr_rev)
	end = time.time()
	print("Execution time of Quick Sort:",end - start,"secs")
	#print(arr_rev)
###---------------------------------------------------------QUICK SORT FOR MEDIAN OF 3---------------------------------------------------------###
	if(size <= 10):
		print("Calling Insertion sort since array size is less than or equal to 10\n")
		start = time.time()
		insertionSort(arr_rev)
		end = time.time()
		print("Execution time of Insertion Sort :",end - start,"secs")
	else:
		start = time.time()
		mquickSort(arr_rev)
		end = time.time()
		print("Execution time of Quick Sort for Median of 3:",end - start,"secs")
		#print(arr_rev)