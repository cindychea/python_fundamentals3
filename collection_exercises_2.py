# EXERCISE 9
grocery_list = ['clementines', 'salmon', 'chicken', 'blueberries', 'coconut milk']

for item in grocery_list:
    print('*' + ' ' + item)

grocery_list.append('rice')
print(grocery_list)

print(len(grocery_list))

print(grocery_list.count('bananas'))

def need_bananas(grocery_list):
    if grocery_list.count('bananas') == 0:
        print("You don't need to pick up bananas today.")
    else:
        print("You need to pick up bananas.")
need_bananas(grocery_list)

print(grocery_list[1])

for item in sorted(grocery_list):
    print('*' + ' ' + item)

grocery_list.pop(1)
for item in sorted(grocery_list):
    print('*' + ' ' + item)

