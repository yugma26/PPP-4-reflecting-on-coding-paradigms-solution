# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

'''
Make sure to answer the following questions about your coding process:

How does this solution ensure data immutability?

#The data saved in an immutable storage format remains fixed due to the WORM (write-once-read-many) mechanism.

Is this solution a pure function? Why or why not?
#A pure function is a function which: Given the same input, will always return the same output.

Is this solution a higher order function? Why or why not?
#A higher order function is a function that takes one or more functions as arguments, 
or returns a function as its result.

Would it have been easier to solve this problem using a different programming style?
#No because only python has easy and quick solution.

Why in particular is functional programming a helpful paradigm when solving this problem?
#Functional programming is less prone to errors or bugs in code. 
The code follows a consistent approach in the form of pure functions.
Each function is associated with some purpose and an output value.
This structured way of writing code reduces the risks of errors during compilation.
'''
