#Flatten a nested list structure.
#Example: if list1 = [1, [2, 3], [4, 5, [6, 7] ] ] then try to convert it in 1-dimensional [1, 2, 3, 4, 5, 6, 7]

def flat_list(nested_list):
    if not isinstance(nested_list, list):  
        return []  

    listA = []
    for item in nested_list:
        if isinstance(item, list):
            listA.extend(flat_list(item)) 
        else:
            listA.append(item)
    return listA

list1 = [1, [2, 3], [4, 5, [6, 7]]]
listB = flat_list(list1)
print(f"Original list: {list1}")
print(f"Flattened list: {listB}") 