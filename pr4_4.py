# Write a python program to store strings in list and then print them.
string_lists = []
string_list = int(input("Enter number of string you want to enter: "))
for i in range(string_list):
    strings = input(f"Enter string {i+1}: ")
    string_lists.append(strings)

print(string_lists)