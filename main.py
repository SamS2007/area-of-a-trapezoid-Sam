# Area of a trapezoid
# This program will ask the user for the dimensions of a trapezoid
# It will then calculate the area and display it for the user
print("Today we will calculate the area of a trapezoid")

# get the Base1 from user and convert it to float
Base1 = float(input("Enter the first base value (cm):"))

# get the base2 from the user and convert it to float
Base2 = float(input("Enter the second base value (cm):"))

# get the height the from the user and convert it to float
Height = float(input("enter the height value (cm)"))

# calculate the Area of the trapezoid
Area = (Base1 + Base2) / 2 * Height

# Display the Area
print("area of a trapezoid with Base value 1 being " + str(Base1) +
      "cm and second base value " + str(Base2) + " and a tall height of " +
      str(Height) + "cm is " + str(Area) + "cm^2.")
