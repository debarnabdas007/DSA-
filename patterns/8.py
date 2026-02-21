N = int(input())
# Pyramid 
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
