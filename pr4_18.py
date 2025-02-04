#Write a Python program to split a list every Nth element.

def split_list(input_list, n):
    if not isinstance(n, int) or n <= 0:
        return None 
    if not input_list:
        return []
    result = []
    for i in range(0, len(input_list), n):
        result.append(input_list[i:i + n])
    return result
list1 = [1,2,3,4,5,6,7,8,9,10]
N = 3
split_list1 = split_list(list1,N)
print(f"Original List: {list1}")
print(f"Split every {N} elements: {split_list1}")