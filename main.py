age = 25
print(age)
############
friends_list = ["Anton", "Beka", "Muha", "Jhon"]
print(friends_list)
###########################
if age >= 18:
    print("Вы совершеннолетний")
else:
    print("Вы несовершеннолетний")
###################################
for friend in friends_list:
    print(f"Привет, {friend}!")
###################################
while age < 30:
    print(f"Текущий возраст: {age}")
    age += 1
####################################
def add_numbers(number1, number2):
    result = number1 + number2
    return result

num1 = 5
num2 = 7
sum_result = add_numbers(num1, num2)
print(f"Сумма {num1} и {num2} равна {sum_result}")
##################################################
def print_greeting(name):
    print(f"Привет, {name}!")

print_greeting("Dias")
####################################################
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)

print(f"Факториал числа 5 равен {result}")
