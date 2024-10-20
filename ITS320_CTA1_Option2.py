Correction made: Added the internal documentation for the project to the top of the source code.
#-------------------------------------------
# Program Name: Module 1 Critical Thinking
# Author: Brian Holden
# Date: 16 June, 2024
#-------------------------------------------
# Pseudocode: The user will be prompted to enter an integer of their choice and then be asked     # again to enter another integer of their choice. Once the user inputs those integers, the program # script uses the integer, float, and modulo functions to calculate and print the final answers as    # requested.
#-------------------------------------------
# Program Input a: 651516
# Program Input b: 65
# Program Integer Division Output: 10023 
# Program Float Division Output: 10023.323076923078
# Program Modulo Division Output: 21
# Program Output: Division Complete
#-------------------------------------------

a = input(prompt:="Enter a number: ")
b = input(prompt:="Enter a number: ")
print("integer division:", int(a)//int(b))
print("float division:", float(a)/float(b))
print("modulo division:", int(a)%int(b))
print("division complete")