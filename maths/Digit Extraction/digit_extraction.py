'''The Mission:
Write a short Python script that takes N = 7789 and prints its digits one by one, from right to left (Output should be: 9, 8, 7, 7).
'''


N = 7789
while N > 0:
    digit= N % 10
    print(digit)
    N = N // 10
    