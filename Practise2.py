# Area of circle
# radius = float(input("Enter radius of circle: "))
# pie=3.14
# area_circle = pie*radius*radius
# print(f'Area of circle is {area_circle}')

# Print average marks of subjects (dynamic)
no_of_subject = int(input("Enter number of subject: ")) 
sum = 0

for num in range(no_of_subject):
    subject_marks = int(input("Enter marks for subject: "))
    sum += subject_marks

average_marks = sum/no_of_subject
print(f"The average marks of {no_of_subject} is {average_marks}")

# Print average marks of subjects (static)
# sub1=int(input("Enter marks of subject1: "))
# sub2=int(input("Enter marks of subject2: "))
# sub3=int(input("Enter marks of subject3: "))
# sub4=int(input("Enter marks of subject4: "))
# sub5=int(input("Enter marks of subject5: "))
# average_marks = (sub1+sub2+sub3+sub4+sub5)/5
# print(f"The average marks = {average_marks}")