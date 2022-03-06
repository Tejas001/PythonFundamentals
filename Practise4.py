# #  Program to 3 digit number in form <n(n+1)(n+2)>
# number = int(input("Enter a number in range 1-7: "))
# number_of_digit_to_print = int(input("Enter a number: "))
# print(number,end="")
# for n in range(1,number_of_digit_to_print):
#     print(number+n,end="")

# Program to read 3 numbers and swap first 2 variables with sums of first and second, second and third respectively
one = int(input("Enter a first number: "))
two = int(input("Enter a second number: "))
three = int(input("Enter a third number: "))
print("Original numbers: ",one, two, three)
print()
one = one+two
two = two+three
print("Swapped numbers: ",one, two, three)