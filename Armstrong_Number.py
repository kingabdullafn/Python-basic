# Take input from the user
num = int(input("Enter Number: "))

# initialize sum
sum =0

# find the sum of the cube of each digit 
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10


# display the result
if num == sum:
    print(num,"is an armstrong number")
else:
    print(num,"is not an Armstrong number")