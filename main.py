from art import logo

#Calculator

#Add
def add(n1,n2):
    return n1+n2

#Subtract
def subtract(n1,n2):
    return n1-n2

#Multiply
def multiply(n1,n2):
    return n1*n2

#Divide
def divide(n1,n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    print(logo)
    calculate_finished = False
    num1 = float(input("What's the first number?: "))
    x=' '.join(operations) # it print + - * /
    print(x)
    while not calculate_finished:

        chosen_operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        answer = operations[chosen_operation](num1,num2)
        # equivalent solution to the line above
        
        #calc_func = operations[chosen_operation]
        #answer = calc_func(num1,num2)

        print(f"{num1} {chosen_operation} {num2} = {answer}")

        msg = f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
        is_finished = input(msg)
        if is_finished == 'y':
            num1 = answer
        elif is_finished =='n':
            #calculate_finished = True
            calculator()

calculator()