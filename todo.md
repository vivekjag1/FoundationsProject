## Todo 
1. Do GNFA rip recursivley 


## Steps
1. let K = num states
if k = 2
    Check for start and accept state
    Return the single transition between the two 
else 
    select the first state in the list of states 
        This state can't be a start or accept state 
        Remove the state using our rules 
            If there is a loop: (char that caused loop)* 
            No loop: take the char 
            If there is more than one char, then use a union 
        