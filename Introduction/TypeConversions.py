# There are two types of type conversions -
# Implicit conversion - Automatic type conversion,
# Explicit conversion - manual type conversion

# Python Implicit Type Conversion::
print(1+2.3)
print(type(1+2.3))
# Python always converts smaller data type ot bigger data types to avoid loss of data.
# Error if
# print("23" + 1) #We need to convert explicitly in this case.
#In Explicit Type Conversion, users convert the data type of an object to required data type.
print(int('12')+34)
print(type("123"))
"""
Key Points to Remember
Type Conversion is the conversion of an object from one data type to another data type.
Implicit Type Conversion is automatically performed by the Python interpreter.
Python avoids the loss of data in Implicit Type Conversion.
Explicit Type Conversion is also called Type Casting, the data types of objects are converted using predefined 
functions by the user.
In Type Casting, loss of data may occur as we enforce the object to a specific data type.
"""