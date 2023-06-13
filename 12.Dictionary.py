
'''Python Dictionary is a key-value pair data structure.'''
dict1 = {'Name':'kumari','age': 21,'sex':'female'}
print(dict1)
#Accessing Elements in a dictionary is done by calling the key. We will get the respective value assocaited with the key in the key : value pair.
print('\n--------------Accessing------------')
print('Name : ',dict1['Name'])
print('Age : ',dict1['age'])
print('Sex : ',dict1['sex'])

#Updating dictionary
print('\n--------------Updating------------')
dict1['age'] = 20 #update existing entry
dict1['school'] = 'JNTU-GV' #add new entry
print('after installing updates')
print(dict1)

#Deleting dictionary
print('\n--------------Deleting------------')
print('Initial Dictionary : ',dict1)
del dict1['Name'] # to delete the pair corresponding to a given value
print('After deleting Name attribute of dictionary : ',dict1)
dict1.clear() #to delete all the entries of the dictionary
print('After deleting all the key-value pairs : ',dict1)
del dict1
print(dict1) #it will throw an error