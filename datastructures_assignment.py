#create an empty list
my_list=[]
my_list=[10,20,30,40]
#append to the first one
my_list.append(my_list)
#change the second element
my_list[1]=15
#create a new list
my_list2=[50,60,70]
#extend the new list with the first list
my_list.extend(my_list2)
#delete the second element of the list
del my_list[-1]
#sort list by ascending order
my_list2.sort()
#print element 30
print(my_list.index(30))

