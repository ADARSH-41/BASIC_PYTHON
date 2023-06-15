#list object can contain elements of different types.

list = ['C','java',100,12]
print(list)

list1 = [1,-2,3+4j,4.34]
print(list1)

list2 = ['a',"b",'c',"d"]
print(list2,'\n')

#accessing of list elements
print(list1[1])
print(list2[3])
print()

#update
print("Value available at index 2 : ",list1[2])
list1[2] = 10
print("New Value available at index 2 : ",list1[2])
print("Updated list :  ",list1,'\n')


#delete
print(list2)
del list2[2]
print("List 2 after deleting element at index 2 : ")
#to delete entire list. After deleting you will get error while printing the list.
del list1
print(list1)
