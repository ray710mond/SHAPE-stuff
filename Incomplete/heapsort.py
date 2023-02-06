def heappush(heap, x):
    heap.insert(1, x)

def getMinIdx(heap):
    min_idx = 1
    for i in range (1, len(heap)):
        if heap[i] < heap[min_idx]:
            min_idx = i
    return min_idx

def heappop(heap):
    return heap.pop(1)

def heapify(heap):
    def swap(li, a, b):
        temp = li[a]
        li[a] = li[b]
        li[b] = temp
        return li
    try:
        heap.remove(None)
    except ValueError:
        print("")
    heap.insert(0, None)
    for i in range (1, len(heap)):
        leftchild = 2 * i
        rightchild = (2 * i) + 1
        parent = (i//2)
        if rightchild < len(heap):
            if heap[leftchild] < heap[rightchild]:
                if heap[leftchild] < heap[i]:
                    swap(heap, leftchild, i)
                    i = parent
            elif heap[rightchild] < heap[leftchild]:
                if heap[rightchild] < heap[i]:
                    swap(heap, rightchild, i)
                    i = parent
        elif leftchild < len(heap):
            if heap[leftchild] < heap[i]:
                swap(heap, leftchild, i)
                i = parent
    return heap

def heapsort(li):
    heap = heapify(li)
    output = []
    while heap:
        output.append(heappop(heap))
        heapify(heap)
    return output

li = [2,5,3,8,7,1,4,9,0,6]

print(heapify(li))

print(heapsort(li))