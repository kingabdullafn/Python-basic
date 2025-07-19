#Take input 
print("Half Pryamid Pattern of stars (*):")
n = int(input("enter number of rows"))
#outer loop to handle numbers of rows
for i in range (n):
    #inner loop to handle number of columns
       for j in range (i+1):
       #display result
         print("*", end="")
       print()   