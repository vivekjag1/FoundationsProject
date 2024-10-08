from DFA import DFA
from State import State
from Transition import Transition
from Transition import printThings
def makeDfa( substring):
        # print("Running make dfa")
        numStates = len(substring) + 1
        states = []
        for i in range(numStates): 
            if (i == 0): 
                states.append(State((f"q_{i + 1}"), True, False, 'self', 'self' )); 
            elif (i!=numStates -1): 
                states.append(State((f"q_{i + 1}"), False, False, 'self', 'self' )); 
            else: 
                states.append(State((f"q_{i + 1}"), False, True, 'self', 'self' )); 
        # for i in range(numStates): 
        #     #print(states[i].toDict())
        dfa = DFA(states)
        dfa.invertDFA()

        print(len(dfa.states))
        # dfa.invertDFA()
        # for i in range(len(dfa.states)): 
        #     dfa.states[i].toDict()
        # print(substring)

        # print("\nTHIS IS THE TRANSITION FUNCTION")
        # allNewTransition = Transition.buildTransitions(dfa.states, substring)
        return states 
    

def buildGNFA(states, transitions):
    # Add new start state
    state = State((f"q_{0}"), True, False, 'self', 'self' )
    states.insert(0, state)
    # Edit old start state to now make it normal state
    oldStart = states[1]
    oldStart.isStart = False
    states[1] = oldStart
    # Make new transition for new start state
    transitions.insert(0, [None, None, states[1]])

    #build new accept state 
    newAccept = State("q_accept", False, True, 'self', 'self')
    states.append(newAccept)

    #iterate through the list of transitions and if we get to an accept state, make it non accpeting and add transition to this new state 
    for i in range(len(states) - 1): 
         thisState = states[i]
    
         if(thisState.isAccept):
              print("At state at index", i)
              thisState.isAccept=False
              transitions[i].append(newAccept)
    

    return transitions




        
def printThings(allTransitions):
    for i in range(len(allTransitions)): 
                    for x in range(len(allTransitions[i])): 
                        if(allTransitions[i][x] == None):
                             print("None")
                        else:
                            allTransitions[i][x].toDict()


        

        
def main(): 
    #1: Get the input from the user
    substring = input("Enter the substring that should not appear:"); 
    #2: Parse input to make sure that there are no zeros and ones 
    if all(ch in "01" for ch in substring): 
       #Create DFA
       newDFA = makeDfa(substring)
        # Build Transitions
       Transitions = Transition.buildTransitions(newDFA, substring)
    #    print("krishna has a shit computer", Transition.buildTransitions(newDFA, substring))
    #    build the GNFA
       thingy = buildGNFA(newDFA, Transitions)
       #print(thingy)
       printThings(thingy)
    #    Transition.printThings(Transitions)
       
    else: 
        print("Invalid string!")
    
        return 

main()


