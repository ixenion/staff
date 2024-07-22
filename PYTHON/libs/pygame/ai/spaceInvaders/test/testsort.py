def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
        
    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_greater) + [pivot] + quick_sort(items_lower)

#a = [2,6,4,3,4,1,0,9,7,8]
#a = [1,2,3,4,5,6]
#for i in range(3):
#    a.append(i)
#out = quick_sort(a)
#print(out)

a = [[1,2],[3,4], [5,6]]
rotate(a,-1)
print(a)

