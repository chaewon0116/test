def div (a,b):
    return a/b
str=input("문자열 입력: ")
def reverse(str):
    return str[::-1]

n=int(input("n: "))
def is_even(n):
    return n%2==0


a=int(input("a:"))
b=int(input("b:"))
op=int("op:")


if op =='+': print(add(a,b))
elif op == '-': print(sub(a,b))
elif op == '*': print(mul(a,b))
elif op =='/': print(div(a,b))