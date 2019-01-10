#Get a SEGFAULT
#Idea: print a value by random address
import ctypes

print(ctypes.cast(123456789, ctypes.py_object).value)
