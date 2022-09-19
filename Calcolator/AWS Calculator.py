
print("---------------------------------")
operations=["+","-","*","/"]

for i in range(4):
    print(f"for {operations[i]} enter {i}")
print("---------------------------------")

operation=int(input("enter the number associated with the operation"))
print("---------------------------------")

print(f"you chose {operations[operation]}")
print("---------------------------------")

first=int(input("enter the first number"))
second=int(input("enter the second number"))
print("---------------------------------")

def f():
    if operation == 0:
        print(first+second)
    elif operation == 1:
        print(first-second)
    elif operation == 2:
        print(first*second)
    elif operation == 3:
        print(first/second)
    else:
        print("you entered a wrong number for the operation")

f()
