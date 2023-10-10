# Find The greatest common divisor of multiple numbers read from the console.


a=int(input())
b=int(input())
if a*b==0:
    print(a+b)
else:
        while a!=b:
            if a>b:
                a=a-b
            else:
                b=b-a
print (a)