#Dictionary methods are that which are available to a dictionary objects
print('----------------len() method---------------')
dict1 = {'name':'adarsh','age':'20','sex':'male'}

#clear() method - deletes all the elements (key-value) pairs of the  dictionary
print('The length of the dict1 before clear() method is : ',len(dict1))
dict1.clear()
print('The length of the dict1 after clear() method is : ',len(dict1))

#copy() method - returns a copy of the dictionary object and stores it in the another one
print('\n----------------copy() method---------------')
dict1 = {'name':'adarsh','age':'20','sex':'male'}
print('The dict1 : ',dict1)
dict2 = dict1.copy()
print('The dict2 : ',dict2)

#array as a value to dictionary
print('\n--------------insert() method---------------')
dict3 = {'subject':['c','c++','java'],'id':[1,2,3]}
print('dict3 before insertion operation : ',dict3)
dict3['subject'].append('python')
dict3['id'].append(4)
print('dict3 after insertion operation : ',dict3)

#fromkeys() method - it is used to assign a specified default value to dictionary keys
print('\n-----------------fromkeys() method--------------')
key = ['name','age','sex']
dict4 = dict3.fromkeys(key) #without values
print('dict4 after performing fromkeys() operation without values : ',dict4)
dict4 = dict3.fromkeys(key,'enter value') #along with values
print('dict4 after performing fromkeys() operation with values : ',dict4)

#get() method : It will return the value of the given key
print('\n------------------get() method--------------------')
print('The value of Name in dict1 is',dict2.get('name'))
print('The value of Age in dict1 is',dict2.get('age'))

#items() method : It will return the key-value pairs as a list of key-value tuple pair
print('\n------------------items() method------------------')
print('key-value pairs are : ',dict1.items())

#keys() method : It will return the list of all keys.
print('\n--------------------keys() method-------------------')
print('The keys list in the dict1 : ',dict1.keys())
print('The keys list in the dict3 : ',dict3.keys())

#values() method : It will return the list of all values.
print('\n--------------------values() method-----------------')
print('The values list in dict1 : ',dict1.values())
print('The values list in dict2 : ',dict3.values())

#default() method : It will set the default values to the keys as values. if any value already present, it won't overrife the previous one
print('\n--------------------default() method-----------------')
dict4.setdefault("name","No data") #already exists
dict4.setdefault("age","Need age") #already exists
dict4.setdefault("students","No data")
dict4.setdefault('faculty',"Need data")
print(dict4)

#update method : it updates a given key value pair given in form of a dictionary to the existing one
print('\n--------------------update() method-----------------')
dict5 = {'name':'naresh','age':'41'}
dict6 = {'sex':'male'}
print('dict5 before updating ->',dict5)
dict5.update(dict6)
print('dict5 after updating  ->',dict5)