def merge_sort(arr):
    if len(arr)>1:
        left = arr[0:len(arr)//2]
        right = arr[len(arr)//2 : ]
        merge_sort(left )
        merge_sort(right)
        merge_two_sorted_arrays(left,right,arr)


def merge_two_sorted_arrays(a,b,arr):
    i = j = k = 0
    while i< len(a) and j< len(b):
        if a[i]<=b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1
    if i< len(a):
        arr[k:] = a[i:]
    else:
        arr[k:] = b[j:]


arr = [4,1,12,7,5]
merge_sort(arr)
print(arr)

