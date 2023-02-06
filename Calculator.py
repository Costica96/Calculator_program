"""This program take the number from user and calculate different oparation."""

def add(given_list: list) -> int:
    """This function takes numbers from user and returns & displays the sum of these"""
    add_number = 0
    for number in given_list:
        add_number += number
    return add_number

def substract(given_list: list) -> int:
    """This function takes numbers from user and returns & displays the substract of these"""
    sub_numb = given_list[0]*2
    for number in given_list:
        sub_numb = sub_numb - number
    return sub_numb

def multiply(given_list: list) -> int:
    """This function takes numbers from user and returns & displays the multiply of these"""
    multiply_number = 1
    for number in given_list:
        multiply_number *= number
    return multiply_number

def div(given_list: list) -> int:
    """This function takes numbers from user and returns & displays the divide of these"""
    div_numb = given_list[0]**2
    for number in given_list:
        div_numb = div_numb / number
    return div_numb

def power(first_param, second_param):
    """This function takes numbers from user and returns & displays the power of these"""
    pow_numb = first_param ** second_param
    return pow_numb


if __name__ == "__main__":
    def user_numbers():
        user_input = int(input("How many nymbers you want: "))
        i=1
        user_list = []
        while i<=user_input:
            user_numbers = int(input(f"Introduce your {i} number: "))
            user_list.append(user_numbers)
            i += 1
        return user_list
    
user_action = input("What operation you want to do with your numbers?(add, substract,multiply, div, power): ")
if user_action == "add":
    print(add(user_numbers()))
elif user_action == "substract":
    print(substract(user_numbers()))
elif user_action == "multiply":
    print(multiply(user_numbers()))
elif user_action == "div":
    print(div(user_numbers()))
elif user_action == "power":
    first_param = int(input("Please, introduce your first number: "))
    second_param = int(input("Please introduce your second number: "))
    print(power(first_param, second_param))
else:
    print("Choose other operation")