#len() function is used to return the length of the list given as parameter to it
list1 = ['adarsh','hashwanth','ramesh']
print('List1 ',list1)
print('Length of List1 : ',len(list1))

list2 = list(range(5))
print('List 2 ',list2)
print('Length of list2 : ',len(list2))

#max() function
list1, list2 = ['adarsh','ramesh','praveen'], [0,2,4,22,32]
print(f"{list1} , {list2}\n")
print(f"Max Element in List 1 : {max(list1)}")
print(f"Max Element of List 2 : {max(list2)}\n")

#min() function
print("Min Element in List 1 : ",min(list1))
print("Min Element of List 2 : ",min(list2))

#list() function : It returns a list object of a given tuple or string
tup = ('m1','m2','m3','m4')
list1 = list(tup)
print(f'\nThe tuple is : {tup}')
print(f'The List for the tuple is : {list1}\n')

str1 = 'Rao Ramesh'
list2 = list(str1)
print(f'The String is : {str1}')
print(f'The List for the String is : {list2}')