# Program to convert centimeter to feet and inches
# height = float(input("Enter height in centimeter: "))
# height_in_inch = height / 2.54
# feet = height_in_inch // 12
# inch = height_in_inch % 12
# print(f"Height in centimeter is {height}, in feet {feet} and in inches {inch}")

# Program to read n and print n2, n3 and n4
# number = int(input("Enter a number: "))
# power_number = int(input("Enter a number greater than 1: "))
# d = {}
# for n in range(2,power_number+1):
#     d[n] = number ** power_number

# print((f"n is {number} which is to be power till {power_number} and its output is {d}"))
# # print(f"n is {n}, n2 is {n**2}, n3 is {n**3} and n4 is {n**4}")

# Program to find area triangle
# height_traingle = float(input("Enter height of triangle: "))
# base_triangle = float(input("Enter base of triangle: "))
# area = (height_traingle*base_triangle)/2
# print(f"Area of triangle is {area}")

# Program to compute simple and compound interest
from tkinter.tix import InputOnly


# principal = int(input('Enter Principal amount: '))
# rate_of_interest = float(input("Enter ROI: "))
# time = int(input("Enter time: "))
# SI = (principal*rate_of_interest*time)/100
# CI = principal*((1+(rate_of_interest/100))**time)-principal
# print(f"Simple Interest is {SI} and Compound Interest is {CI}")

# Program to print first 5 multiples
# n=5
# number = int(input('Enter a number: '))
# for i in range(1,n+1):
#     print(f"The number {number} and multiple of {i} is {number * i}")

# Program to print name,class, age of student
name = input("Enter your name: ")
classs = int(input("Enter in which class are you studying: "))
age = int(input("Enter your age: "))
print("Name:",name,end=", ")
print("class:",classs,end=", ")
print("Age:",age)
print()
print()
print("Name: ",name)
print("class: ",classs)
print("Age: ",age)
print()
print()
print("Name:",name + ", " + "class:",str(classs) + ", " + "Age:",str(age))