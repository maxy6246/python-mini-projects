def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print("Calculator")
print("1 Add\n2 Subtract\n3 Multiply\n4 Divide")

choice = int(input("Enter choice: "))
a = float(input("First number: "))
b = float(input("Second number: "))

if choice == 1:
    print(add(a, b))
elif choice == 2:
    print(subtract(a, b))
elif choice == 3:
    print(multiply(a, b))
elif choice == 4:
    print(divide(a, b))
