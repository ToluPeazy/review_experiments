'''
#################################################################
This function defines how the universe set and set of subsets are 
drawn from the datafile.
##################################################################
'''
def read_datafile(path):
    U = []
    #U = set()
    Sets = []
    
    with open((file_path), "r") as file:
        i = 0
        for line in file:
            Set = []
            #if(i == 0):
            #    for num in line.strip().split(","):
            #        U.append(int(num))
            #else:
            for num in line.strip().split(" "):
                Set.append(int(num))
            Sets.append(Set)
            

            if(i == 0):
                for num in line.strip().split(" "):
                    U.append(int(num))
            else:
              for num in line.strip().split(" "):
                newnum = int(num)
                if newnum not in U:
                  U.append(newnum)
            i+=1
                
    return Sets, U