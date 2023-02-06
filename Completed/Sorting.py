## Sorting

def find_min(li):
    min_idx = 0
    idx = 0
    while idx < len(li):
        if li[idx] < li[min_idx]:
            min_idx = idx
        idx+=1
    return min_idx

test_list = [1, 5, 0, 3, 2, 4, 8, 7]
out_list =[]
while test_list:
    min_idx = find_min(test_list)
    out_list.append(test_list[min_idx])
    test_list.remove(test_list[min_idx])
print(out_list)

def swap (li, a, b):
    temp = li[a]
    li[a] = li[b]
    li[b] = temp
    return li

unsortedlist = [3,5,2,8,6,7,4,9]
def selection_sort(li):
    for j in range (len(li)):
        min_idx = j
        for k in range(j + 1, len(li)):
            if(li[k] < li[min_idx]):
                min_idx = k
        swap(li, j, min_idx)
    return li
print(selection_sort(unsortedlist))

unsortedlist2 = [4,4,7,2,5,1,7,8]
def insertion_sort(li):
    for i in range (1, len(li)):
        while li[i] < li[i-1]:
            swap(li, i, i-1)
            if i>1:
                i-=1
    return li
print(insertion_sort(unsortedlist2))