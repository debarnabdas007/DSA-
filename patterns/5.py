N = int(input())
'''
for i in range(0,N):
    for j in range(N, i, -1):
        print("*", end="")

    print()    
'''

# Prefered method:  

for i in range(0,N):
    for j in range(N-i):
        print("*",end="")
    print()    
