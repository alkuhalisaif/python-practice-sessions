# Getting a table
"""def get_table(you: int, friend: int) -> int:
    if you>=8 or friend>=8:
        return 2
    elif you<=2 or friend<=2:
        return 0
    else:
        return 1
print(get_table(5, 10))
print(get_table(5, 2))
print(get_table(5, 5))"""

# Caught speeding
"""def caught_speeding(speed: int, isBirthday: bool) -> int:
    if isBirthday:
        speed -= 5
    if speed<=80:
        return 0
    elif speed>=81 and speed<=100:
        return 1
    elif speed>=101:
        return 2
print(caught_speeding(80, False))
print(caught_speeding(85, False))
print(caught_speeding(85, True))"""

# Find the smallest item in a list of numbers using a loop
"""listOfNumbers = [5, 3, 123, 524, 60424, 200]
temp = listOfNumbers[0]
for number in listOfNumbers:
    if number<temp:
        temp=number
print(temp)"""

# Guessing Game revisited
"""import random as random
randomNumber = random.randint(0,100)
hasFoundNumber = False
guess = -1
while not hasFoundNumber:
    guess = int(input("Guess the number (0-100): "))
    if guess==randomNumber:
        hasFoundNumber = True
        print(f"The number was {randomNumber} and you've found it!!!")
    elif guess<randomNumber:
        print("Higher!")
    else:
        print("Lower!")"""


# Count even elements
"""def count_evens(list):
    evenNumberCount = 0
    for number in list:
        if number%2==0:
            evenNumberCount += 1
    return evenNumberCount
print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5]))"""

# Sum of Even Numbers
"""def sumOfEvenNumbers(list):
    sum = 0
    for number in list:
        if number%2==0 and number<20 and number>1:
            sum += number
    return sum
print(sumOfEvenNumbers([4, 6, 16]))"""

# Break and Continue
"""for i in range(1, 11):
    if i%3==0:
        continue
    elif i==7:
        break
    else:
        print(i)"""

# Loop and function
"""def triangle(start: int, end: int, char: str):
    for i in range(start, end+1):
        print(char*i)

triangle(2, 5, "+")
triangle(3,5,"@")"""


# Fibonacci numbers
"""def fiboFromIndex(index):
    fiboList = list()
    fiboList.append(0)
    fiboList.append(1)
    if index!=1 and index!=0:
        for i in range(2, index+1):
            numberAtIndex = (fiboList[i-1] + fiboList[i-2])
            fiboList.append(numberAtIndex)
    return fiboList[index]
print(fiboFromIndex(7))"""

# List and Tuple Operations
"""list1 = [1, 2, 3, 4, 5, 1000, "YOOO"]
def listToTuple(list):
    return tuple(list)
print(list1)
print(listToTuple(list1))
print(len(listToTuple(list1)))
print(listToTuple(list1)[2])"""

# List of Dictionaries (Structured Data)
"""products = [
    {"name": "Apple", "price": 20, "quantity": 5},
    {"name": "Banana", "price": 15, "quantity": 8},
    {"name": "Orange", "price": 30, "quantity": 3},
]
tempForPrice = 0
mostExpensiveProductName = ""
for product in products:
    if product["price"] > tempForPrice or tempForPrice ==0:
        tempForPrice = product["price"]
        mostExpensiveProductName = product["name"]
print(f"Most expensive product is {mostExpensiveProductName} and it costs {tempForPrice}kr")
tempForPrice = 0
leastExpensiveProductName = ""
for product in products:
    if product["price"] < tempForPrice or tempForPrice==0:
        tempForPrice = product["price"]
        leastExpensiveProductName = product["name"]
print(f"Least expensive product is {leastExpensiveProductName} and it costs {tempForPrice}kr")
totalValueSum = 0
for product in products:
    print(f"The total value of {product["name"]} is {product["price"] * product["quantity"]}kr")
    totalValueSum += (product["price"] * product["quantity"])
print(f"The total value sum of all products is {totalValueSum}kr")"""