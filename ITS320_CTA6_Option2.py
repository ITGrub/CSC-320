#-------------------------------------------
# Program Name: Critical Thinking Option 2			Change 1: Fixed Program Name
# Author: Brian Holden
# Date: 15 July, 2024
#-------------------------------------------
# Pseudocode: The program begins by defining the cartesian product and then the 
# main code script asking the user to enter list A separated by commas and then
# list B separated by commas. The cartesian product is then printed to the user.
#-------------------------------------------
# Program Input a: 2,4,6,8
# Program Input b: 1,3,5,7
# Program Output: (2, 1), (2, 3), (2, 5), (2, 7), (4, 1), (4, 3), (4, 5), 
# Program Output Cont.: (4, 7), (6, 1), (6, 3), (6, 5), (6, 7), (8, 1), (8, 3), 
# Program Output Cont.: (8, 5), (8, 7)
#-------------------------------------------
def cartesian_product(A, B):
    return [(a, b) for a in A for b in B]

def main():
    A = list(map(int, input("Enter list A (comma-separated): ").split(','))) # Input two lists for the Cartesian 
    B = list(map(int, input("Enter list B (comma-separated): ").split(','))) # product from the user seperated by commas

    result = cartesian_product(A, B) # Compute the Cartesian product
    
    print("AxB =", result) # Print the Cartesian product

if __name__ == "__main__":
    main()
