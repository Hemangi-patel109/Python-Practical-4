#Write a Python program to print the numbers of a specified list after removing even numbers from it.

list1 = [10, 2, 13, 4, 5, 6, 7, 78, 1]
list2 = []
for i in list1:
    if i % 2 != 0:
        list2.append(i)
print(list2)