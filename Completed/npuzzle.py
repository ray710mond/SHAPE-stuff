"""
SHAPE Summer 2022

In this assignment you will implement and compare different search strategies
for solving the n-Puzzle, which is a generalization of the 8 and 15 puzzle to
squares of arbitrary size (we will only test it with 8-puzzles for now). 
See Courseworks for detailed instructions.
"""

import time
import random

def state_to_string(state):
    row_strings = [" ".join([str(cell) for cell in row]) for row in state]
    return "\n".join(row_strings)


def swap_cells(state, i1, j1, i2, j2):
    """
    Returns a new state with the cells (i1,j1) and (i2,j2) swapped. 
    """
    value1 = state[i1][j1]
    value2 = state[i2][j2]
    
    new_state = []
    for row in range(len(state)): 
        new_row = []
        for column in range(len(state[row])): 
            if row == i1 and column == j1: 
                new_row.append(value2)
            elif row == i2 and column == j2:
                new_row.append(value1)
            else: 
                new_row.append(state[row][column])
        new_state.append(tuple(new_row))
    return tuple(new_state)
    

def get_successors(state):
    """
    This function returns a list of possible successor states resulting
    from applicable actions. 
    The result should be a list containing (Action, state) tuples. 
    For example [("Up", ((1, 4, 2),(0, 5, 8),(3, 6, 7))), 
                 ("Left",((4, 0, 2),(1, 5, 8),(3, 6, 7)))] 
    """ 
    child_states = []

    for row in range(len(state)):
        for column in range(len(state[row])):
            if state[row][column] == 0:
                if column < len(state)-1: # Left 
                    new_state = swap_cells(state, row,column, row, column+1)
                    child_states.append(("Left",new_state))
                if column > 0: # Right 
                    new_state = swap_cells(state, row,column, row, column-1)
                    child_states.append(("Right",new_state))
                if row < len(state)-1:   #Up 
                    new_state = swap_cells(state, row,column, row+1, column)
                    child_states.append(("Up",new_state))
                if row > 0: # Down
                    new_state = swap_cells(state, row,column, row-1, column)
                    child_states.append(("Down", new_state))
                break
    return child_states

            
def goal_test(state):
    """
    Returns True if the state is a goal state, False otherwise. 
    """    
    counter = 0
    for row in state:
        for cell in row: 
            if counter != cell: 
                return False 
            counter += 1
    return True

def bfs(state):
    """
    Breadth first search.
    Returns A list of actions
    Should print:  the number of states expanded, and the maximum size of the frontier.  
    """
    prev = {}
    actions = {} # for each discovered state,
                 # what is the action that 
                 # took you there

    # Write code here for bfs.  
    queue = []
    discovered  = set()
    queue.append(state)
    discovered.add(state)

    total_visited_states = 0
    while queue:
        u = queue.pop(0)
        total_visited_states +=1
        successors = get_successors(u)
        for action, v in successors:
            if v not in discovered:   
                discovered.add(v)
                queue.append(v)
                prev[v] = u
                actions[v] = action
                if goal_test(v) == True:
                    i = v
                    path = []
                    while(i != state):
                        path.append(actions[i])
                        i = prev[i]
                    print("Total Visited States: " + str(total_visited_states))
                    path.reverse()
                    return path
    print("Total Visited States: " + str(total_visited_states))       
    return None # No solution found
                               
     
def dfs(state):
    """
    Depth first search.
    Returns: A list of actions.
    Should print: the number of states expanded, and the maximum size of the frontier.  
    """
    prev = {}
    actions = {}
    
    #Write code here for dfs  
    stack = []
    discovered  = set()
    stack.append(state)
    discovered.add(state)

    total_visited_states = 0
    while stack:
        u = stack.pop()
        total_visited_states +=1
        successors = get_successors(u)
        for action, v in successors:
            if v not in discovered:   
                discovered.add(v)
                stack.append(v)
                prev[v] = u
                actions[v] = action
                if goal_test(v) == True:
                    i = v
                    path = []
                    while(i != state):
                        path.append(actions[i])
                        i = prev[i]
                    print("Total Visited States: " + str(total_visited_states))
                    path.reverse()
                    return path
    print("Total Visited States: " + str(total_visited_states))       
    return None # No solution found

def misplaced_heuristic(state):
    """
    Returns the number of misplaced tiles.
    """
    count = 0
    misplaced_tiles = 0
    for j in state:
        for k in j:
            if k != count and k != 0:
                misplaced_tiles+=1
            count+=1

    return misplaced_tiles # replace this


def manhattan_heuristic(state):
    """
    For each misplaced tile, compute the manhattan distance between the current
    position and the goal position. THen sum all distances. 
    """
    heuristic = 0
    def correct_row(int):
        if int in [1, 2]:
            correct_row = 0
        if int in [3, 4, 5]:
            correct_row = 1
        if int in [6, 7, 8]:
            correct_row = 2
        return correct_row
    def correct_column(int):
        if int in [3, 6]:
            correct_column = 0
        if int in [1, 4, 7]:
            correct_column = 1
        if int in [2, 5, 8]:
            correct_column = 2
        return correct_column
    for row in range (0, len(state)):
        for column in range (0, len(state[row])):
            if state[row][column] != 0:
                row_moves = correct_row(state[row][column]) - row
                column_moves = correct_column(state[row][column]) - column
                if row_moves < 0:
                    row_moves *= -1
                if column_moves < 0:
                    column_moves *= -1
                heuristic += row_moves
                heuristic += column_moves
            
    return heuristic # replace this

