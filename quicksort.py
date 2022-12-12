def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    else:
        pivot = arr.pop()

    upperlist = []
    lowerlist = []

    for ele in arr:
        if ele > pivot:
            upperlist.append(ele)
        else:
            lowerlist.append(ele)
    
    return quick_sort(lowerlist) + [pivot] + quick_sort(upperlist)

lis = [9,8,7,6,5,4,3,2,1]
p = quick_sort(lis)
print(p)
