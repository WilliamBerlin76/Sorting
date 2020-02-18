# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    i, j, k = 0, 0, 0

    while i < len(arrA) and j < len(arrB):
        # print(arrA, arrB)
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            i += 1
            k += 1
        elif arrA[i] > arrB[j]:
            merged_arr[k] = arrB[j]
            k += 1
            j += 1
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i += 1
        k += 1
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        j += 1
        k += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # divide array by 2 until left with sub arrays of len 1
    spl_point = len(arr)//2
    if len(arr) > 1:
        left = merge_sort(arr[:spl_point])
        right = merge_sort(arr[spl_point:])
        arr = merge(left, right)
        
    return arr
    
# print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
