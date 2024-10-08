from DFA import DFA
from State import State
from Transition import Transition
from Transition import printThings
from GNFA import GNFA
import re
def makeDfa( substring):
        numStates = len(substring) + 1
        states = []
        for i in range(numStates): 
            if (i == 0): 
                states.append(State((f"q_{i + 1}"), True, False, 'self', 'self' )); 
            elif (i!=numStates -1): 
                states.append(State((f"q_{i + 1}"), False, False, 'self', 'self' )); 
            else: 
                states.append(State((f"q_{i + 1}"), False, True, 'self', 'self' )); 

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
    state = State((f"q_{0}"), True, False, [None], [states[1]])
    states.insert(0, state)
    # Edit old start state to now make it normal state
    oldStart = states[1]
    oldStart.isStart = False
    states[1] = oldStart
    # Make new transition for new start state
    transitions.insert(0, [None, None, states[1]])

    #build new accept state
    newStates = [] 
    for j in range(len(states)):
         if(j == 0 or j == len(states) - 1):
              continue
         else:
              newStates.append(states[j])
    # Will add every state pointing to accept except the start and original accept state
    newAccept = State("q_accept", False, True, newStates, [None])
    states.append(newAccept)

    #iterate through the list of transitions and if we get to an accept state, make it non accpeting and add transition to this new state 
    for i in range(len(states) - 1): 
         
         thisState = states[i]
         print(i, "accept: ", thisState.isAccept)

         if(not thisState.isAccept and (not thisState.isStart)): 
              transitions[i].append(None)
    
         if(thisState.isAccept):
              print("At state at index", i)
              thisState.isAccept=False
              transitions[i].append(newAccept)
              
        #  if(i == len(states) -1): 
        #       transitions[i].append(None)
    retGNFA = GNFA(states, transitions)
    return retGNFA

        
def printStateInfo(allTransitions):
    print("Curr State  |  0  |   1  |  E  ")
    for i in range(len(allTransitions)):      
                ind_1 = "None"
                ind_2 = "None"
                ind_3 = "None"
                if(allTransitions[i][0] != None):
                     ind_1 = allTransitions[i][0].toDict()
                if(allTransitions[i][1] != None):
                     ind_2 = allTransitions[i][1].toDict()
                if(allTransitions[i][2] != None):
                     ind_3 = allTransitions[i][2].toDict()
                print(f"q{i}        ",ind_1, ind_2, ind_3)


        
def crushGNFA(states, transitions):
     acc = ""
     if(len(states) == 2):
          return "(" + acc + ")*"
     pivot = states[1]
     currTrans = transitions[1]
     arr = idLoop(pivot, currTrans)
    #  Has loops
     if(arr != "Fail"):
          acc = acc + arr[1] + "* "
          print("Accumulate this shit asshole " + acc)
        #   No loops
     if(arr == "Fail"):
        #    In the case of failure you need to find the pointer to the next state
           acc = acc + findNextTrans(pivot, currTrans)
           
           print("Accumulate this shit asshole 2 " + acc)
     
     del states[1]
     del transitions[1]
     crushGNFA(states, transitions)

def idLoop(state, transition):
     arr = ["0", "1", "E"]
     arrFinal = []
     currName = state.name
    #  print("Current Name", currName)
     for i in range(len(transition)):
        #   print("I hate lfe", currName, transition[i].name)
          if(currName == transition[i].name):
            #    print("Transition index ", transition[i].name)
               arrFinal.append(currName)
               arrFinal.append(arr[i])
               return arrFinal
     return "Fail"


def findNextTrans(state, transition):
     arr = ['0', '1', 'None']
     currentStateInd = findInt(state.name)
     for i in range(len(transition)):
          if(findInt(transition[i].name) > currentStateInd):
               return arr[i]
     return "Nah"
          

def findInt(string):
     return int(re.search(r'\d+', string).group())
     
def main(): 
    #1: Get the input from the user
    substring = input("Enter the substring that should not appear:"); 
    #2: Parse input to make sure that there are no zeros and ones 
    if all(ch in "01" for ch in substring): 
       #Create DFA
       currentStates = makeDfa(substring)
       # Build Transitions
       Transitions = Transition.buildTransitions(currentStates, substring) #returns an array of arrays where each index of the array is in the form [state to move if 0 is read, state to move to if 1 is read]4
       #build GNFA attaches a new start and accept state to the exiting dfa
       newGNFA = buildGNFA(currentStates, Transitions)
       #this prints the current states and thier transitions       
       printStateInfo(newGNFA.transitions)

       crushGNFA(newGNFA.states, newGNFA.transitions)
    else: #the case that something other than 0 and 1 were added
        print("Invalid string!")
        return  #exit
main()


