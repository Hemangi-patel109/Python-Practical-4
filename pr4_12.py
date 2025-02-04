#Write a Python program to find the list of words that are longer than n from a given string.

def word_count(ip_str, n):
    words = ip_str.split()
    result_list = []
    
    for word in words:
        if len(word) > n:
            result_list.append(word)
    return result_list

ip_str = "This is practical set four."
n = 3
result = word_count(ip_str, n)
print(f"Words longer than {n} in '{ip_str}' is {result}")