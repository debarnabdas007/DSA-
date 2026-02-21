N = int(input())

for i in range(N):
    # 1. Left Spaces
    for j in range(N - i - 1):
        print(" ", end="")



    # 2. Letters (The Peak Logic)
    ch = ord('A')
    breakpoint = (2 * i + 1) // 2  # Find the exact middle
    
    for k in range(2 * i + 1):
        print(chr(ch), end="")
        if k < breakpoint:
            ch += 1  # Go up: A -> B -> C
        else:
            ch -= 1  # Go down: C -> B -> A

          
            
    # 3. Right Spaces (Optional, but included for structure)
    for l in range(N - i - 1):
        print(" ", end="")
        
    print()