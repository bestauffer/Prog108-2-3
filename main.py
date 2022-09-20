# Exercise 2-3: Create a simple program

# INSTRUCTIONS

# Create a simple program on your own to ask for the length and width of a rectangle/square.

# Then calculate the area and perimeter and display the results.

# There is no starting file for this activity.

# Consider user experience and output - include a title, and a farewell greeting.
print("Lets find the area & perimeter of a rectangle!!!")
print()
length = int(input('Enter the length: '))
width = int(input('Enter the width:  '))
area = length * width
perimeter = 2*(length + width)
print("====================Results====================")
if length == width:
  print("It's a square!!!")
else:
  print("It's a rectangle!!!")
print()
print("length:   ", length)
print("width:    ", width)
print("area:     ", area)
print("perimeter:", perimeter)
print()
print("Goodbye user")
