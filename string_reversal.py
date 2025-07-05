#Input a word or sentence
string = input("Please enter your own string :")
#code like mandem

string2 = ("")
#Loop for printing in reverse
for i in string:
    string2 = i  + string2

print("/n The orginal string -", string)
print("The reversed string =", string2)