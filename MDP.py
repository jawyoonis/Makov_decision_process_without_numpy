# Acknowlegement:
      # -Thanks to Emely Alfaro,who helped me to figure out to calculate the optimal policy
#
import copy
import random
class MDP():

    def __init__( self, gridword ):
        self.gridword=gridword
        self.V= [[0,0,0], [0,0,0], [0,0,0]]
        self.U = [[0,0,0], [0,0,0], [0,0,0]]
        self.policy =  [[0,0,0], [0,0,0], [0,0,0]]
        self.A = ['^', 'v', '>', '<']


    def get_policy(self):
        ''' This method calculates the optimal policy'''
        for i in range(len(self.gridword)):
            for j in range(len(self.gridword)):
                best_action = [self.expected_utility(i, j, "v"), "v"]
                for a in self.A:
                    if self.expected_utility(i, j, a) > best_action[0]:
                        best_action = [self.expected_utility(i, j, a), a]
                        print(best_action)
                self.policy[i][j] = best_action[1]
        print(self.policy)
    #


    def value_iteration( self, epsilon=0.01, iter=random.randint(10000,100000), gamma=0.94123):
        '''this method serves for the value iteration algorithm of MDP'''
        for i in range(iter):
            for i in range(len(self.gridword)):
                for j in range(len(self.gridword)):
                    optimal_action=[self.expected_utility(i, j, "v"), "v"]
                    for a in self.A:
                        if self.expected_utility(i, j, a) > optimal_action[0]:
                            optimal_action= [self.expected_utility(i, j, a), a]
                            print(optimal_action)
                    self.V[i][j]= self.gridword[i][j] + gamma*(optimal_action[0])
            print(self.U)
            self.U = copy.deepcopy(self.V)
            if optimal_action< epsilon * (1 - gamma) / gamma:
                 print(self.U)



                    #
    def get_the_value(self, i, j):
        ''' This method gets the reward value in each state in the grid and update the Utility a long the way'''
        if i < 0:
            return self.U[i+1][j]
        elif i > len(self.U)-1:
            return self.U[i-1][j]
        if j < 0:
            return self.U[i][j+1]
        elif j > len(self.U)-1:
            return self.U[i][j-1]
        return self.U[i][j]

    def expected_utility(self, i, j,a):
        '''this method serves to calculate total of the expected utility for each state regarding the actions'''
        if a == '^':
            return self.get_the_value(i-1, j)*0.7 + self.get_the_value(i+1, j) * 0.1 + self.get_the_value(i, j+1) * 0.1 + self.get_the_value(i, j-1) * 0.1
        elif a == 'v':
            return  self.get_the_value(i-1, j)*0.1 + self.get_the_value(i+1, j) * 0.7 + self.get_the_value(i, j+1) * 0.1 + self.get_the_value(i, j-1) * 0.1
        elif a == '>':
            return self.get_the_value(i-1, j)*0.1 + self.get_the_value(i+1, j) * 0.1 + self.get_the_value(i, j+1) * 0.7 + self.get_the_value(i, j-1) * 0.1
        elif a == '<':
            return  self.get_the_value(i-1, j)*0.1 + self.get_the_value(i+1, j) * 0.1 + self.get_the_value(i, j+1) * 0.1 + self.get_the_value(i, j-1) * 0.7
        return



mdp= MDP([[0, 0, 10],
         [0, -1, 0],
         [0, -1, 0]])
mdp.value_iteration()

mdp.get_policy()
