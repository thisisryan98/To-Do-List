def divide_numbers():
    try: 
        number_one = float(input("enter your first number: "))
        number_two = float(input("enter your second number: "))
        print("The result is: ")
        print(number_one / number_two)
    except ZeroDivisionError:
        print("You can't divide by zero!")

divide_numbers()