#Checks if the characters to a certain point of the index are the same if not then we return false
def allSameToIndex(index, substring):
    # print("index is ", index)
    # print("substring is ", substring)
    currChar = substring[0]
    if(allSame(substring)):
        return True
    
    for i in range(index + 1):
        # print("substring i ", substring[i])
        if(currChar != substring[i]):
            return False
    return True

def allSame(substring):
    currChar = substring[0]
    for i in range(len(substring)):
        if(currChar != substring[i]):
            return False
    return True


def printThings(allTransitions):
    for i in range(len(allTransitions)): 
                    for x in range(len(allTransitions[i])): 
                        allTransitions[i][x].toDict()
class Transition: 
    def __init__(self, states): 
        self.states = states
    def buildTransitions(states, substring): 
        allTransitions = []
        for i in range(len(states)):
            next = i + 1
            subnext = i + 1
            changeAllSame = False
            # if(i + 1 != len(states)):
            #     next = i+1

            # if(i + 1 != len(states) - 1):
            #     subnext = i+1
            # When the index is at the last of the string
            if(i == len(states) - 2):
                subnext = len(substring) - 1
            
            # If the value has changed
            if(i > 0):
                if(allSameToIndex(i, substring) != allSameToIndex(i - 1, substring)):
                    changeAllSame = True
            # print("NEXT IS THIS MF ", next)
            # print("SUBNEXT IS THIS MF ", subnext)
            # print("All same? ", allSameToIndex(i, substring))
            # If you know you are at the end of the state array
            # The end of the array will always loop back to itself since it is the accept state
            if(i == len(states) - 1):
                transition = [states[i], states[i]]
                allTransitions.append(transition)
                printThings(allTransitions)
                return allTransitions
            # If all the characters are the same so far
            if(allSameToIndex(i, substring)):
                #  If the next one changes then the transition is 
                 if(substring[i] == '0' and changeAllSame):
                    # print("if allsame 1")
                    transition = [states[i], states[next]]
                    allTransitions.append(transition)
                    # print(transition[0].name, transition[1].name)

                 elif(substring[i] == '1' and changeAllSame):
                    # print("if allsame 2")
                    # print("Subnext is ", subnext)
                    # print("Next index values ", substring[subnext])
                    transition = [states[next], states[i]]
                    allTransitions.append(transition)
                    # print(transition[0].name, transition[1].name)
                
                 elif(substring[i] == '1' and not changeAllSame):
                    # print("if allsame 3")
                    transition = [states[0], states[next]]
                    allTransitions.append(transition)
                    # print(transition[0].name, transition[1].name)
                 
                 elif(substring[i] == '0' and not changeAllSame):
                    # print("if allsame 4")
                    transition = [states[next], states[0]]
                    allTransitions.append(transition)
                    # print(transition[0].name, transition[1].name)
            
            if(not allSameToIndex(i, substring)):
                #  If the next one changes then the transition is 
                 if(substring[i] == '0' and changeAllSame):
                    # print("if allnotsame 1")
                    transition = [states[next], states[i]]
                    allTransitions.append(transition)
                    # print(transition[0].name, transition[1].name)

                 elif(substring[i] == '1' and changeAllSame):
                    # print("if allnotsame 2")
                    transition = [states[i], states[next]]
                    allTransitions.append(transition)
                    # print(transition[0].name, transition[1].name)
                
                 elif(substring[i] == '1' and not changeAllSame):
                    # print("if allnotsame 3")
                    transition = [states[0], states[next]]
                    allTransitions.append(transition)
                    # print(transition[0].name, transition[1].name)
                 
                 elif(substring[i] == '0' and not changeAllSame):
                    # print("if allnotsame 4")
                    transition = [states[next], states[0]]
                    allTransitions.append(transition)
                    # print(transition[0].name, transition[1].name)
        return