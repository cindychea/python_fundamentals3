# EXERCISE 11
# one_to_hundred = range(1, 101)
# for num in one_to_hundred:
#     if num % 3 == 0 and num % 5 == 0:
#         print('BitMaker') 
#     elif num % 3 == 0:
#         print('Bit')
#     elif num % 5 == 0:
#         print('Maker')
#     else:
#         print(num)

# EXERCISE 12
def pizzas():
    print('How many pizzas do you want to order?')
    number_pizzas = list(range(1, (int(input())+1)))
    return number_pizzas
pizza_order = pizzas()
for pizza in pizza_order:
    print(f'How many toppings for pizza {pizza}')
    topping_number = input()
    print(f'You have ordered a pizza with {topping_number} toppings.')