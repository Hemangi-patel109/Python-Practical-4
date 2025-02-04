#Write a Python program to multiply all the items in a list.

def multiply_items(list1):
    result = 1
    for num in list1:
        result *= num
    return result

list1 = [5, 4, 10, 7]
result = multiply_items(list1)
print(f"The multiplication of all the items in the list is: {result}")
