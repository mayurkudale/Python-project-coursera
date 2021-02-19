# Python code to demonstrate the working of 
# copy_abs(),copy_sign() and copy_negate()

# importing "decimal" module to use decimal functions
import decimal

# Initializing decimal number
a = decimal.Decimal(9.53)

# Initializing decimal number
b = decimal.Decimal(-9.56)

# printing absolute value using copy_abs()
print ("The absolute value using copy_abs() is : ",end="")
print (b.copy_abs())

# printing negated value using copy_negate()
print ("The negated value using copy_negate() is : ",end="")
print (b.copy_negate())

# printing sign effected value using copy_sign()
print ("The sign effected value using copy_sign() is : ",end="")
print (a.copy_sign(b))


'''
9. copy_abs() :- This function prints the absolute value of decimal argument.

10. copy_negate() :- This function prints the negation of decimal argument.

11. copy_sign() :- This function prints the first argument by copying the sign from 2nd argument.

'''