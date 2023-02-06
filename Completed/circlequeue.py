
def circleQueue(n, k):

    circleQueue = []
    output = "The winner is "
    for i in range (n):
        circleQueue.append(i+1)
    while len(circleQueue) > 1:
        for i in range (0, k-1):
            circleQueue.append(circleQueue.pop(0))
        circleQueue.pop(0)
        print(circleQueue)

    return output + str(circleQueue[0])

print(circleQueue(7, 3))