
#Básico
def add(a, b):
    result = a + b
    print(f"Adding {a} and {b} results in {result}")

def subtract(a, b):
    result = a - b
    print(f"Subtracting {b} from {a} results in {result}")

def multiply(a, b):
    result = a * b
    print(f"Multiplying {a} and {b} results in {result}")

def divide(a, b):
    try:
        result = a / b
        print(f"Dividing {a} by {b} results in {result}")
    except ZeroDivisionError:
        print(f"Error: Cannot divide {a} by zero! Division by zero is undefined.")


#Desafio;
def equation_on_two_degree(a, b, c):
	print("gotta solve the delta") #TODO: delta e bhaskara.