from helper_functions import ProblemStatement
ps = ProblemStatement()


ping_pong = 10
pip = 100

class Code_Problems:
    def __init__(self):
        self.question = {
            1: self.one, 2: self.two, 3: self.three, 4: self.four, 5: self.five, 6: self.six, 7: self.seven, 8: self.eight, 9: self.nine, 10: self.ten, 11: self.eleven, 12: self.twelve, 13: self.thirteen, 14: self.fourteen, 15: self.fifteen, 16: self.sixteen, 17: self.seventeen, 18: self.eighteen, 19: self.nineteen, 20: self.twenty, 21: self.twenty_one, 22: self.twenty_two, 23: self.twenty_three, 24: self.twenty_four, 25: self.twenty_five, 26: self.twenty_six, 27: self.twenty_seven, 28: self.twenty_eight, 29: self.twenty_nine,
            
            30: self.fix_me_1, 31: self.fix_me_2, 32: self.fix_me_3, 33: self.fix_me_4, 34: self.fix_me_5, 35: self.fix_me_6, 36: self.fix_me_7, 37: self.fix_me_8, 38: self.fix_me_9, 39: self.fix_me_10,
            
            40: self.final_1, 41: self.final_2, 42: self.final_3
        }
        
    def run_problem(self, problem_number, *args, **kwargs):
        if problem_number in self.question:
            sanitized_args = self._sanitize_args(args, problem_number)
            # self.problem_dict[problem_number](sanitized_args, **kwargs)
            self.question[problem_number]()
        else:
            print("Problem number not found. Please choose a valid problem number.")
    
    def _sanitize_args(self, args, problem_number):
        """Sanitize and validate input arguments."""
        # if problem_number == 1:
        #     if isinstance(args[0], str):
        #         args[0] = args[0].strip()

        # if not args:
        #     return None

        return args
        
        
    """
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

    def five(self):
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

    def seven(self, to_generate, max_bound):
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

    def nine(self):
        ps.display(9)
        """
        Add your code here.
        """

        return

    def ten(self, phi, tolerance):
        ps.display(10)
        """
        Add your code here.
        """
        def recurse_golden_ratio(phi, tolerance):
            return 


        return recurse_golden_ratio(phi, tolerance)

    def eleven(self, nth_fib_digit):
        ps.display(11)
        """
        Add your code here.
        """
        def recursive_fibonacci(n):
            return
        

        return recursive_fibonacci(nth_fib_digit)

    def twelve(self, nth_fib_digit):
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


    def fourteen(self, num_rows):
        ps.display(14)
        """
        Add your code here.
        """

        return False #return True when you believe you have the correct output.

    def fifteen(self, asc=True):
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

    def seventeen(self, stories=1, dimensions=[], triangle_height=0):
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

    def nineteen(self):
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
        
    def twenty(self, sentence, clear_text_word):
        ps.display(20)
        """
        Add your code here.
        """

        return 'unshifted sentence', 'number'

    def twenty_one(self, a, b):
        ps.display(21)
        """
        Add your code here.
        """

        return

    def twenty_two(self, two_dimensional_list):
        ps.display(22)
        """
        Add your code here.
        """

        return

    def twenty_three(self, two_dimensional_list):
        ps.display(23)
        """
        Add your code here.
        """
        def recursive_spiral(): # what do you need to pass in here?
            return

        return recursive_spiral()

    def twenty_four(self, sentence):
        ps.display(24)
        """
        Add your code here.
        """

        return

    def twenty_five(self, people_who_own_cars):
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

    def twenty_six(self, people_who_may_own_cars):
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

    

    def twenty_eight(self):
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
        ping_or_pong = []

        return ping_or_pong





    def fix_me_1(self, list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
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

    def fix_me_2(list=[1, 3, 6, 5, 5]):
        ps.display("rest")
        """
        reverse a list then print the reversed list. use insert and pop to do this
        
        error is one line, find and fix it.
        """
        arr = list
        for i in arr:
            arr.insert(i, arr.pop(-1))
            
        return arr

    def fix_me_3(self, left=[1, 3, 5], right=[2, 4, 6, 7, 8]):
        ps.display("rest")
        """
        combine two lists, interchanging which index to take. prioritize left side.
        
        3 errors here, find and fix them. (uncomment the code to start working)
        """
        
        combined = []
        for i in range(100):
            # combined.append(?) if i ?? len(left) else None
            # combined.append(?) if i ?? len(right) else None
            pass
            
        return combined

    def fix_me_4(self, number):
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

    def fix_me_5(self, keys=["a", "b", "c", "4"], values=[1, 2, 3, "d"]):
        ps.display("rest")
        """
        Given 2 lists, create a dictionary.
        
        FOR THIS ONE, hard code the 'error count' to how many errors you find!
        """
        error_count = 9001
        
        new_dict = dict(zip(keys, values))
        
        return new_dict, error_count

    def fix_me_6(self, name="John Doe"):
        ps.display("rest")
        """
        given a string, output first_letter_of_lastname. firstname.
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
                return "base case reached"
            else:
                return recursive_function(n - 1)

        return recursive_function(100)

    def fix_me_9(self, value=20):
        pip = value

        ps.display("rest")
        """
        the yell function is missing something. it should return "AAAA" if pip is less than 5, and "OOOO" if pip is greater than or equal to 5. find and fix the error.
        """
        def yell():
            return "AAAA" if pip < 5 else "OOOO"
        
        return yell() #should be OOOO

    def fix_me_10(self, totally_a_number="teehee"):
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
            print(f"result is currently: {result1}, while on number: {i}")
        
        result2 = 0
        # while loop here

        return True if result1 == result2 else False

    def final_2(self):
        import random
        random.seed(10)
        arr = [x for x in random.sample(range(1, 100), 30)]
        ps.display("final")
        """
        Turn this iterative function into a recursive function! woooo!
        """
        
        def iterative_binary_search(arr, target):
            left, right = 0, len(arr) - 1
            target = 50
            
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    result1 = mid
                    break
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        
        
        
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
