N = int(input())
# Pyramid 
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
