# Q1: Range Check
"""
number = float(input("Type a number: "))
if (number >= 5 and number <= 10):
    print("Yes!")
else:
    print("No!")
"""

# Q2: Guessing Game
"""
fixedNumber = 7
number = float(input("Guess the number: "))
if number<fixedNumber:
    print("Higher!")
elif number>fixedNumber:
    print("Lower!")
else:
    print("You got it!")
"""


# Q3: Odd and Divisible
"""number = float(input("Guess the number: "))
if number%2==1 and number%3==0:
    print("Yes!")
else:
    print("No!")"""

# Q4: Calculator Application
"""switchBoard = """
#1 for addition          2 for subtraction
#3 for multiplication    4 for division
#5 for power             6 for remainder
"""
print(switchBoard)
choice = int(input("Enter your choice: "))
firstValue = int(input("Enter first value: "))
secondValue = int(input("Enter second value: "))
if choice==1:
    print(f"{firstValue} + {secondValue} = {firstValue + secondValue}")
elif choice==2:
    print(f"{firstValue} - {secondValue} = {firstValue - secondValue}")
elif choice==3:
    print(f"{firstValue} * {secondValue} = {firstValue * secondValue}")
elif choice==4:
    print(f"{firstValue} / {secondValue} = {firstValue / secondValue}")
elif choice==5:
    print(f"{firstValue} ** {secondValue} = {firstValue ** secondValue}")
elif choice==6:
    print(f"{firstValue} % {secondValue} = {firstValue % secondValue}")
else:
    print("Something went wrong")"""

# Q5: Create and Manipulate a List
"""myList = [999, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(myList)
myList[0] = 1
print(myList)
myList.append(100)
print(myList)
myList.pop()
print(myList)
myList.sort(reverse=True)
print(f"Final list: {myList}")"""

# Q6: Slicing Lists
"""listPrimes = [2, 3, 5, 7, 11, 13, 17, 19]
print(listPrimes)
print(listPrimes[:4])
print(listPrimes[-3::])
print(listPrimes[::-1])
print(listPrimes[::2])"""

# Q7: List Operations with User Input
"""number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))
number4 = int(input("Enter fourth number: "))
number5 = int(input("Enter fifth number: "))
listOfNumbers = [number1, number2, number3, number4, number5]
listOfNumbers.sort()
print(f"{number1} + {number2} + {number3} + {number4} + {number5} = {number5 + number4 + number3 + number2 + number1}")
print(f"Maximum: {listOfNumbers[-1:]}")
print(f"Minimum: {listOfNumbers[:1:]}")"""

"""list1 = list()
for i in range(5):
    num = int(input("Enter a number: "))
    list1.append(num)
print(f"Original list: {list1}")
print(sum(list1))
print(max(list1))
print(min(list1))
x = 0
for i in list1:
    list1[x] = (i * 2)
    x += 1
print((f"List multipled by 2 at every index: {list1}"))"""

# Q8: String Manipulation
"""string1 = str(input("Enter a string: "))
print(len(string1))
print(string1[::-1])
if string1 == string1[::-1]:
    print("It's a palindrome")
else:
    print("Not a palindrome")"""

# Q8: String Slicing
"""String1 = "Python is Amazing!"
print(String1[:6])
print(String1[10:-1])
print(String1.upper())
String2 = String1
String2 = String2.replace("Amazing", "Fun")
print(String2)"""

# Q9: String to List Conversion
"""sentence = str(input("Write a sentence here: "))
wordList = sentence.split()
wordCount = len(wordList)
print(f"List: {wordList}, Total Count: {wordCount}")"""

# Q10: Create and Update a Dictionary
"""dictionary1 = {"Saif": 100, "Aiman": 200, "Essa": 500}
print(dictionary1)
dictionary1["Saif"] = 200
print(dictionary1)
dictionary1["Hakim"] = 99999
print(dictionary1)"""

# Q11: Create and Update a Dictionary
"""student = {"name": "John", "age": 20, "grade": "B"}
print(f"age = {student.get("age")}")
student["grade"] = "A"
student["major"] = "Computer Science"
print(student)"""

# Q12: Searching in a Dictionary
"""ages = {"Alice": 25, "Bob": 22, "Carol": 27}
name1 = str(input("Enter your name: "))
if ages.get(name1) == None:
    print("Not found")
else:
    print("Found")"""

# Q13: List of Dictionaries (Structured Data)
"""products = [
    {"name": "Apple", "price": 10, "quantity": 5},
    {"name": "Banana", "price": 5, "quantity": 8},
    {"name": "Orange", "price": 7, "quantity": 3},
]
Total = 0
for product in products:
    Total += (product["price"] * product["quantity"])
    print(f"Added amount: {product["price"] * product["quantity"]}")
print(f"The total is: {Total}")"""

# Q14: Boolean Expressions
"""is_raining = True
is_cold = False
if is_raining and is_cold:
    print("It is both raining, and cold.")
elif is_raining or is_cold:
    print("It is either raining, or cold.")
elif not is_raining:
    print("It's not raining nor cold")"""

# Q15: Tuple Unpacking:
"""person = ("Alice", 25, "Engineer")
name = person[0]
age = person[1]
profession = person[2]
String1 = f"{name} is a {age}-year-old {profession}"
print(String1)"""