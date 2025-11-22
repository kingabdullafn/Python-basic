try:
    n = int(input("Enter a number:"))
except ValueError:
    print("Please enter a valid interger.")
    exit()
odd_numbers = [i for i in range (1,n) if i % 2 != 0]
even_numbers = [i for i in range (1,n)if i % 2 == 0]
print("Odd Numbers:",odd_numbers)
print("Even Numbers:", even_numbers)
fruits = ["Durian", "lychee", "Banana", "Pineapple"]
updated_fruits = [fruit.capitalize() for fruit in fruits]
print("Upadated fruits:",updated_fruits)
