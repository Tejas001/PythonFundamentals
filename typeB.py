# 1 - c,d,f
# 2 - print(temp) , b is not defined and print(a,b), print(a,b,c), x=4, print(X==X), else is keyword
# 3 - i) 15, 13,22  ii) (2,3,6) , (11,3,33)  iii) (7,49)
# 4 - i) IndentationError ii) TypeError iii) TypeError
# 5 - (4, 6) 4
# 6 - -6 12
# 7 - i) 12,6,24 ii)2 3 None
# 8 - (1 2 3) (25 13 16)
# 9 - 

# prime number

def primenum(n):
    status=False
    if n>1:
        for i in range(2,n):
            if (n%i) == 0:
                status=True
                break
    if status:
        print(f'{n} is composite number')
    else:
        print(f'{n} is prime number')
n = int(input("Enter a number: "))
primenum(n)
