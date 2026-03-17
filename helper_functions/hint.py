"""
Do not look at this file
"""

class Hint:
    def __init__(self):
        self.hint_dict = {
            1: ["hint 1 for problem 1", "hint 2 for problem 1", "hint 3 for problem 1"],
            2: ["hint 1 for problem 2", "hint 2 for problem 2", "hint 3 for problem 2"],
            3: ["hint 1 for problem 3", "hint 2 for problem 3", "hint 3 for problem 3"],
            4: ["hint 1 for problem 4", "hint 2 for problem 4", "hint 3 for problem 4"],
            5: ["hint 1 for problem 5", "hint 2 for problem 5", "hint 3 for problem 5"]
        }
        pass

    def get_hint(self, problem_number, hint_level):
        if problem_number in self.hint_dict:
            if 1 <= hint_level <= len(self.hint_dict[problem_number]):
                print(self.hint_dict[problem_number][hint_level - 1])
        else:
            print("Invalid problem number. Please choose a valid hint + hint level.")

    def hint(self):
        print(""""
            Problems 1-29 have 3 hints, 30-40 have 2 hints, and 41-43 have 1 hint. Question [8, 16, 17, 19, 20, 22, 28] all have 4 hint levels.  
            """)
        
        input = input("Enter the problem you would like a hint for (1-29) for the main ones, (30-40) for the fix_me ones, and (41-43) for the final problems!\n You will be asked which hint level you want (bigger number = better hint).\n\n Example, 'i need a hint for problem 4, and i want a level 2 hint' -> '4 2' (SPACE SEPARATED): ")

        hint, level = input.split().strip()

        try:
            hint = int(hint)
            level = int(level)
        except ValueError:
            print("Invalid input. Please enter a valid format.")
            pass
        except Exception as e:
            print(f"An error occurred TRY AGAIN: {e}")
            pass
        
    
    
