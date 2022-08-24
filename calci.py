
from art import logo
# defining operations
def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

# symbol and names wrt to them
operations={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}

print(logo)
print("Welcome to CALCULATOR program ")
def calculation():
    end = False
    num1=float(input("What's your first number? "))
    while not end:      # to perform repeatedly with outcoming result
        print("Choose an operations from below list: ")
        for keys in operations:
            print(keys)
        opeartion_selected=input("Your operation: ")
        num2=float(input("What's your next number? "))
        function=operations[opeartion_selected]   # getting respective function from dictionary
        res=function(num1,num2)
        print(f"{num1} {opeartion_selected} {num2} = {res}")
        cont=input("Do you want to continue(y for continue & n to reset calculations & s to end)? ")
        if cont=="y":
            num1=res        # num1 becomes result to continue further
            end=False
        elif cont=="n":
            end=True
            calculation()
        elif cont=="s":
            return


calculation()