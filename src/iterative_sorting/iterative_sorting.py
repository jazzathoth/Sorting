# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    if(len(arr) > 1):
        for i in range(0, len(arr) - 1):
            cur_index = i
            smallest_index = cur_index
            for itr2 in range(cur_index, len(arr)):
                if arr[smallest_index] > arr[itr2]:
                    smallest_index = itr2
            arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        return arr
    else:
        return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    if(len(arr) > 1):
        fin = 0
        while fin != 1:
            fin = 1
            for i in range(1, len(arr)):
                if arr[i - 1] > arr[i]:
                    arr[i - 1], arr[i] = arr[i], arr[i - 1]
                    fin = 0
        return arr
    else:
        return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr