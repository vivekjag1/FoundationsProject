from State import State 
class DFA: 
    '''
    A dfa is a 5 tuple 
    1. the set of states 
    2. the allowable chars. 
    3. transition function 
    4. the start state. 
    5. the set of accept states 
    '''
    def __init__(self, states, transitionValues): 
        self.states = states 
        self.transitionValues = transitionValues

    
    


    