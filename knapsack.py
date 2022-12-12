def knapSack(capacity, weight, value,n):

    if n == 0 or capacity == 0:
        return 0

    if (weight[n-1] > capacity):
        return knapSack(capacity, weight, value, n-1)

    else:
        return max(value[n-1] + knapSack(capacity-weight[n-1], weight, value, n-1),knapSack(capacity, weight, value, n-1))

value = [60, 100, 120]
weight = [10, 20, 30]
capacity = 20
n = len(value)

p= knapSack(capacity, weight, value,n)
print(p)
