"""
Do not look at this file
"""

class Hint_Manager:
    def __init__(self):
        self.hint_dict = {
            1: ["You require a path to read the file, the path is: files/data_duo.txt, use the os.path.join() function.", "Reading the lines returns a list of strings. You'll need to convert each string to an integer.", "use 'with open(PATH, 'r') as f:' to read the file, and then 'lines = f.readlines()' to get the lines of the file."],
            2: ["The path to read the file is: files/data_tri.txt", "The product (or multiplication) is done via the * (asterisk/star) operator.", "use 'with open(PATH, 'r') as f:' to read the file, and then 'lines = f.readlines()' to get the lines of the file."],
            3: ["The path to read the file is: files/data_solo.txt", "The factorial of a number n is the product of all positive integers less than or equal to n. Since we are doing repetition, use a loop.", "use 'with open(PATH, 'r') as f:' to read the file, and then 'lines = f.readlines()' to get the lines of the file."],
            4: ["The path to read the file is: files/grades.csv", "you will need to import the csv module (WITHIN THE FUNCTION SCOPE).", "You should read and save all the contents of the file in a variable before writing the contents to a new file.", "use 'with open(PATH, 'r') as f:' and csv.reader() to read the file, use 'with open(PATH, 'w', newline='') as f:' and csv.writer(delimiter=',') to write the file, and remember to calculate the average grade for each student. before writing."],
            5: ["The path to write the file is: files/output.csv", "You need to create a CSV writer object using csv.writer().", "use 'with open(PATH, 'w', newline='') as f:' to write the file, and then use writer.writerow() to write each row."],
            6: ["The path to read the file is: files/data_duo.txt", "The difference of two integers a and b can be calculated as a - b.", "use 'with open(PATH, 'r') as f:' to read the file, and then 'lines = f.readlines()' to get the lines of the file."],
            7: ["Import the random module, and use random.seed(10), make sure the import is within the function.", "Use random.sample() [LOOK AT THE DOCUMENTATION] to generate unique random integers within a specified range.", "use 'with open(PATH, 'w') as f:' to write the file, and remember to convert the integers to strings before writing them to the file."],
            8: []
        }
        pass

    def get_hint(self, problem_number, hint_level):
        if problem_number in self.hint_dict:
            if 1 <= hint_level <= len(self.hint_dict[problem_number]):
                print(self.hint_dict[problem_number][hint_level - 1])
        else:
            print("Invalid problem number. Please choose a valid hint + hint level.")

    def ask_hint(self):
        print("\033[96m"+
            "Problems 1-29 have 3 hints, 30-40 have 2 hints, and 41-43 have 1 hint.\n Question [4, 8, 16, 17, 19, 20, 22, 28] all have 4 hint levels."+
            "\033[0m")
        
        user_input = input("Enter the problem you would like a hint for\n(1-29) for the main ones,\n(30-40) for the fix_me ones, and\n(41-43) for the final problems!\nYou will be asked which hint level you want (bigger number = better hint).\n\nExample, 'i need a hint for problem 4, and i want a level 2 hint' -> '4 2' (SPACE SEPARATED): ")

        try:
            hint, level = user_input.strip().split()
        except ValueError:
            print("Invalid input format. Please enter the problem number and hint level separated by a space.")
            return
        except Exception as e:
            print(f"An error occurred: {e}")
            return

        try:
            hint = int(hint)
            level = int(level)
        except ValueError:
            print("Invalid input. Please enter numbers that are space separated.")
            return
        except Exception as e:
            print(f"An error occurred TRY AGAIN: {e}")
            return
        
        print("-"*20)
        self.get_hint(hint, level)
        print("-"*20, end="\n\n")
        
    
    
