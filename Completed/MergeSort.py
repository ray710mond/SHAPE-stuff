def Merge(left, right):
    output = []
    a = 0
    b = 0
    while (a < len(left) and b < len(right)):
        if left[a] < right[b]:
            output.append(left[a])
            a+=1
        else:
            output.append(right[b])
            b+=1
    while len(left) > a:
        output.append(left[a])
        a+=1
    while len(right) > b:
        output.append(right[b])
        b+=1

    return output

def MergeSort(li):
    left = []
    right = []
    if(len(li) == 1 or len(li) == 0):
        return li
    else:
        left = li[0: len(li) // 2]
        right = li[len(li) // 2: len(li)]
        left = MergeSort(left)
        right = MergeSort(right)
        return Merge(left, right)

li = [3,6,4,7,8,2,4,9,8,1,0,7,4,8,5]

print(MergeSort(li))