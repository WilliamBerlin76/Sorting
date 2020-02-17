# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j 
                # print(arr[j], arr[smallest_index])   
               
        # TO-DO: swap
        # keep smallest item
        temp = arr[smallest_index]
        # swap smallest item with cur item
        arr[smallest_index] = arr[cur_index]
        #make current index the smallest index
        arr[cur_index] = temp
        
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    ar_sort = False
    if len(arr) == 0:
        return arr
    while ar_sort == False:
        count = 0
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                count += 1
            if count == 0 and i == len(arr) - 2:
                ar_sort = True
            elif count > 0 and i == len(arr) - 2:
                count -= count
            if ar_sort == True:
                return arr
                

# Recursive
# def bubble_sort( arr ):
#     count = 0
#     has_switched = count
#     for i in range(0, len(arr) - 1):
#         if arr[i] > arr[i + 1]:
#             temp = arr[i]
#             arr[i] = arr[i + 1]
#             arr[i + 1] = temp
#             count += 1
#     if count == has_switched:
#         return arr
#     else: 
#         return bubble_sort(arr)

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr