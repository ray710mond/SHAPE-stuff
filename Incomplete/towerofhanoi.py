moves = 0

def Hanoi(src, buff, dest, k, moves):
    if k == 1:
        print("Move disk " + str(k) + " from " + src + " to " + dest + ".")
        moves+=1
        print("The puzzle took " + str(moves) + " moves to solve.")
    else:
        Hanoi(src, dest, buff, k-1, moves+1)
        print("Move disk " + str(k) + " from " + src + " to " + dest + ".")
        Hanoi(buff, src, dest, k-1, moves+1)

moves = 0
Hanoi('A', 'B', 'C', 4, moves)