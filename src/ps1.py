# Exercise 1
"""
name = str(input("Enter your name: "))
print(f"Welcome {name}!")
"""

# Exercise 2
"""
firstName = str(input("Enter your first name: "))
lastName = str(input("Enter your last name: "))
age = int(input("Enter your age: "))
print(f"Welcome Mr. {firstName} {lastName}, your age is {age}")
"""

# Exercise 3
"""
firstNumber = float(input("Enter first number: "))
secondNumber = float(input("Enter second number: "))
print(f"{firstNumber:.1f} + {secondNumber:.1f} = {(firstNumber + secondNumber):.1f}")
print(f"{firstNumber:.1f} - {secondNumber:.1f} = {(firstNumber - secondNumber):.1f}")
print(f"{firstNumber:.1f} * {secondNumber:.1f} = {(firstNumber * secondNumber):.1f}")
print(f"{firstNumber:.1f} / {secondNumber:.1f} = {(firstNumber / secondNumber):.1f}")
print(f"{firstNumber:.1f} % {secondNumber:.1f} = {(firstNumber % secondNumber):.1f}")
"""

# Exercise 4
"""
base = 10.0
height = 8.0
area = round(float((base * height) / 2), 1)
print(f"A triangle with a base of {base} meters and a height of {height} meters has an area of {area} meters squared!")
"""

# Exercise 5
"""
firstMonthSalary = round(float(input("Enter salary of the first month: ")), 2)
secondMonthSalary = round(float(input("Enter salary of the second month: ")), 2)
thirdMonthSalary = round(float(input("Enter salary of the third month: ")), 2)
averageSalary = (firstMonthSalary + secondMonthSalary + thirdMonthSalary) / 3
print(f"The average salary is: {averageSalary:.2f}")
"""

# Exercise 6
"""
inputFahrenheit = float(input("Enter the temperature in Fahrenheit: "))
convertedToCelsius = round((inputFahrenheit - 32) * 5/9)
print(f"The temperature in Celsius: {convertedToCelsius:.1f}")
"""


# Exercise 7
"""
monthlySalary = 25000
costPerMonth = 19000
costPerYear = 480
totalAfterYear = ((monthlySalary - costPerMonth) * 12) - costPerYear
print(f"With a monthly salary of {monthlySalary}kr and a cost per month of {costPerMonth}kr and a cost per year of {costPerYear}kr, the total after a year will be {totalAfterYear}kr")
"""

# Exercise 8
"""
savedMoney = 20000
ticketCost = 5000
daysInHotel = 10
hotelCostPerDay = 550
costOnFood = 2000
transportCost = 1750
giftsCost = 5000
amountLeft = savedMoney - (ticketCost + (daysInHotel * hotelCostPerDay) + costOnFood + transportCost + giftsCost)
print(f"The amount left is {amountLeft}kr")
"""

# Exercise 9
"""
laptopCost = 9900 * 0.85
printerCost = 2800 * 0.9
print(f"The cost is {laptopCost + printerCost}")
"""

# Exercise 10
"""
pricePerTicket = int(input("Enter the price for a normal air ticket: "))
priceForSon = pricePerTicket*0.7
priceForDaughter = pricePerTicket*0.4
totalPriceForFamily = (pricePerTicket*2+priceForSon+priceForDaughter)
print(f"The total price for normal air tickets, for the whole family is: {totalPriceForFamily:.1f}")
"""