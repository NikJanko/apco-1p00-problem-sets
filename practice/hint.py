"""
Run this file to get hints for the practice problems.
When you run this file, you will get the ability to write in what level of hint you want, and to which problem.
If you are really stuck, you may email:

nj21mf@brocku.ca

Run this program, input the problem and hint level,
Do not scroll down, all the hints are written in plain text.




















































































































"""

def hint():
    print("Welcome to the hint system!")
    print("Please enter the problem number you want a hint for (1-5):")
    problem_number = input()
    print("Please enter the level of hint you want (1-3):")
    hint_level = input()
    
    if problem_number == "1":
        if hint_level == "1":
            print("Hint 1 for Problem 1: Think about how to use a loop to iterate through the numbers.")
        elif hint_level == "2":
            print("Hint 2 for Problem 1: Consider using a conditional statement to check for even numbers.")
        elif hint_level == "3":
            print("Hint 3 for Problem 1: You can use the modulus operator (%) to determine if a number is even.")
        else:
            print("Invalid hint level. Please choose between 1 and 3.")
    
    elif problem_number == "2":
        if hint_level == "1":
            print("Hint 1 for Problem 2: Think about how to use a list to store your data.")
        elif hint_level == "2":
            print("Hint 2 for Problem 2: Consider using a function to organize your code.")
        elif hint_level == "3":
            print("Hint 3 for Problem 2: You can use the built-in 'sum' function to calculate the total.")
        else:
            print("Invalid hint level. Please choose between 1 and 3.")
    
    # Add similar blocks for problems 3, 4, and 5 as needed.
    
    else:
        print("Invalid problem number. Please choose between 1 and 5.")


if __name__ == "__main__":
    hint()