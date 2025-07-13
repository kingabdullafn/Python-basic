start=int(input("enter the starting range "))
end=int(input("enter the ending range"))

for num in range(start,end+1):
    for i in range(2,num):
        if num%i==0:

            break
    else:
            print(num,"it is prime")