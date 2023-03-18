"""
2i Coding Challenge:

“In a language of your choice, using all best practice principles you’re aware of,
could you please provide code that reads a list of 10 numbers ranging between 1 to 100.
Assuming there are 4 duplicates in the list of numbers, the output should remove the duplicates and sort the remaining
numbers in descending order.
Please state any assumptions you’ve made. "

Date: 18/03/2023
Author: Elizabeth Forster
"""

import numpy as np

def format_number_list(numbers) :

    """
    This function formats a list of numbers such that it contains no duplicates and is in descending order

    :param numbers: A list of numbers to be formatted
    :return: A list of numbers formatted as desired
    """

    formatted_numbers = []              # Creates empty list to be added to

    for i in range(len(numbers)) :      # Loops over range of length of list (10)

        if numbers[i] not in formatted_numbers :    # Conditional for if the number is not already in formatted_numbers

            formatted_numbers.append(numbers[i])    # Adds said number to new list

    print("Formatted with no duplicates : ", formatted_numbers)     # Prints this step for checking it works as expected

    return sorted(formatted_numbers, reverse = True)                # Returns fully formatted list


if __name__ == '__main__':                                              # Runs the code when file runs as a script

    # Generates list of 10 numbers between 1 and 100, allowing duplicates :
    number_list = np.random.choice(100, size = 10, replace = True)

    print("Generated list: ", number_list)            # Prints generated list to compare that functions work as expected

    formatted_list = format_number_list(number_list)    # Calls formatting function to generated list

    print("Formatted list : ", formatted_list)          # Prints formatted list to terminal



