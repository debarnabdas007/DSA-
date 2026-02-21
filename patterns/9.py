N = int(input())

#Combination of Two opposite pyramid

# Pyramid 1
for i in range(0,N):
    #space
    for j in range(N-i-1):
        print(" ",end="")
    #stars    
    for k in range(2*i+1):
        print("*", end="") 
    #space  
    for l in range(N-i-1):
        print(" ", end="")    
    print()    

# Pyramid 2
for i in range(0,N):
    #space
    for j in range(i):
        print(" ",end="")
    #stars    
    for k in range(2*N-2*i-1):
        print("*", end="") 
    #space  
    for l in range(i):
        print(" ", end="")    
    print()    

