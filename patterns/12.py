# Number Crown Pattern

n = int(input())

for i in range(1,n+1):
    # no.
    for j in range(1,i+1):
        print(j, end="")
    # space
    for k in range(0, 2*n-2*i):
        print(" ", end="")
    #no.
    for l in range(i, 0, -1):
        print(l, end="")
    print()    