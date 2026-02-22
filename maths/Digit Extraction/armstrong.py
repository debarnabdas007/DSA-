N = int(input())

original = N  # for the very end
temp1 = N  # for the first loop

count = 0
while temp1 > 0:
    digits = temp1 % 10
    count = count + 1 
    temp1 = temp1 // 10
print(f"total no. of digits: {count}")

# for matching
temp2 = original
total_sum = 0

while temp2 > 0:
    digit = temp2 % 10
    total_sum = total_sum + (digit**count)
    temp2 = temp2 // 10
print(f"The sum is: {total_sum}")

if total_sum == original:
    print("TRUE")
else: 
    print("FALSE")       
      