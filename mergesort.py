def merge_sort(arr):
    n = len(arr)

    if n <= 1:
        return arr
    
    else:
        mid = n//2
        left,right = arr[:mid],arr[mid:]

        merge_sort(left);merge_sort(right)

        l = r = k = 0

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                arr[k] = left[l]
                l += 1
            
            else:
                arr[k] = right[r]
                r += 1
            k += 1
        
        while l < len(left):
            arr[k] = left[l]
            l += 1
            k += 1
        
        while r < len(right):
            arr[k] = right[r]
            r += 1
            k += 1
    return arr


lis = [9,8,7,6,5,4,3]

p = merge_sort(lis)
print(p)
