#-------------------------------------------
# Program Name: Critical Thinking Option 2			Change 1: Fixed Program Name
# Author: Brian Holden
# Date: 06 July, 2024
#-------------------------------------------
# Pseudocode: The five grades are entered and all are placed into 
# an array of numbers so that a min and max can be found. All grades are
# added together and divided by the number of inputs for the average.
#-------------------------------------------
# Program Inputs:						Change 2: Added in more documentation for my code
# Grade 1: 58
# Grade 2: 62
# Grade 3: 89
# Grade 4: 98
# Grade 5: 68
#
# Program Outputs:				
# Average: 75.00
# Maximum: 98.00
# Minimum: 58.00
#-------------------------------------------
def main():
  # Initialize variables to store grades
  grades = []

  # Read five grades from the user
  for i in range(5):
      grade = float(input(f"Enter grade {i+1}: "))
      grades.append(grade)

  # Calculate average
  average = sum(grades) / len(grades)

  # Calculate maximum and minimum
  maximum = max(grades)
  minimum = min(grades)

  # Print the results
  print(f"Average grade: {average:.2f}")
  print(f"Maximum grade: {maximum:.2f}")
  print(f"Minimum grade: {minimum:.2f}")

if __name__ == "__main__":
  main()
