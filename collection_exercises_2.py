# EXERCISE 9
# grocery_list = ['clementines', 'salmon', 'chicken', 'blueberries', 'coconut milk']

# for item in grocery_list:
#     print('*' + ' ' + item)

# grocery_list.append('rice')
# print(grocery_list)

# print(len(grocery_list))

# print(grocery_list.count('bananas'))

# def need_bananas(grocery_list):
#     if grocery_list.count('bananas') == 0:
#         print("You don't need to pick up bananas today.")
#     else:
#         print("You need to pick up bananas.")
# need_bananas(grocery_list)

# print(grocery_list[1])

# for item in sorted(grocery_list):
#     print('*' + ' ' + item)

# grocery_list.pop(1)
# for item in sorted(grocery_list):
#     print('*' + ' ' + item)

# EXERCISE 10
students = {
    'cohort1': 34,
    'cohort2': 42,
    'cohort3': 22
}

# def cohort_students():
#     for cohort, number in students.items():
#         print("{}: {} students".format(cohort, number))
# cohort_students()

# students['cohort4'] = 43
# print(students)

# print(students.keys())

# Map used here to transform the values in the dictionary
# But is there a better way to update the dictionary as the values are transformed?
new_students = list(map((lambda number: float(number) * 1.05), students.values()))

print(new_students)
students['cohort1'] = new_students[0]
students['cohort2'] = new_students[1]
students['cohort3'] = new_students[2]
print(students)

# del students['cohort2']
# print(students)

# total = 0
# for cohort, number in students.items():
#     total += number
# print(total)








# list = ['1','2','3']
# #counter = 0
# for i in range(len(list)):
#     n = list[i]
#     nn = int(n) + 1
#     list[i] = nn
#     #counter += 1
# print(list)

# for cohort, number in students.items():
#     students[cohort] = round((float(number) * 1.05), 2)
# print(students)