
# python tuple is an immutable object. immutable means unchangeable

tup1 = ('adarsh','aditya','surya','varma','reddy',101,420)
tup2 = (2002,2003,2004,2005,2006)
print(tup1,tup2)

#accessing tuple's elements
print("\n----------Access an Element--------------")
print("tup1[0] : ",tup1[0])

#slicing of tuples
print("\n----------Slicing a Tuple--------------")
print("tup1[1:5] : ",tup1[1:5])

#updating of tuples at a given position as follows: tup1[0] = 10 cannot be done
print("\n----------Updating a Tuple--------------")
'''tup[0] = 10 #invalid. you can decomment and try'''
'''But you can do as follows to modify a tuple.'''
tup3 = tup1+tup2
print(tup3)

#Deletion in tuple is also an impossible one. But you can delete the entire tuple
'''del tup1[3] #Invalid. You can decomment and try. It will throw you an error.'''
print("\n----------Deletion in a Tuple--------------")
del tup1
print(tup1) #it will show you an error.
