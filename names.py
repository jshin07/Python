# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
#
#
# def fullName(arr):
#     for i in students:
#         print i["first_name"], i["last_name"]
# fullName(students)




users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
#

# def printDictionary (users):
#     for key in users:
#         count =0
#         print key
#         for y in users[key]:
#             count += 1
#             length =len(y["first_name"]) + len(y["last_name"])
#             print count,"-", y["first_name"].upper(), y["last_name"].upper(),"-", length
#
# printDictionary(users)
#


def printKey (users):
    for i in users:
        print i
printKey(users)
