def allSame(substring): 
        acc = True
        prevChar = ''
        for i in range(len(substring)): 
            if(i ==0): 
                prevChar = substring[i]
            else: 
                if(substring[i] != prevChar): 
                    acc = False
                    return acc
        return acc 
def allSameToIndex(substring, toIndex): 
         acc = True
         prevChar = ''
         for i in range(toIndex): 
            if(i ==0): 
                    prevChar = substring[i]
            else: 
                    if(substring[i] != prevChar): 
                        acc = False
                        return acc
            return acc 