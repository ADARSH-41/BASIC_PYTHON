tup1,tup2 = ('xyz','abc'),(101,102,104)
print(tup1,tup2)
#len() function
print('\n--------------len() function--------------')
print('Length of tuple 1 : ',len(tup1))
print('Length of tuple 2 : ',len(tup2))

#max() function
print("\n-------------max() function--------------")
print('Max value in tuple tup1 : ',max(tup1))
print('Max value in tuple tup2 : ',max(tup2))

#min() function
print("\n-------------min() function--------------")
print('Min value in tuple tup1 : ',min(tup1))
print('Min value in tuple tup2 : ',min(tup2))

#tuple() function
print("\n-------------tuple() function--------------")
list1 = ['abc','bcd','cde','def']
print('list1 is : ',list1)
tuple1 = tuple(list1)
print('tuple form of list1 is : ',tuple1)
str1 = "anderson"
print('str1 is : ',str1)
tuple2 = tuple(str1)
print('Tuple form of str1 is : ',tuple2)
