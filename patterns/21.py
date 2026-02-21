## Hollow Rectangle (The Boundary Logic)



N = int(input())

for i in range(N):
    for j in range(N):
        # If it's the first row, last row, first column, or last column -> Print *
        if i == 0 or i == N - 1 or j == 0 or j == N - 1:
            print("*", end="")
        else:
            print(" ", end="")  # Otherwise, hollow space
    print()