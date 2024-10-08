class State: 
    '''
    name -> string 
    isStart -> boolean 
    isAccept -> boolean 
    origin -> list of states that can reach this state
    dest -> list of states that can be reached from this state
    '''
    def __init__(self, name, isStart, isAccept, origin, dest): 
        self.name = name 
        self.isStart = isStart
        self.isAccept = isAccept
        self.origin = origin
        self.dest = dest
    def toDict(self):
        return self.name
        
        # print("Is start?: ", self.isStart)
        # print("Is Accept?: ", self.isAccept)
        # print("Origin", self.origin)
        # print("Dest", self.dest)
