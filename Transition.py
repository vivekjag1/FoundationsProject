from allSame import allSame, allSameToIndex
class Transition: 
    def __init__(self, states): 
        self.states = states
    def buildTransitions(states, substring): 
        allTransitions = []
        '''
        [q0, q1, q2]
        1. read the state 
        2. if not the next char
            stay at state 
        3. if next char 
            move to next state
        '''
        '''
        1110 


        q0 q1 q2 q3 q4 q5

        '''
        # prevChar = ''
        # allSame = True





        for i in range(len(states)):     
            '''
            [move if 0 is read, move if 1 is read]
            '''
            next = -1
            if(i + 1 != len(states)):
                next = i+1
            else: 
                next = i
            if(i == len(states) - 1 ): 
                #if on the last state, trap and transition to yourself no matter what
                transition = [states[i], states[i]] 
                allTransitions.append(transition)
                for i in range(len(allTransitions)): 
                    for x in range(len(allTransitions[i])): 
                        allTransitions[i][x].toDict() 
                return 

            if(allSameToIndex(substring, i) and i== len(substring) -1):
                transition = [states[i], states[0]]
                for i in range(len(allTransitions)): 
                    for x in range(len(allTransitions[i])): 
                        allTransitions[i][x].toDict() 
                return 
            elif (allSameToIndex(substring, i) and i != len(substring) -1 and substring[i] != substring[i+1]): 
                transition = [states[i+1], states[i]]
                allTransitions.append(transition)
            elif (allSameToIndex(substring, i) and i != len(substring) -1 and substring[i] == substring[i+1]): 
                transition = [states[i], states[i+1] ]
                allTransitions.append(transition)
                 
            else: 
                if(substring[i] == '0'): 
                    transition = [states[next], states[i]]
                    allTransitions.append(transition)
                else: 
                    transition = [states[i], states[next]]
                    allTransitions.append(transition)
            
        return 
    


