str1 = ''
str2 = 'geeks'

# repr is used to print the string along with the quotes
print (repr(str1 and str2)) # Returns str1 
print (repr(str2 and str1)) # Returns str1
print (repr(str1 or str2)) # Returns str2 
print (repr(str2 or str1)) # Returns str2

str1 = 'for'

print (repr(str1 and str2)) # Returns str2 
print (repr(str2 and str1)) # Returns str1
print (repr(str1 or str2)) # Returns str1 
print (repr(str2 or str1)) # Returns str2


