from imp import init_builtin
import random
from sqlite3 import SQLITE_DELETE
import sys


class FrozenLake(object):

    def __init__(self, width, height, targets, blocked, holes, start):
        self.initial_state = start 
        self.width = width
        self.height = height
        self.targets = set(targets)
        self.holes = set(holes)
        self.blocked = set(blocked)

        # Parameters for the simulation
        self.gamma = 0.9
        self.success_prob = 0.5
        self.fail_prob = 0.25

    def get_reward(self, state):
        if state in self.holes: 
            return -5.0 
        elif state in self.targets:
            return 1.0
        else: 
            return -0.1

    def print_map(self, policy=None):
        sys.stdout.write(" ")
        for i in range(self.width):
            sys.stdout.write("--")
        sys.stdout.write("\n")
        for j in range(self.height): 
            
            sys.stdout.write("|")
            for i in range(self.width): 
                if (i,j) in self.targets:
                    sys.stdout.write("T ")
                elif (i,j) in self.holes:  
                    sys.stdout.write("O ")
                elif (i,j) in self.blocked: 
                    sys.stdout.write("# ")
                else: 
                    if policy and (i,j) in policy:
                        a = policy[(i,j)]
                        if a=="n":
                            sys.stdout.write("^")
                        elif a=="s":
                            sys.stdout.write("v")
                        elif a=="e":
                            sys.stdout.write(">")
                        elif a=="w":
                            sys.stdout.write("<")
                        sys.stdout.write(" ")
                    elif (i,j)==self.initial_state:
                        sys.stdout.write("* ")
                    else: 
                        sys.stdout.write(". ")
            sys.stdout.write("|")
            sys.stdout.write("\n")
        sys.stdout.write(" ")
        for i in range(self.width):
            sys.stdout.write("--")
        sys.stdout.write("\n")

    def get_transitions(self, state, direction):
        result = []
        x,y = state
        remain_p = 0.0

        if direction=="n": 
            success = (x,y-1)
            fail = [(x+1,y), (x-1,y)]
        elif direction=="s":
            success =  (x,y+1)
            fail = [(x+1,y), (x-1,y)]
        elif direction=="e":
            success = (x+1,y)
            fail= [(x,y-1), (x,y+1)]
        elif direction == "w":
            success = (x-1,y)
            fail= [(x,y-1), (x,y+1)]
          
        if success[0] < 0 or success[0] > self.width-1 or \
           success[1] < 0 or success[1] > self.height-1 or \
           success in self.blocked: 
                remain_p += self.success_prob
        else: 
            result.append((success, self.success_prob))
        
        for i,j in fail:
            if i < 0 or i > self.width-1 or \
               j < 0 or j > self.height-1 or \
               (i,j) in self.blocked: 
                    remain_p += self.fail_prob 
            else: 
                result.append(((i,j), self.fail_prob))
           
        if remain_p > 0.0: 
            result.append(((x,y), remain_p))
        return result

    def get_initial_utility_function(self):
        result = {}
        for x in range(self.width): 
            for y in range(self.height): 
                result[(x,y)] = 0.0
        return result

    #### Your code starts here ###
    
    def move(self, state, direction):
        """
        Return the state that results from going in this direction.
        """
        possible_transitions = self.get_transitions(state, direction)
        randNum = random.random()
        prob_total = 0
        for transition in possible_transitions:
            prob_total += transition[1]
            if randNum < prob_total:
                return transition[0]
    
    def get_random_policy(self):
        """
        Generate a random policy.
        """
        policy = {}
        for row in range(0, self.width):
            for col in range (0, self.height):    
                randNum = random.randInt(1, 4)
                if randNum == 1:
                    policy[(row, col)] = "n"
                if randNum == 2:
                    policy[(row, col)] = "s"
                if randNum == 3:
                    policy[(row, col)] = "e"
                if randNum == 4:
                    policy[(row, col)] = "w"
        return policy

    def simple_policy_rollout(self, policy):
        """
        Return True if a random trial with this policy is successful.  
        """
        targets = self.targets
        holes = self.holes
        state = self.initial_state
        while not state in targets and not state in holes:
            state = self.move(state, policy[state])
        if state in targets:
            return True
        else:
            return False

    def evaluate_policy(self, policy, t=100):
        """
        Return the percentage of successful trials within t random trials with
        this policy.
        """
        successes = 0
        for i in range(t):
            if self.simple_policy_rollout(policy):
                successes+=1
        return (successes / t)
    
    def value_iteration(self, epsilon = 0.001):
        """
        The value iteration algorithm to iteratively compute an optimal
        utility function.
        """
        util_func = self.get_initial_utility_function()
        new_util_func = util_func
        notTerminated = True
        while (notTerminated):
            for row in range(0, self.width):
                for col in range(0, self.height):
                    if col == self.height:
                        next = (row + 1, 0)
                    else:
                        next = (row, col + 1)
                    transitions = []
                    transitions.append(self.get_transitions((row, col), "n"))
                    transitions.append(self.get_transitions((row, col), "s"))
                    transitions.append(self.get_transitions((row, col), "e"))
                    transitions.append(self.get_transitions((row, col), "w"))
                    prob_sprime = 0
                    new_util_func[next] = self.get_reward((row, col))
                    for transition in transitions:
                        total_util = 0
                        if (row, col) != transition[0][0]:
                            prob_sprime += transition[0][1]
                            total_util+=util_func[transition[0][0]]
                        new_util_func[next] += (self.gamma * prob_sprime * total_util)
                    if ((new_util_func[next] - util_func[(row, col)]) < epsilon * (1 - self.gamma) / self.gamma):
                        notTerminated = False
                    util_func = new_util_func
        return util_func

    def extract_policy(self, utility_function):
        """
        Given a utility function, return the best policy. 
        """
        policy = {}
        for row in range(0, self.width):
            for col in range(0, row):
                transitions = []
                north = []
                south = []
                east = []
                west = []
                transitions.append(self.get_transitions((row, col), "n"))
                north.append(self.get_transitions((row, col), "n"))
                transitions.append(self.get_transitions((row, col), "s"))
                south.append(self.get_transitions((row, col), "s"))
                transitions.append(self.get_transitions((row, col), "e"))
                east.append(self.get_transitions((row, col), "e"))
                transitions.append(self.get_transitions((row, col), "w"))
                west.append(self.get_transitions((row, col), "w"))
                prob_sprime = 0
                sum  = 0
                max = (0, 0)
                for transition in transitions:
                    total_util = 0
                    if (row, col) != transition[0][0]:
                        prob_sprime += transition[0][1]
                        total_util+=utility_function[transition[0][0]]
                    sum+=(self.gamma * prob_sprime * total_util)
                    if sum > max[0]:
                        max = (sum, transition[0][0])
                if max[1] in north:
                    policy[(row, col)] = "n"
                elif max[1] in south:
                    policy[(row, col)] = "s"
                elif max[1] in east:
                    policy[(row, col)] = "e"
                else:
                    policy[(row, col)] = "w"
        return policy 
    def q_learn(self, episodes = 100, alpha = 0.5, epsilon = 0.2):
        q = []
        state = self.initial_state
        for row in range (0, self.width):
            for col in range (0, self.height):
                q.append((row, col), 0.0)
        while not state in self.targets and not state in self.holes:
            for k in range(episodes):
                max = 0
                for s, action in q:
                    if action > max:
                        max = action
                        state = self.move(s, action)

if __name__ == "__main__":
   
    # Create a lake simulation 
    lake = FrozenLake(width=8,height=8, targets=[(3,4)], blocked = [(3,3),(2,3),(2,4), ], holes=[(4,0),(4,1),(3,0),(3,1), (6,4),(6,5),(0,7),(0,6),(1,7)], start=(0,0))
    util_func = lake.value_iteration()
    policy = lake.extract_policy(util_func)
    lake.print_map(policy)

    
