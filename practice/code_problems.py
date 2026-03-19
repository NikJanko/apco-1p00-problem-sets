import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from helper_functions import ProblemStatement
from helper_functions import verify_environment as VE
from helper_functions import hint as hint
import io
import inspect

ps = ProblemStatement()

golden_ratio = 1.61803398875
ping_pong = 10
pip = 100


"""
Start coding at the very bottom "if __name__ == "__main__":" section.
"""


class Code_Problems:
    def __init__(self):
        self.question = {
            1: self.one, 2: self.two, 3: self.three, 4: self.four, 5: self.five, 6: self.six, 7: self.seven, 8: self.eight, 9: self.nine, 10: self.ten, 11: self.eleven, 12: self.twelve, 13: self.thirteen, 14: self.fourteen, 15: self.fifteen, 16: self.sixteen, 17: self.seventeen, 18: self.eighteen, 19: self.nineteen, 20: self.twenty, 21: self.twenty_one, 22: self.twenty_two, 23: self.twenty_three, 24: self.twenty_four, 25: self.twenty_five, 26: self.twenty_six, 27: self.twenty_seven, 28: self.twenty_eight, 29: self.twenty_nine,
            
            30: self.fix_me_1, 31: self.fix_me_2, 32: self.fix_me_3, 33: self.fix_me_4, 34: self.fix_me_5, 35: self.fix_me_6, 36: self.fix_me_7, 37: self.fix_me_8, 38: self.fix_me_9, 39: self.fix_me_10,
            
            40: self.final_1, 41: self.final_2, 42: self.final_3
        }
        
    def run_problem(self, problem_number, *args, **kwargs):
        try:
            if problem_number in self.question:
                method = self.question[problem_number]
                sanitized_args = self._sanitize_args(args, method)
                
                # Check if method accepts parameters beyond self
                sig = inspect.signature(method)
                params = [p for p in sig.parameters.values() if p.name != 'self']
                
                # Only pass arguments if method has parameters
                if params:
                    return method(*sanitized_args, **kwargs)
                else:
                    return method()
            else:
                print("\033[91mProblem number not found. Please choose a valid problem number.\033[0m")
        except (TypeError, ValueError) as e:
            if problem_number in range(30, 43):
                print(f"\033[91mError in problem {problem_number}: {e}. This is expected since this problem has intentional errors to fix. Please check your code and try again.\033[0m")
            else:
                print(f"\033[91mError: {e}. Please check the arguments you provided for problem {problem_number}.\033[0m")
    
    def _sanitize_args(self, args, method):
        """Sanitize and convert input arguments to match method parameter types."""
        if not args:
            return args
        
        sig = inspect.signature(method)
        params = [p for p in sig.parameters.values() if p.name != 'self']
        
        sanitized = []
        for i, arg in enumerate(args):
            if i >= len(params):
                # Extra arguments beyond parameters
                sanitized.append(arg)
                continue
            
            param = params[i]
            annotation = param.annotation
            
            # If no annotation, return as-is
            if annotation == inspect.Parameter.empty:
                sanitized.append(arg)
                continue
            
            # Convert to the expected type
            try:
                if annotation == int:
                    sanitized.append(int(arg))
                elif annotation == float:
                    sanitized.append(float(arg))
                elif annotation == str:
                    sanitized.append(str(arg))
                elif annotation == bool:
                    # Handle bool conversion sensibly
                    if isinstance(arg, str):
                        sanitized.append(arg.lower() in ['true', '1', 'yes', 'y'])
                    else:
                        sanitized.append(bool(arg))
                elif annotation == list:
                    if isinstance(arg, list):
                        sanitized.append(arg)
                    else:
                        sanitized.append([arg])
                elif annotation == dict:
                    if isinstance(arg, dict):
                        sanitized.append(arg)
                    else:
                        sanitized.append({})
                else:
                    # For other types, try to convert directly
                    sanitized.append(annotation(arg))
            except (ValueError, TypeError) as e:
                raise ValueError(f"\033[91mCannot convert argument '{arg}' to type {annotation.__name__}: {e}\033[0m")
        
        return tuple(sanitized)
        
    def print_all_problems(self, print_to_file: bool=False):
        if print_to_file:
            try:
                output_file = Path("./all_problems.txt").resolve()
                with open(output_file, "w") as f:
                    for num in sorted(self.question.keys()):
                        f.write(f"Problem {num}:\n{ps.display(num)}\n\n{'-'*50}\n\n")
                print("\033[92mAll problems have been printed to 'all_problems.txt'.\033[0m")
            except IOError as e:
                print(f"\033[91mError writing to file: {e}\033[0m")
            except Exception as e:
                print(f"\033[91mAn unexpected error occurred: {e}\033[0m")
                
                
        for num in sorted(self.question.keys()):
            if not print_to_file:
                print(f"\033[94mProblem {num}:\033[0m")
                print(ps.display(num))
                print("\n" + "-"*50 + "\n")
            else:
                break
        
        
        
    """
    START CODING Under HERE
    START CODING Under HERE
    START CODING Under HERE
    """ 
    

    def one(self):
        ps.display(1)
        """
        Add your code here.
        """
        
        return 

    def two(self):
        ps.display(2)
        """
        Add your code here.
        """

        return

    def three(self):
        ps.display(3)
        """
        Add your code here.
        """

        return

    def four(self):
        ps.display(4)
        """
        Add your code here.
        """

    def five(self, csv_additions: list=[['Jane', 0, 30],['Joe', 50, 40]]):
        ps.display(5)
        """
        Add your code here.
        """

        return

    def six(self):
        ps.display(6)
        """
        Add your code here.
        """

        return

    def seven(self, to_generate: int, max_bound: int):
        ps.display(7)
        """
        Add your code here.
        """

        return

    def eight(self):
        ps.display(8)
        """
        Add your code here.
        """

        return

    def nine(self, target: int=10):
        ps.display(9)
        """
        Add your code here.
        """

        return

    def ten(self, phi: float, tolerance: float):
        ps.display(10)
        """
        Add your code here.
        you may use the global variable 'golden_ratio' if you want.
        """
        def recurse_golden_ratio(phi, tolerance):
            return 


        return recurse_golden_ratio(phi, tolerance)

    def eleven(self, nth_fib_digit: int):
        ps.display(11)
        """
        Add your code here.
        """
        def recursive_fibonacci(n):
            return
        

        return recursive_fibonacci(nth_fib_digit)


    def twelve(self, nth_fib_digit: int):
        ps.display(12)
        """
        Add your code here.
        """

        return

    def thirteen(self):
        ps.display(13)
        """
        Add your code here.
        """

        return


    def fourteen(self, num_rows: int):
        ps.display(14)
        """
        Add your code here.
        """

        return False #return True when you believe you have the correct output.

    def fifteen(self, asc: bool=True):
        ps.display(15)
        """
        Add your code here.
        """

        return 

    def sixteen(self):
        ps.display(16)
        """
        Add your code here.
        """

        return

    def seventeen(self, stories: int=1, dimensions: list=[], triangle_height: int=0):
        ps.display(17)
        """
        Add your code here.
        """

        return

    def eighteen(self):
        ps.display(18)
        """
        Add your code here.
        """
        cipher_map = {
            'A': 'Q',    'B': 'W',    'C': 'E',    'D': 'R',
            'E': 'T',    'F': 'Y',    'G': 'U',    'H': 'I',
            'I': 'O',    'J': 'P',    'K': 'A',    'L': 'S',
            'M': 'D',    'N': 'F',    'O': 'G',    'P': 'H',
            'Q': 'J',    'R': 'K',    'S': 'L',    'T': 'Z',
            'U': 'X',    'V': 'C',    'W': 'V',    'X': 'B',
            'Y': 'N',    'Z': 'M',    ' ': '-',    '-': ' '
        }
        
        
        

        return

    def nineteen(self, input: str="possiblyFilePath"):
        ps.display(19)
        """
        Add your code here.
        """
        cipher_map = {
            'A': 'Q',    'B': 'W',    'C': 'E',    'D': 'R',
            'E': 'T',    'F': 'Y',    'G': 'U',    'H': 'I',
            'I': 'O',    'J': 'P',    'K': 'A',    'L': 'S',
            'M': 'D',    'N': 'F',    'O': 'G',    'P': 'H',
            'Q': 'J',    'R': 'K',    'S': 'L',    'T': 'Z',
            'U': 'X',    'V': 'C',    'W': 'V',    'X': 'B',
            'Y': 'N',    'Z': 'M',    ' ': '-',    '-': ' '
        }
        

        return
        
    def twenty(self, sentence: str="llohe rld!wo tsle deco", clear_text_word: str="lets"):
        ps.display(20)
        """
        Add your code here.
        """

        return 'unshifted sentence', 'number'

    def twenty_one(self, a: int, b: int):
        ps.display(21)
        """
        Add your code here.
        """

        return

    def twenty_two(self, two_dimensional_list: list=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]):
        ps.display(22)
        """
        Add your code here.
        """

        return

    def twenty_three(self, two_dimensional_list: list=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]):
        ps.display(23)
        """
        Add your code here.
        """
        def recursive_spiral(): # what do you need to pass in here?
            return

        return recursive_spiral()

    def twenty_four(self, sentence: str):
        ps.display(24)
        """
        Add your code here.
        """

        return

    def twenty_five(self, people_who_own_cars: list=[["jimmy", "honda", "civic", 2010, "red"]]):
        ps.display(25)
        """
        Add your code here.
        """
        # class Vehicle:
        #    init code here
        #    give_string function code here

        set_up_class = []
        class_results = []
        # set_up_class.append(Vehicle("john", "Toyota", "Camry", 2020))
        
        # class_results.append(set_up_class[0].give_string())
        
        return class_results

    def twenty_six(self, people_who_may_own_cars: list=[["jimmy", "honda", "civic", '2010x', "red"]]):
        ps.display(26)
        """
        Add your code here.
        
        (see code in twenty_five)
        """

        return

    def twenty_seven(self):
        ps.display(27)
        """
        Add your code here.
        """

        return

    def twenty_eight(self, game = [1, 2, 3, 2, 1]):
        ps.display(28)
        """
        Add your code here.
        """
        

        return False # return True when you believe you have the correct answer, (this is because global variables need to be tested differently)

    def twenty_nine(self):
        ps.display(29)
        """
        Add your code here.
        """
        ping_or_pong_list = []

        return ping_or_pong_list





    def fix_me_1(self, list: list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
        ps.display("rest")
        """
        If we encounter a multiple of 8, double the next numbers until the next multiple of 8.
        if we encounter an odd number, halve it. 
        
        1-line error here. find and fix it.
        """
        arr = list
        
        for i in range(len(arr)):
            if arr[i] % 8 == 0:
                for j in range(1, len(arr)):
                    if arr[j] % 8 == 0:
                        break
                    arr[j] *= 2
            elif arr[i] % 2 == 1:
                arr[i] /= 2
        
        return arr

    def fix_me_2(list: list=[1, 3, 6, 5, 5]):
        ps.display("rest")
        """
        reverse a list then print the reversed list. use insert and pop to do this
        
        error is one line, find and fix it.
        """
        arr = list
        for i in arr:
            arr.insert(i, arr.pop(-1))
            
        return arr

    def fix_me_3(self, left: list=[1, 3, 5], right: list=[2, 4, 6, 7, 8]):
        ps.display("rest")
        """
        combine two lists, interchanging which index to take. prioritize left side.
        
        4 errors here, find and fix them. (uncomment the code to start working)
        """
        
        combined = []
        for i in range(100):
            # if i ? ?:
            #     combined.append(?))
            # if i ? ?:
            #     combined.append(?)
            pass
            
        return combined

    def fix_me_4(self, number: int):
        import random
        ps.display("rest")
        """
        simplify this code. it is supposed to return the same thing as it currently does, but it is very messy and has some unnecessary parts. find and remove the unnecessary parts, and simplify the code as much as possible.
        """
        Regina_George = abs(int(number))
        
        misunderstanding = random.randint(1000, 9999)
        
        flippy_doo_dad = True
        for _ in range(misunderstanding):
            flippy_doo_dad = not flippy_doo_dad
            
        mean_girls_movie_reference = Regina_George + misunderstanding
        
        new_problem = flippy_doo_dad
        
        while (mean_girls_movie_reference > 0):
            new_problem = bool(int(new_problem)^1)
            mean_girls_movie_reference -= len(list("1"))
            
        return 1 if new_problem else 0

    def fix_me_5(self, keys: list=["a", "b", "c", 4], values: list=[1, 2, 3, "d"]):
        ps.display("rest")
        """
        Given 2 lists, create a dictionary.
        
        FOR THIS ONE, hard code the 'error count' to how many errors you find!
        """
        error_count = 9001
        
        new_dict = dict(zip(keys, values))
        
        return new_dict, error_count

    def fix_me_6(self, name: str="John Doe"):
        ps.display("rest")
        """
        given a string, output first_letter_of_lastname. firstname.
        there is one error
        """
        firstname, lastname = name.split()    
        introduction = f"{lastname}. {firstname}."
    
        return introduction

    def fix_me_7(self):
        ps.display("rest")
        """
        simplify this code.
        this code should always return the string "final result".
        """
        
        def first_function():
            def second_function():
                def third_function():
                    def fourth_function():
                        def fifth_function():
                            return "final result"
                        return fifth_function()
                    return fourth_function()
                return third_function()
            return second_function()            
        return first_function()
        

    def fix_me_8(self):
        ps.display("rest")
        """
        this does a thing, there is a single error tho. find and fix it.
        """
        def recursive_function(n):
            if n > 0:
                return n
            else:
                return recursive_function(n - 1)

        return recursive_function(100)

    def fix_me_9(self, value: int=20):
        global pip
        pip = value

        ps.display("rest")
        """
        the yell function is missing something. it should return "AAAA" if pip is less than 5, and "OOOO" if pip is greater than or equal to 5. find and fix the error.
        """
        def yell():
            return "AAAA" if pip < 5 else "OOOO"
        
        return yell() #should be OOOO

    def fix_me_10(self, totally_a_number: str="teehee"):
        ps.display("rest")
        """
        this should have some error handling, return 'not a number' if the input is not a number, otherwise return the number (VALUE ERROR)
        """
        
        num = totally_a_number
        num = int(num)     

        return num

    def final_1(self):
        ps.display("final")
        """
        turn this for loop into a while loop.
        """
        result1 = 0
        for i in range(10, 100, 2):
            result1 += i
            # print(f"result is currently: {result1}, while on number: {i}") # this can be uncommented for your aid
        
        result2 = 0
        # while loop here

        return True if result1 == result2 else False

    def final_2(self):
        import random
        random.seed(10)
        arr = [x for x in random.sample(range(1, 100), 30)]
        ps.display("final")
        """
        Turn this iterative function into a recursive function! woooo! (return -1 if not found.)
        """
        
        def iterative_binary_search(arr, target):
            left, right = 0, len(arr) - 1
            target = 50
            
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1        
        
        def recursive_binary_search(arr, left, right, target):
            # CONVERT ME TO RECURSIVE BINARY SEARCH
            return
        
        return True if iterative_binary_search(arr, 50) == recursive_binary_search(arr, 0, len(arr) - 1, 50) else False

    def final_3(self):
        ps.display("final")
        """
        this list is a dictionary, convert it back into two lists.
        """
        keys_list = ["Canada", "USA", "Mexico", "UK", "France", "Germany", "Italy", "Spain", "Portugal", "Netherlands"]
        values_list = [6, 3, 6, 2, 6, 7, 5, 5, 8, 11]
        
        countries_dict = dict(zip(keys_list, values_list))
        
        # now convert the dict back into two list, one for keys, and the other for values.
        
        dict_keys_list = []
        dict_values_list = []

        return True if (True if keys_list == dict_keys_list else False) and (True if values_list == dict_values_list else False) else False



"""
This is where you will be able to run your code!
"""

if __name__ == "__main__":
    verify = VE.Verify_Environment()
    verify.verify_environment(dir_name=verify.dir_name, dir_name2=verify.dir_name2)
    problems = Code_Problems()
    hint = hint.Hint_Manager()
    """
    WORKFLOW:
    1. Uncomment a problem below to run it (problems 1-29 are regular, 30-39 are 'fix me', 40-42 are final) 
        - the problem statement will print in the terminal, in which, you'll know what to do.
    2. Write code in code_problems.py
    3. Use hints with hint.ask_hint() if stuck (try before checking solutions folder) 
        - This is open book, (but dont use AI).
    4. When you complete all problems, go to the Test_Cases/test.py file and run it up! 
        - a history will be stored in 'history.txt' 
        - you'll be testing your solutions against mine.
        
    Questions are rated by difficulty, higher level the more involved or harder the problem is. Do not be sad or discouraged if you find a problem hard, just try your best and use the resources available to you. The goal is to learn!
    
    GUIDELINES:
    - Problems should print AND return results (non-file problems)
    - File-generation problems only need to create files in ../generated_files
    - Don't use AI to generate code; use notes, hints, docs, StackOverflow, and solutions folder as reference
    - For debugging: use verify.fix_files() to reset files/folders (will clear generated_files)
    """    
    # CHOOSE & RUN A PROBLEM :
    # problems.run_problem(7, 'arguments here if applicable', 'more than 1 argument')
        
    
    # GET A HINT :
    # hint.ask_hint()
    
    # RESET FILES/FOLDERS (WARNING: clears both folders) :
    # verify.fix_files()