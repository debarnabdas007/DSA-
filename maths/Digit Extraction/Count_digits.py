N = 7789
count = 0
while N > 0:
    digit= N % 10
    # print(digit)
    count = count + 1
    N = N // 10

print(count)
    