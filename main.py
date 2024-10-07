from DFA import DFA
from State import State
from Transition import Transition
def makeDfa( substring):
        # print("Running make dfa")
        numStates = len(substring) + 1
        states = []
        for i in range(numStates): 
            if (i == 0): 
                states.append(State((f"q_{i}"), True, False, 'self', 'self' )); 
            elif (i!=numStates -1): 
                states.append(State((f"q_{i}"), False, False, 'self', 'self' )); 
            else: 
                states.append(State((f"q_{i}"), False, True, 'self', 'self' )); 
        # for i in range(numStates): 
        #     #print(states[i].toDict())
        dfa = DFA(states)
        print(len(dfa.states))
        # dfa.invertDFA()
        for i in range(len(dfa.states)): 
            dfa.states[i].toDict()
        print(substring)
        Transition.buildTransitions(dfa.states, substring)

        


        
def main(): 
    #1: Get the input from the user
    substring = input("Enter the substring that should not appear:"); 
    #2: Parse input to make sure that there are no zeros and ones 
    if all(ch in "01" for ch in substring): 
       #Create DFA
    #    newDFA = DFA()
       makeDfa(substring)

    else: 
        print("Invalid string!")
        
        return 

main()


        