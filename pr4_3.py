# Write a python program to check whether the given list is palindrome or not.

list1 = [1,2,1]
copy = list1.copy()
copy.reverse()
if list1 == copy:
    print("List is Palindrome")
else:
    print("List is not Palindrome")