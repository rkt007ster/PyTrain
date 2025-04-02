
# Task 1: Create a Dictionary of Student Marks

dictionary = {'Ramprakash':90,'Banrakas':70, 'Binod':55, 'Avisek':43, 'Alice': 85}

name = input("Enter Student's Name: ").capitalize()

if name in dictionary.keys():
    print(name + "'s marks: ",dictionary.get(name))
else:
    print('Student not found')



