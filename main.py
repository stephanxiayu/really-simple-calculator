from art import logo

print(logo)

def add(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

def multi(n1, n2):
    return n1*n2

def divid(n1, n2):
    return n1/n2

dictonary={
    "+":add,
    "-":sub,
    "*":multi,
    "/":divid
    }

function= dictonary["*"]

num1=int(input("Nummer 1?: "))

for key in dictonary:
    print(key)
operation_symbol=input("wähle eins der + - * / operation: ")   
num2=int(input("Nummer 2?: "))

calculation_function=dictonary[operation_symbol]
result=calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {result}")