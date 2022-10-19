#!/usr/bin/env python3

"""importing from first_module"""

# the name of the import matches the file name (minus the .py)
# these two files MUST BE IN THE SAME DIRECTORY
import first_module

#Now run second_module.py, which will import/execute everything in first_module.py.
#__name__ is the variable from  the imported_module
print(f"Module #2 Name= {__name__}")
