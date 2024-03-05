my_list = []
# append values
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#print(my_list)

# insert 15 at the second position
my_list.insert(1, 15) 

print("First list: ", my_list)

# extend list
list2 = [50,60,70]               #create second list
print("Second list: ", list2)

my_list.extend(list2)
print("Extended list: ",my_list)

# removing the last element
my_list.remove(70)
print(my_list)

# sorting in ascending order
my_list.sort(reverse = False)
print(my_list)

#find and print index of the value 30
index_of_30 = my_list.index(30)
print("Index of the value 30 is : ", index_of_30)