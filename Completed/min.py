## min
list = [5, 3, 2, 0, 1, 9, 8]
min_idx = 0
idx = 0
while idx < len(list):
    if list[idx] < list[min_idx]:
        min_idx = idx
    idx+=1

print(list[min_idx], "at index", min_idx)