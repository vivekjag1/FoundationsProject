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
    def __init__(self, states): 
        self.states = states 
    def invertDFA(self): 
        for i in range (len(self.states)): 
            obj = self.states[i]
            #if the state is accepting make it non accepting 
           
            self.states[i] = State(obj.name, obj.isStart, not (obj.isAccept), obj.origin, obj.dest)
        numStates = len(self.states)
        for i in range(numStates): 
             obj = self.states[i]
            # print(obj.toDict())
