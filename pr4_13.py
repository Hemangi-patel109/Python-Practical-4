#Write a Python function that takes two lists and returns True if they have at least one common member.

def common_num(list1,list2):
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                return True
            return False
listA = [1,2,3,4,5]
listB = [1,3,5,7,9]
print(common_num(listA,listB))