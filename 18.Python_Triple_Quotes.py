str = '''
this ia a long string that is made up of 
several lines and non-printable characters such as
TAB (\t) and they will show up that way when displayed.
NEWLLINES within the string wheteher explicitly given like
this within the brackets [\n],  or just a newline with in the 
variable assignment will also show up.
'''
print(str)

#use of raw string : In normal string while printing escapes the backslash characters. But raw strings produce as usual
print('C:\\Demo') #first \ will be used for escaping
print(r'C:\\Demo') #ignores both \