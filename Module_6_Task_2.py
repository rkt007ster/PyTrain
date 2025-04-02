
# Task 2: Demonstrate List Slicing

list1 = []
list2 = []
for i in range(1,11):
    list1.append(i)

five_element = list1[:5]
reverse = five_element[::-1]

print('Original List: ', list1)
print('Extracted First Five Elements: ',five_element)
print('Reversed Extracted Elements: ', reverse)