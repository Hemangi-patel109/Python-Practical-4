#Write a python program which covers all the methods (functions) of list

list1 = [1,2,3]
print(list1)
list1.append(4)     # append
print("Append: ",list1)

list1.extend([6,7])     # extend
print("Extend: ",list1)

list1.insert(4,5)     # insert
print("Insert: ",list1)

list1.remove(6)     # remove
print("remove:",list1)

list1.pop(4)    # pop
print("Pop: ",list1)

list1.clear()   # clear
print("Clear: ",list1)

list2 = [10,20,30,40,50,10]    
print("List2: ",list2)
print("Index of 20: ",list2.index(20))  #index

print("Count of 10:" ,list2.count(10))      # count

list2.sort()     # sort
print("Sort: ",list2)

list2.reverse()     # reverse
print("Reverse: ",list2)

new_list = list2.copy()     # copy
print("Copy: ",new_list)