def greedy(state, heuristic = misplaced_heuristic):
    """
    Greedy search is a variant of depth-first search that uses a heuristic to 
    select the next state from the immediate successor states.  
    Returns three values: A list of actions.

    Should print:  the number of states expanded, and the maximum size of the frontier.  
    """

    # You might want to use these functions to maintain a priority queue
    # You may also use your own heap class here
    from heapq import heappush
    from heapq import heappop

    parents = {}
    actions = {}
    costs = {}

    costs[state] = 0

    # Write best first search here.
    stack = []
    discovered  = set()
    stack.append(state)
    discovered.add(state)
    total_visited_states = 0
    while stack:
        u = stack.pop()
        successors = get_successors(u)
        total_visited_states +=1
        tmp_list = []
        for s in successors: 
            tmp_list.append((heuristic(s[1]), s)) 
        tmp_list.sort(reverse = True)
        successors2 = [s for (h, s) in tmp_list]
        for action, v in successors2:
            if v not in discovered:   
                discovered.add(v)
                stack.append(v)
                parents[v] = u
                actions[v] = action
                if goal_test(v) == True:
                    i = v
                    path = []
                    while(i != state):
                        path.append(actions[i])
                        i = parents[i]
                    print("Total Visited States: " + str(total_visited_states))
                    path.reverse()
                    return path
    print("Total Visited States: " + str(total_visited_states))
    return None # No solution found


def best_first(state, heuristic = misplaced_heuristic):
    """
    Breadth first search using the heuristic function passed as a parameter.
    Returns: A list of actions
    Shoudl print: the number of states visited, and the maximum size of the frontier.  
    """

    # You might want to use these functions to maintain a priority queue
    # You may also use your own heap class here
    import heapq

    parents = {}
    actions = {}
    costs = {}

    costs[state] = 0

    # Write best first search here.
    heap = []
    discovered  = set()
    heapq.heappush(heap, (heuristic(state), state))
    discovered.add(state)
    total_visited_states = 0
    while heap:
        h_value, u = heapq.heappop(heap)
        successors = get_successors(u)
        total_visited_states +=1
        #for s in successors: 
        #    tmp_list.append((heuristic(s[1]), s)) 
        #tmp_list.sort(reverse = True)
        #successors = [s for (h, s) in tmp_list]
        for action, v in successors:
            if v not in discovered:   
                discovered.add(v)
                heapq.heappush(heap, (heuristic(v),v))
                parents[v] = u
                actions[v] = action
                if goal_test(v) == True:
                    i = v
                    path = []
                    while(i != state):
                        path.append(actions[i])
                        i = parents[i]
                    print("Total Visited States: " + str(total_visited_states))
                    path.reverse()
                    return path
    print("Total Visited States: " + str(total_visited_states)) 
    return None # No solution found


def astar(state, heuristic = misplaced_heuristic):
    """
    A-star search using the heuristic function passed as a parameter. 
    Returns: A list of actions
    Should print: the number of states expanded, and the maximum size of the frontier.  
    """
    # You might want to use these functions to maintain a priority queue
    # You may also use your own heap class here

    import heapq

    parents = {}
    actions = {}
    costs = {}

    costs[state] = 0
    
    # Write A* search here
    heap = []
    discovered  = set()
    heapq.heappush(heap, (heuristic(state), state))
    discovered.add(state)
    total_visited_states = 0
    while heap:
        f_value, u = heapq.heappop(heap)
        total_visited_states +=1
        successors = get_successors(u)
        for action, v in successors:
            if v not in discovered:   
                discovered.add(v)
                parents[v] = u
                actions[v] = action
                costs[v] = costs[u] + 1
                heapq.heappush(heap, (heuristic(v)+costs[v], v))
                if goal_test(v) == True:
                    i = v
                    path = []
                    while(i != state):
                        path.append(actions[i])
                        i = parents[i]
                    print("Total Visited States: " + str(total_visited_states))
                    path.reverse()
                    return path
    print("Total Visited States: " + str(total_visited_states)) 
    return None # No solution found


def print_result(solution):
    """
    Helper function to format test output. 
    """
    if solution is None: 
        print("No solution found.")
    else: 
        print("Solution has {} actions.".format(len(solution)))



if __name__ == "__main__":

    #Easy test case
    test_state = ((1, 4, 2),
                  (0, 5, 8), 
                  (3, 6, 7))  

    #More difficult test case
    #test_state = ((7, 2, 4),
    #              (5, 0, 6), 
    #              (8, 3, 1))  

    print(state_to_string(test_state))
    print()

    print("====BFS====")
    start = time.time()
    solution = bfs(test_state)
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end-start))

    print() 
    print("====DFS====") 
    start = time.time()
    solution = dfs(test_state)
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end-start))


    print()
    print("====Greedy====") 
    start = time.time()
    solution = greedy(test_state, misplaced_heuristic)
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end-start))
    

    print() 
    print("====Best-First====") 
    start = time.time()
    solution = best_first(test_state, misplaced_heuristic)
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end-start))
    
    print() 
    print("====A*====") 
    start = time.time()
    solution = astar(test_state, misplaced_heuristic)
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end-start))



