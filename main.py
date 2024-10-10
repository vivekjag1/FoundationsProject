from DFA import DFA
from State import State
from Transition import Transition
from Transition import printThings
from GNFA import GNFA
import re

acc = ""

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
     #     print(i, "accept: ", thisState.isAccept)

         if(not thisState.isAccept and (not thisState.isStart)): 
              transitions[i].append(None)
    
         if(thisState.isAccept):
              #print("At state at index", i)
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

                if(allTransitions[i][0] != None and allTransitions[i][0] != "None"):
                     ind_1 = allTransitions[i][0].toDict()
                if(allTransitions[i][1] != None and allTransitions[i][1] != "None"):
                     ind_2 = allTransitions[i][1].toDict()
                if(allTransitions[i][2] != None and allTransitions[i][2] != "None"):
                     ind_3 = allTransitions[i][2].toDict()
                print(f"q{i}        ",ind_1, ind_2, ind_3)

def crushGNFA(states, transitions, length):
     accum = ""
     while(len(states) != 2):
          pivot = states[1]
          currTrans = transitions[1]
          isLoop = idLoop(pivot, currTrans)
          if(length != len(states)):
               pivot.origin = [accum]
          begin = "(" + parseFunc(pivot.origin) + ")"
          looper = ""
          if(idLoop(states[1], transitions[1]) != []):
               print(idLoop(states[1], transitions[1]))
               send = []
               send.append(idLoop(pivot, currTrans)[1])
               looper = "(" + parseFunc(send) + "*" + ")"
          else:
               looper = ""
          
          end = "(" + parseFunc(states[1].dest) + ")"
          
          accum = "(" + begin + looper + end + ")" + "U"
          newTrans = deleteStateInstance(states[1].name, transitions, states).copy()
          
          print("ACCUM IS : ", accum)
          del states[1]
          del transitions[1]
          # print("NEW TRANS")
          printStateInfo(newTrans)
     print("ACCUM IS : ", accum[:-1])
     return "Final: " + accum[-1]

def parseFunc(arr):
     final_string = ""
     for i in range(len(arr)):
          final_string += "U" + str(arr[i])
     # final_string[0] = ""
     # print(final_string)
     return final_string.replace("U", "", 1)

def findNextTrans(state, transition):
     arr = ['0', '1', 'None']
     currentStateInd = findInt(state.name)
     for i in range(len(transition)):
          if(findInt(transition[i].name) > currentStateInd):
               return arr[i]
     return "None"

def findInt(string):
     if(re.search(r'\d+', string) == None):
          return "None"
     return int(re.search(r'\d+', string).group())

# Deletes all instances of a transition to the state being deleted in the transition table
def deleteStateInstance(stateName, transitions, states):
     newTrans = transitions.copy()
     # Replaces all instances of the state in the transition table unless its the start state
     for i in range(len(newTrans)):
          for x in range(3):
               if(newTrans[i][x] != "None"):
                    if(i == 0 and newTrans[i][x].name == stateName):
                         newTrans[i][x] = states[i + 2]
                         
                    elif(i > 0 and newTrans[i][x].name == stateName):
                         newTrans[i][x] = "None"  

               elif(newTrans[i][x] == "None"):
                    continue

     return newTrans

# These three functions are ABSOLUTELY ESSENTIAL TO GENERATING A REGEX FROM OUR CODE
def idLoop(state, transition):
     arr = ["0", "1", "E"]
     arrFinal = []
     currName = state.name
    #  print("Current Name", currName)
     for i in range(3):
          # print("I hate lfe ", transition[i].name")
          # print(f"transition {i} is {transition[i]}")
          
          if(transition[i] != "None" and currName == transition[i].name):
            #    print("Transition index ", transition[i].name)
               arrFinal.append(currName)
               arrFinal.append(arr[i]) #Need this
               return arrFinal
     return []

def findIncoming(state, transitions):
     currStateName = state.name
     finalArr = []
     incoming = []
     indexes = []

     for i in range(len(transitions)):
          # If not the current state and you find the current state name that means there is a transition to it
          # This is for incoming finding which states transition to the current state
          for x in range((3)):
               
               if(transitions[i][x] == None):
                    transitions[i][x] = "None"
               elif(transitions[i][x] != "None" and transitions[i][x].name == currStateName and (i != findInt(currStateName))):
                    incoming.append(f"q_{i}")
                    if(x == 2):
                         indexes.append("E")
                    else:
                         indexes.append(x)
     finalArr.append(incoming)
     finalArr.append(indexes)

#     print(finalArr)
     return finalArr
               
def findOutgoing(state, transitions):
     currStateName = state.name
     # print("find outgoing curr state name ", currStateName)
     finalArr = []
     outgoing = []
     indexes = []
     for i in range(3):
          if(findInt(currStateName) != "None"):
               if(transitions[findInt(currStateName)][i] != "None" and transitions[findInt(currStateName)][i].name != currStateName):
                    # outgoing.append(transitions[findInt(currStateName)][i].name)
                    if(i == 2):
                              indexes.append("E")
                              continue
                    else:
                         outgoing.append(transitions[findInt(currStateName)][i].name)
                         indexes.append(i)
              
               if(findInt(currStateName) == "None"):
                    if(transitions[0][i] != "None" and transitions[0][i].name != currStateName):
                         # outgoing.append(transitions[findInt(currStateName)][i].name)
                         if(i == 2):
                                   indexes.append("E")
                                   continue
                         else:
                              outgoing.append(transitions[findInt(currStateName)][i].name)
                              indexes.append(i)
     
     finalArr.append(outgoing)
     finalArr.append(indexes)
     
     # print(finalArr)
     
     return finalArr

# End of essential functions

# This is used to fill out the origin and dest values of each state
def fillInOut(transitions, states):
     # print("Fill in out")
     # print(states)
     for i in range(len(states)):
          states[i].origin = findIncoming(states[i], transitions)[1]
          states[i].dest = findOutgoing(states[i], transitions)[1]
     return
     
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
     #   print("fml" ,newGNFA.states[1])

       fillInOut(newGNFA.transitions, newGNFA.states)
     #   print("Fill in out finished")
     #   This returns the indexes (the values 0, 1, or E) that point to this state
       for i in range(len(newGNFA.states)):
           print(f"ORIGIN for {newGNFA.states[i].name}: ", newGNFA.states[i].origin)
          #  print(f"LOOP for {newGNFA.states[i].name}: ", idLoop(newGNFA.states[i], newGNFA.transitions))
           print(f"OUT for {newGNFA.states[i].name}: ", newGNFA.states[i].dest)
           
       #this prints the current states and thier transitions       
       printStateInfo(newGNFA.transitions)
       #call crush GNFA -> this is where the resulting regex is printed
       return crushGNFA(newGNFA.states, newGNFA.transitions, len(newGNFA.states))

     #   Checking parse transitions
     #   print("Incoming")
     #   findIncoming(newGNFA.states[1], newGNFA.transitions)
    else: #the case that something other than 0 and 1 were added
        print("Invalid string!")
        return  #exit
main()


