# Assignment for Tuesday 11/30/2021
# Written by Maximilian Conroy for Per Scholas Cloud DevOps course

# Assignment Details:
# Create a function named even that will take 2 int parameters, one for starting point and the other is a counter.
# Return a list of counter smallest even int greater than or equal to starting point in ascending order.
#
# STDIN      Function
# -----      --------
# 5 7     →  start = 5, n = 7
#
# Sample Output:
# 6 8 10 12 14 16 18

def list_counter(start, count):
    # Initialize list to size of count
    list1 = [0] * count
    # Set a counter used to increase by 2 every iteration
    counter = 0
    # If start is an odd number, add 1 to even it
    if start % 2 != 0:
        start += 1
    # Iterate through list
    for i in range(len(list1)):
        # Set current element to the next even number in sequence
        list1[i] = start + counter
        # Increment counter by 2 to prepare for next iteration
        counter += 2
    # Print list results
    print(list1)


# Call the function
list_counter(5, 7)
