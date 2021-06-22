my_list = [1,2,4,5,1,4,5,6,]

print("original list is:" + str(my_list))

list2 = []

for i in my_list:
    if i not in list2:
        list2.append(i)

print('New list after duplicates removal: ' +str(list2))