#append() method - inserts an element at the last index of the list
print("------------Append Method----------")
skills = ['C','C++','java','python']
print('skills list before using .apend() method : ',skills)
skills.append('java Script')
print(f'skills list after using .apend() method : {skills}\n')

#count() method - counts the number of elements present in the list of one that is given as a parameter
print('-----------Count Method------------')
math = ['m1','m2','m2','m3','m4','m2','m1','m3','m3','m2']
print(f'The List math is {math}')
print('The number of m3 elements in the list math : ',math.count('m3'))
print('The number of m2 elements in the list math : ',math.count('m2'))

#extend() method - concatenates two lists l1 and l2 and saves the result in l1
print('\n----------Extends Method------------')
print('The Skills List : ')
print('The Math List : ')
skills.extend(math)
print('The Extended (concatenated) list : ',skills)

#index() method - returns the first index of an element that is passed as a parameter
print('\n-----------Index Method---------------')
print('The skills list is : ',skills)
print(f'The index of the element \'java\' is : {skills.index("java")}')
print(f'The index of the element \'m1\' is : {skills.index("m1")}\n')

#insert() method - Unlike append() method, it inserts an element at a given index.
print('------------Insert Method--------------')
l1 = [1,2,3,4]
print('The List l1 before inserting : ',l1)
l1.insert(3,10)
print('The List l1 after inserting : ',l1)

#pop() method - it removes the element with n-1 (last) index
print('\n------------Pop Method------------------')
print('The List l1 before popping : ',l1)
l1.pop()
print('The List l1 after popping : ',l1)

#remove() method - it removes the specified element from the list that is sent as parameter
print('\n------------Remove Method---------------')
print('The List l1 before removing : ',l1)
l1.remove(2)
print('The List l1 after removing the element 2 : ',l1)

#reverse() method - It reverses the order of the list
print('\n------------Reverse Method---------------')
l2 = ['adarsh','nalla','mahesh','gattam']
print('The List l2 is ',l2)
print('The List l2 before reverse method : ',l2)
l2.reverse()
print('The List l2 after reverse method : ',l2)

#sort() method - It sorts the list as per the numerical or alphabetical order of the elements
print('\n--------------Sort Method------------------')
print('The List l2 before sorting : ',l2)
l2.sort()
print('The List l2 after sorting : ',l2)