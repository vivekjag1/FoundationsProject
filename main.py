from DFA import DFA
from State import State
def makeDfa( substring):
        print("Running make dfa")
        numStates = len(substring)
        states = []
        for i in range(numStates): 
            if (i == 0): 
                states.append(State((f"q_{i}"), True, False, 'self', 'self' )); 
            elif (i!=numStates): 
                states.append(State((f"q_{i}"), False, False, 'self', 'self' )); 
            else: 
                states.append(State((f"q_{i}"), False, True, 'self', 'self' )); 
        print(states)

            
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


        