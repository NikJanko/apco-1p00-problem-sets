from helper_functions import ProblemStatement
import inspect

ps = ProblemStatement()

golden_ratio = 1.61803398875
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
        
        
    """
    START CODING Under HERE
    """
    

    def one(self):
        ps.display(1)
        """
        Add your code here.
        """
        result = []
        with open('../files/data_duo.txt', 'r') as f:
            for line in f:
                parts = line.strip().split()
                result.append(int(parts[0]) + int(parts[1]))
        return result

    def two(self):
        ps.display(2)
        """
        Add your code here.
        """
        result = []
        with open('../files/data_tri.txt', 'r') as f:
            for line in f:
                parts = line.strip().split()
                result.append(int(parts[0]) * int(parts[1]) * int(parts[2]))
        return result

    def three(self):
        ps.display(3)
        """
        Add your code here.
        """
        def factorial(n):
            if n <= 1:
                return 1
            return n * factorial(n - 1)

        result = []
        with open('../files/data_solo.txt', 'r') as f:
            for line in f:
                result.append(factorial(int(line.strip())))
        return result

    def four(self):
        ps.display(4)
        """
        Add your code here.
        """
        import csv

        result = []
        with open('../files/grades.csv', 'r') as f:
            reader = csv.reader(f)
            with open('./generated_files/grades_output.csv', 'w', newline='') as out:
                writer = csv.writer(out)
                writer.writerow(['Last Name', 'First Name', 'Assignment 1', 'Assignment 2', 'Average'])
                for row in reader:
                    lastname = row[0].strip()
                    firstname = row[1].strip()
                    grade1 = int(row[2].strip())
                    grade2 = int(row[3].strip())
                    avg = (grade1 + grade2) / 2
                    result.append(f"{firstname} {lastname}: {avg}")
                    writer.writerow([lastname, firstname, grade1, grade2, avg])
        return result

    def five(self, csv_additions: list=[['Jane', 0, 30],['Joe', 50, 40]]):
        ps.display(5)
        """
        Add your code here.
        """
        import csv

        with open('./generated_files/output.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'Assignment1', 'Assignment2'])
            for row in csv_additions:
                writer.writerow(row)
        return 0

    def six(self):
        ps.display(6)
        """
        Add your code here.
        """
        result = []
        with open('../files/data_duo.txt', 'r') as f:
            for line in f:
                parts = line.strip().split()
                result.append(int(parts[0]) - int(parts[1]))
        return result

    def seven(self, to_generate: int, max_bound: int):
        ps.display(7)
        """
        Add your code here.
        """
        import random

        random.seed(10)
        numbers = random.sample(range(1, max_bound + 1), to_generate)
        with open('./generated_files/recur.txt', 'w') as f:
            for num in numbers:
                f.write(str(num) + '\n')
        return numbers

    def eight(self):
        ps.display(8)
        """
        Add your code here.
        """
        def recursive_sort(arr, n, asc=True):
            if n == 1:
                return
            for i in range(n - 1):
                if (asc and arr[i] > arr[i + 1]) or (not asc and arr[i] < arr[i + 1]):
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            recursive_sort(arr, n - 1, asc)

        with open('./generated_files/recur.txt', 'r') as f:
            arr = [int(line.strip()) for line in f]

        recursive_sort(arr, len(arr), asc=True)

        with open('./generated_files/recur2.txt', 'w') as f:
            for num in arr:
                f.write(str(num) + '\n')

        return arr

    def nine(self, target: int=10):
        ps.display(9)
        """
        Add your code here.
        """
        def recursive_binary_search(arr, left, right, target):
            if left > right:
                return -1
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                return recursive_binary_search(arr, mid + 1, right, target)
            else:
                return recursive_binary_search(arr, left, mid - 1, target)

        with open('./generated_files/recur2.txt', 'r') as f:
            arr = [int(line.strip()) for line in f]

        return recursive_binary_search(arr, 0, len(arr) - 1, target)

    def ten(self, phi: float, tolerance: float):
        ps.display(10)
        """
        Add your code here.
        you may use the global variable 'golden_ratio' if you want.
        """
        def recurse_golden_ratio(phi, tolerance):
            next_phi = 1 + 1 / phi
            if abs(next_phi - phi) < tolerance:
                return next_phi
            return recurse_golden_ratio(next_phi, tolerance)

        return recurse_golden_ratio(phi, tolerance)

    def eleven(self, nth_fib_digit: int):
        ps.display(11)
        """
        Add your code here.
        """
        def recursive_fibonacci(n):
            if n <= 1:
                return n
            return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

        return recursive_fibonacci(nth_fib_digit)


    def twelve(self, nth_fib_digit: int):
        ps.display(12)
        """
        Add your code here.
        """
        if nth_fib_digit <= 1:
            return nth_fib_digit
        a, b = 0, 1
        for _ in range(2, nth_fib_digit + 1):
            a, b = b, a + b
        return b

    def thirteen(self):
        ps.display(13)
        """
        Add your code here.
        """
        result = []
        with open('../files/data_quad.txt', 'r') as f:
            for line in f:
                parts = line.strip().split()
                nums = [int(p) for p in parts]
                total = 0
                for n in nums:
                    total += n
                result.append(total / len(nums))
        return result


    def fourteen(self, num_rows: int):
        ps.display(14)
        """
        Add your code here.
        """
        import random

        random.seed(10)
        with open('./generated_files/recur2.txt', 'w') as f:
            generated = set()
            for row in range(num_rows):
                row_nums = []
                while len(row_nums) < 10:
                    num = random.randint(1, 100)
                    if num not in generated:
                        row_nums.append(num)
                        generated.add(num)
                f.write(' '.join([str(n) for n in row_nums]) + '\n')

        return True

    def fifteen(self, asc: bool=True):
        ps.display(15)
        """
        Add your code here.
        """
        with open('./generated_files/recur2.txt', 'r') as f:
            rows = []
            for line in f:
                parts = line.strip().split()
                row = [int(p) for p in parts]
                rows.append(sorted(row, reverse=not asc))

        with open('./generated_files/recur3.txt', 'w') as f:
            for row in rows:
                f.write(' '.join([str(n) for n in row]) + '\n')

        return rows

    def sixteen(self):
        ps.display(16)
        """
        Add your code here.
        """
        with open('./generated_files/recur2.txt', 'r') as f:
            mode_dict = {}
            for line in f:
                parts = line.strip().split()
                for p in parts:
                    num = int(p)
                    mode_dict[num] = mode_dict.get(num, 0) + 1
        return mode_dict

    def seventeen(self, stories: int=1, dimensions: list=[], triangle_height: int=0):
        ps.display(17)
        """
        Add your code here.
        """
        if not dimensions or len(dimensions) < 3:
            return 0, 0

        length, width, height = dimensions[0], dimensions[1], dimensions[2]

        wall_area = 2 * (length * height) + 2 * (width * height)
        wall_area *= stories

        floor_area = length * width

        roof_length = length + 2
        roof_width = width + 2
        roof_area = roof_length * triangle_height + 0.5 * roof_width * triangle_height

        total_area = wall_area + floor_area + roof_area

        return round(total_area, 2), round(roof_area, 2)

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

        decode_map = {v: k for k, v in cipher_map.items()}

        with open('../files/cipher_passage.txt', 'r') as f:
            encoded = f.read()

        decoded = ''.join(decode_map.get(c, c) for c in encoded)
        return decoded

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

        import os
        if os.path.isfile(input):
            with open(input, 'r') as f:
                input = f.read()

        encoded = ''.join(cipher_map.get(c.upper(), c) for c in input)
        return encoded
        
    def twenty(self, sentence: str="llohe rld!wo tsle deco", clear_text_word: str="lets"):
        ps.display(20)
        """
        Add your code here.
        """
        words = sentence.split()
        magic_shift = None

        for word in words:
            for shift in range(len(word)):
                if shift == 0:
                    rotated = word
                else:
                    rotated = word[-shift:] + word[:-shift]
                if rotated.lower() == clear_text_word.lower():
                    magic_shift = shift
                    break
            if magic_shift is not None:
                break

        if magic_shift is None:
            return sentence, 0

        descrambled_words = []
        for word in words:
            if magic_shift == 0:
                rotated = word
            else:
                rotated = word[-magic_shift:] + word[:-magic_shift]
            descrambled_words.append(rotated)

        descrambled_sentence = ' '.join(descrambled_words)
        return descrambled_sentence, magic_shift

    def twenty_one(self, a: int, b: int):
        ps.display(21)
        """
        Add your code here.
        """
        result = 0
        for _ in range(b):
            result += a
        return result

    def twenty_two(self, two_dimensional_list: list=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]):
        ps.display(22)
        """
        Add your code here.
        """
        result = []
        if not two_dimensional_list:
            return result

        top, bottom = 0, len(two_dimensional_list)
        left, right = 0, len(two_dimensional_list[0])

        while top < bottom and left < right:
            for col in range(left, right):
                result.append(two_dimensional_list[top][col])
            top += 1

            for row in range(top, bottom):
                result.append(two_dimensional_list[row][right - 1])
            right -= 1

            if top < bottom:
                for col in range(right - 1, left - 1, -1):
                    result.append(two_dimensional_list[bottom - 1][col])
                bottom -= 1

            if left < right:
                for row in range(bottom - 1, top - 1, -1):
                    result.append(two_dimensional_list[row][left])
                left += 1

        return result

    def twenty_three(self, two_dimensional_list: list=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]):
        ps.display(23)
        """
        Add your code here.
        """
        def recursive_spiral(matrix, top, bottom, left, right, result):
            if top > bottom or left > right:
                return
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
            recursive_spiral(matrix, top, bottom, left, right, result)

        result = []
        recursive_spiral(two_dimensional_list, 0, len(two_dimensional_list) - 1, 0, len(two_dimensional_list[0]) - 1, result)
        return result

    def twenty_four(self, sentence: str):
        ps.display(24)
        """
        Add your code here.
        """
        vowels = 'aeiouAEIOU'
        vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

        for char in sentence:
            if char in vowels:
                vowel_count[char.lower()] += 1

        result_string = ''.join(char for char in sentence if char not in vowels)
        return result_string, vowel_count

    def twenty_five(self, people_who_own_cars: list=[["jimmy", "honda", "civic", 2010, "red"]]):
        ps.display(25)
        """
        Add your code here.
        """
        class Vehicle:
            def __init__(self, owner, vehicle_type, model, year, color):
                self.owner = owner
                self.vehicle_type = vehicle_type
                self.model = model
                self.year = year
                self.color = color

            def give_string(self):
                return f"{self.owner} owns a {self.color} {self.vehicle_type} from {self.year}."

        set_up_class = []
        class_results = []

        for person in people_who_own_cars:
            vehicle = Vehicle(person[0], person[1], person[2], person[3], person[4])
            set_up_class.append(vehicle)
            class_results.append(vehicle.give_string())

        return class_results

    def twenty_six(self, people_who_may_own_cars: list=[["jimmy", "honda", "civic", '2010x', "red"]]):
        ps.display(26)
        """
        Add your code here.
        
        (see code in twenty_five)
        """
        class Vehicle:
            def __init__(self, owner, vehicle_type, model, year, color):
                if not isinstance(year, int) or year > 2025:
                    raise ValueError("Invalid year. Year must be an integer and cannot be in the future.")
                if vehicle_type not in ['car', 'truck', 'bus', 'motorcycle']:
                    raise ValueError("Invalid type. Type must be one of car, truck, bus or motorcycle.")
                self.owner = owner
                self.vehicle_type = vehicle_type
                self.model = model
                self.year = year
                self.color = color

            def give_string(self):
                return f"{self.owner} owns a {self.color} {self.vehicle_type} from {self.year}."

        class_results = []
        for person in people_who_may_own_cars:
            try:
                vehicle = Vehicle(person[0], person[1], person[2], int(person[3]), person[4])
                class_results.append(vehicle.give_string())
            except ValueError as e:
                class_results.append(f"Error: {e}")
            except Exception as e:
                class_results.append(f"Error: {e}")

        return class_results

    def twenty_seven(self):
        ps.display(27)
        """
        Add your code here.
        """
        result = []
        with open('../files/except.txt', 'r') as f:
            for line in f:
                value = line.strip()
                try:
                    result.append(int(value))
                except ValueError:
                    try:
                        result.append(float(value))
                    except ValueError:
                        result.append(value)
        return result

    def twenty_eight(self, game = [1, 2, 3, 2, 1]):
        ps.display(28)
        """
        Add your code here.
        """
        global ping_pong

        def increment():
            global ping_pong
            ping_pong += 1

        def decrement():
            global ping_pong
            ping_pong -= 1

        increment()
        for i in range(1, len(game)):
            if game[i] > game[i - 1]:
                increment()
            elif game[i] < game[i - 1]:
                decrement()

        return ping_pong

    def twenty_nine(self):
        ps.display(29)
        """
        Add your code here.
        """
        global ping_pong
        ping_pong = 0

        ping_or_pong_list = []
        with open('../files/data_quad.txt', 'r') as f:
            for line in f:
                ping_pong = 0
                parts = line.strip().split()
                nums = [int(p) for p in parts]
                self.twenty_eight(nums)
                if ping_pong > 0:
                    ping_or_pong_list.append('ping')
                elif ping_pong < 0:
                    ping_or_pong_list.append('pong')
                else:
                    ping_or_pong_list.append('ping pong')

        return ping_or_pong_list





    def fix_me_1(self, list: list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
        ps.display("rest")
        """
        If we encounter a multiple of 8, double the next numbers until the next multiple of 8.
        if we encounter an odd number, halve it. 
        
        1-line error here. find and fix it.
        """
        arr = list.copy()
        
        for i in range(len(arr)):
            if arr[i] % 8 == 0:
                for j in range(i + 1, len(arr)):
                    if arr[j] % 8 == 0:
                        break
                    arr[j] *= 2
            elif arr[i] % 2 == 1:
                arr[i] /= 2
        
        return arr

    def fix_me_2(self, list: list=[1, 3, 6, 5, 5]):
        ps.display("rest")
        """
        reverse a list then print the reversed list. use insert and pop to do this
        
        error is one line, find and fix it.
        """
        arr = list.copy()
        for i in range(len(arr)):
            arr.insert(0, arr.pop(-1))
            
        return arr

    def fix_me_3(self, left: list=[1, 3, 5], right: list=[2, 4, 6, 7, 8]):
        ps.display("rest")
        """
        combine two lists, interchanging which index to take. prioritize left side.
        
        4 errors here, find and fix them. (uncomment the code to start working)
        """
        
        combined = []
        for i in range(max(len(left), len(right))):
            if i < len(left):
                combined.append(left[i])
            if i < len(right):
                combined.append(right[i])
            
        return combined

    def fix_me_4(self, number: int):
        import random
        ps.display("rest")
        """
        simplify this code. it is supposed to return the same thing as it currently does, but it is very messy and has some unnecessary parts. find and remove the unnecessary parts, and simplify the code as much as possible.
        """
        return int(abs(number) % 2 == 0)

    def fix_me_5(self, keys: list=["a", "b", "c", 4], values: list=[1, 2, 3, "d"]):
        ps.display("rest")
        """
        Given 2 lists, create a dictionary.
        
        FOR THIS ONE, hard code the 'error count' to how many errors you find!
        """
        error_count = 0
        
        new_dict = dict(zip(keys, values))
        
        return new_dict, error_count

    def fix_me_6(self, name: str="John Doe"):
        ps.display("rest")
        """
        given a string, output first_letter_of_lastname. firstname.
        there is one error
        """
        firstname, lastname = name.split()    
        introduction = f"{lastname[0]}. {firstname}."
    
        return introduction

    def fix_me_7(self):
        ps.display("rest")
        """
        simplify this code.
        this code should always return the string "final result".
        """
        return "final result"

    def fix_me_8(self):
        ps.display("rest")
        """
        this does a thing, there is a single error tho. find and fix it.
        """
        def recursive_function(n):
            if n <= 0:
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
            global pip
            return "AAAA" if pip < 5 else "OOOO"
        
        return yell() #should be OOOO

    def fix_me_10(self, totally_a_number: str="teehee"):
        ps.display("rest")
        """
        this should have some error handling, return 'not a number' if the input is not a number, otherwise return the number (VALUE ERROR)
        """
        try:
            num = int(totally_a_number)
            return num
        except ValueError:
            return 'not a number'

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
        i = 10
        while i < 100:
            result2 += i
            print(f"result is currently: {result2}, while on number: {i}")
            i += 2

        return True if result1 == result2 else False

    def final_2(self):
        import random
        random.seed(10)
        arr = sorted(random.sample(range(1, 100), 30))
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
            if left > right:
                return -1
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                return recursive_binary_search(arr, mid + 1, right, target)
            else:
                return recursive_binary_search(arr, left, mid - 1, target)
        
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
        
        dict_keys_list = list(countries_dict.keys())
        dict_values_list = list(countries_dict.values())
        


        return True if (True if keys_list == dict_keys_list else False) and (True if values_list == dict_values_list else False) else False
