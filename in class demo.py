# Write the Tanh function from scratch using only the Numpy library 

import numpy as np

def tanh(x):
    return (np.exp(x) - np.exp(-x))/(np.exp(x) + np.exp(-x))

# Use a for loop to call the Tanh function you wrote above using input values ranging from -10 to 10 (including both -10 and 10) with increments of 5
# For each function call, print the output as "The Tanh value of x is y" in a new line
   # Replace x and y with appropriate values 

for i in range(-10, 11, 5):
    print("The Tanh value of", i, "is", tanh(i))
    



    