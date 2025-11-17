# student_data = { 'id1':
#      {'name': ["Sara"],
#      'class': ['V'],
#     'subject_inter':['english, math, science']},
#     'id2':
#      {'name': ["Bob"],
#      'class': ['V'],
#     'subject_inter':['english, math, science']},
#     'id3':
#      {'name': ["Surya"],
#      'class': ['V'],
#     'subject_inter':['english, math, science']},
#     'id4':
#      {'name': ["Jimmy Bob Jr."],
#      'class': ['V'],
#     'subject_inter':['english, math, science']},
# }
# result = {}
# for key,value in student_data.items():
#     if value not in result.values():
#         result[key] = value

# print(result)
tes = {'codingnal': 2, 'is' :2, 'best' : 2, 'for' : 2, 'coding' : 1}
print(tes)
k = int(input("enter in a number: "))

res = 0
for key in tes:
    if tes[key] == k:
        res = res + 1

print("frequince of K is: " + str(res))