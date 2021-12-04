##########################################################################################
# Step 1. Modules:
#           are files containing pieces of frequently used code
#           have their own namespace
#           are accessed with the command "import"
#           should have the extension ".py"
# User can create own modules. Python searches modules in the order below:
#   current dir --> dirs in the env variable PYTHONPATH --> dirs in the env variable PATH
# These pathes can be changes inside the script using variable sys.path
# 
# The command "import" also created compiled version of module with the extension ".pyc"
# Python always keeps compiled module in sync with the "*.py"
# A module is loaded only once, i.e, a second import statement does nothing.
# Use the command ""reload" to load again the same module.
##########################################################################################

import my_math

PI = 3

print(my_math.add(3, 4))
print(my_math._add(3, 4))

print(my_math.sub(3, 4))
print(my_math.mult(3, 4))

print(PI)
print(my_math.PI)

##########################################################################################
# Step 2. Other syntax of "import" command:
#         from <modules_list> import *
#         in this case names starting with "_" are not importing
##########################################################################################

PI = 3

from my_math import *

print(add(3, 4))
# print _add(3, 4)
print(sub(3, 4))
print(mult(3, 4))

print(PI)

##########################################################################################
# Step 3. Using builtin function "dir" to get
#         list of the names in the module
##########################################################################################

import my_math

print(dir())

print("--------------")

print(dir(my_math))

##########################################################################################
# Step 4. Can be imported part of the names
##########################################################################################

from my_math import add, sub

print(add(3, 4))
print(sub(3, 4))

##########################################################################################
# Step 5. Syntax  "import <module_name> as <new_name>"
#                 is smth like alias for <module_name>
##########################################################################################

PI = 3

import my_math as new_math

print(new_math.add(3, 4))
print(new_math._add(3, 4))

print(new_math.sub(3, 4))
print(new_math.mult(3, 4))

print(PI)
print(new_math.PI)

##########################################################################################
# Step 6. Python Standard Library includes large amount of modules. List of modules
#         names can be found in the Python doc. Below is the list of frequently
#         used modules.
#  string     Common string operations
#  datetime   Basic date and time types
#  types      Names for built-in types
#  math       Mathematical functions
#  os         Miscellaneous operating system interfaces
#  os.path    Common pathname manipulations
#  re         regexp support
#  Tkinter    Python interface to Tk
#  sys        System-specific parameters and functions
##########################################################################################

import string
import math

print(dir(string))
print("--------------")
print(dir(math))
print("--------------")

##########################################################################################
# Step 7. Create user-defined packages
#    - create package structure
#    - add special file named "__init__.py" to each subdir (including package directory)
#    - each "__init__.py" file should contain "import" or "from ... import ..." commands
#      to load names in the subdirectory
#    - make package path visible for python, for that:
#      a) do nothing if package is in the current directory    (or)
#      b) add package path to the env variable PYTHONPATH      (or)
#      c) add package path to the env variable PATH            (or)
#      d) add package path to the variable sys.path within the script
#      e) import package directory in the main script ("import ..."
#         or "from ... import ...")
##########################################################################################

from my_package import *

print(dir())

print("--------------")

my_add()
my_add_complex()
io_files.io_read()

##########################################################################################
# Step 8. Using the form "import ...". In this case we should mention
#         full notation to the name
##########################################################################################

import my_package

print(dir(my_package))

print("--------------")

my_package.my_add()
my_package.my_add_complex()
my_package.io_files.io_read()

##########################################################################################
# Step 9. module's __name__
#         Builtin variable __name__ automatocally set to the value "__main__" if
#         the module called by python, and to the module name if the module imported.
##########################################################################################

import my_package

print(__name__)
print(my_package.__name__)
print(sys.__name__)

##########################################################################################
# Step 10. module's __name__ can be used to separate cases of calling the module
#          by python or importing from other module
##########################################################################################

import my_calc

my_calc.calc()

##########################################################################################
# invalid step #
##########################################################################################
