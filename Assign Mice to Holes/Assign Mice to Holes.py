#Assign Mice to Holes
def assignHoles(m,h,mices,holes):
    mices.sort()
    holes.sort()
    if(m!=h):
        return -1
    max=0
    for i in range(m):
        if(max<(mices[i]-holes[i])):
            max=(mices[i]-holes[i])
    
    return max
        
        
    
print("Enter the number of mices:")    
mices=[int (i) for i in input().split()]
print("Enter the number of holes:")
holes=[int (i) for i in input().split()]
m=len(mices)
h=len(holes)
min_time=assignHoles(m,h,mices,holes)
print("min_time is: ",min_time)


    
