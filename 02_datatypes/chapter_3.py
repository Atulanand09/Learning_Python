#Interger data type

black_tea_grams = 14
ginger_tea_grams = 3

total_tea_grams = black_tea_grams + ginger_tea_grams
print(total_tea_grams , "Grams of tea in total")

remaing_tea_grams = black_tea_grams - ginger_tea_grams
print(remaing_tea_grams, "Grams of tea remaining after making ginger tea")


milk_liters = 7
servings = 4
milk_per_serving = milk_liters / servings
print(milk_per_serving, "Liters of milk per serving")

total_tea_bags = 7
pots = 2
bags_per_pot = total_tea_bags // pots
print(bags_per_pot, "Tea bags per pot")

total_codamom_pods = 10
pods_per_cup = 3
leftover_pods = total_codamom_pods % pods_per_cup
print(leftover_pods, "Codamom pods left after making tea")

total_tea_bags = 7
pots = 2
bags_per_pot = total_tea_bags / pots
print(bags_per_pot, "Tea bags per pot (float division)")  
# Float division results in a float value even if the result is a whole number  
# Use // for integer division to get an integer result
# Example: 7 / 2 = 3.5 (float division) vs 7 // 2 = 3 (integer division)
print(type(bags_per_pot))
# Use type() function to check the data type of a variable
# In this case, bags_per_pot will be of type 'float' due to float division
# Understanding the difference between float and integer division is important in programming
# Float division (/) always returns a float
# Integer division (//) returns an integer by discarding the decimal part
# This distinction can affect calculations and data types in your programs
print(isinstance(bags_per_pot, float))
# Use isinstance() to check if a variable is of a specific type
# Here, we check if bags_per_pot is an instance of float
# This is useful for type checking and validation in your code
# Understanding data types and their behavior is crucial for effective programming

print(isinstance(bags_per_pot, int))
# Check if bags_per_pot is an instance of int
# This will return False since bags_per_pot is a float due to float division
# This highlights the importance of choosing the correct division operator based on the desired outcome
# Summary:
# Use / for float division and // for integer division
# Use type() to check variable types
# Use isinstance() for type checking
# Understanding data types and division operators is essential for accurate calculations in programming
# Updata Interger
# Integer data type represents whole numbers without decimal points
# Examples of integer operations include addition, subtraction, multiplication, and division
# Integer division (//) discards the decimal part and returns an integer result
# Float division (/) returns a float result, even if the result is a whole number
# Use type() to check the data type of a variable
# Use isinstance() to check if a variable is of a specific type
# Understanding data types and their behavior is crucial for effective programming
# Integer data type represents whole numbers without decimal points
# Examples of integer operations include addition, subtraction, multiplication, and division
# Integer division (//) discards the decimal part and returns an integer result
# Float division (/) returns a float result, even if the result is a whole number
# Use type() to check the data type of a variable
# Use isinstance() to check if a variable is of a specific type
# Understanding data types and their behavior is crucial for effective programming
# Integer data type represents whole numbers without decimal points
# Examples of integer operations include addition, subtraction, multiplication, and division
# Integer division (//) discards the decimal part and returns an integer result
# Float division (/) returns a float result, even if the result is a whole number
# Use type() to check the data type of a variable
# Use isinstance() to check if a variable is of a specific type
# Understanding data types and their behavior is crucial for effective programming
# Integer data type represents whole numbers without decimal points
# Examples of integer operations include addition, subtraction, multiplication, and division
# Integer division (//) discards the decimal part and returns an integer result
# Float division (/) returns a float result, even if the result is a whole number
# Use type() to check the data type of a variable
# Use isinstance() to check if a variable is of a specific type
# Understanding data types and their behavior is crucial for effective programming  
# Integer data type represents whole numbers without decimal points. 