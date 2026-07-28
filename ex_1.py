# exercise 1 Rectangle Area calculator
# This program calculates the area of a rectangle based on user input for length and width  
# this will raise an error because the input() function returns a string, and multiplying two strings is not valid for calculating area. To fix this, we need to convert the inputs to integers or floats before performing the multiplication.
# i had to delete the few code in above i wrote before it was the best example but two sets of code doing the same thing is pretty messy for the user to read and understand so i had to delete it and write a new one below
length = float(input('Enter the length of the rectangle in Gn(goon metres): '))
width = float(input('Enter the width of the rectangle in Gn(goon metres): '))
area = length * width
print(f"The true area of the rectangle is: {area}Gn² (goon metres squared)")
# how does someone use superscript in windows 11?
# hence it works and now we knw that 69 * 67 = 4623 (great work chat now dont ask why i love these numbers)