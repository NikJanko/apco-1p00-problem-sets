"""
Do not look at this file
"""

class Hint_Manager:
    def __init__(self):
        self.hint_dict = {
            1: ["You require a path to read the file, the path is: ../files/data_duo.txt, use the os.path.join() function.", "Reading the lines returns a list of strings. You'll need to convert each string to an integer.", "use 'with open(PATH, 'r') as f:' to read the file, and then 'lines = f.readlines()' to get the lines of the file."],
            2: ["The path to read the file is: ../files/data_tri.txt", "The product (or multiplication) is done via the * (asterisk/star) operator.", "use 'with open(PATH, 'r') as f:' to read the file, and then 'lines = f.readlines()' to get the lines of the file."],
            3: ["The path to read the file is: ../files/data_solo.txt", "The factorial of a number n is the product of all positive integers less than or equal to n. Since we are doing repetition, use a loop.", "use 'with open(PATH, 'r') as f:' to read the file, and then 'lines = f.readlines()' to get the lines of the file."],
            4: ["The path to read the file is: ../files/grades.csv", "you will need to import the csv module (WITHIN THE FUNCTION SCOPE).", "You should read and save all the contents of the file in a variable before writing the contents to a new file.", "use 'with open(PATH, 'r') as f:' and csv.reader() to read the file, use 'with open(PATH, 'w', newline='') as f:' and csv.writer() to write the file, and remember to calculate the average grade for each student. before writing."],
            5: ["The path to write the file is: ../generated_files/output.csv", "You need to create a CSV writer object using csv.writer().", "use 'with open(PATH, 'w', newline='') as f:' to write the file, and then use writer.writerow() to write each row."],
            6: ["The path to read the file is: ../files/data_duo.txt", "The difference of two integers a and b can be calculated as a - b.", "use 'with open(PATH, 'r') as f:' to read the file, and then 'lines = f.readlines()' to get the lines of the file."],
            7: ["Import the random module, and use random.seed(10), make sure the import is within the function.", "Use random.sample() [LOOK AT THE DOCUMENTATION] to generate unique random integers within a specified range.", "use 'with open(PATH, 'w') as f:' to write the file, and remember to convert the integers to strings before writing them to the file. The PATH is ../generated_files/recur.txt"],
            8: ["The path to read the file is: ../generated_files/recur.txt", "use 'with open(PATH, 'r') as f:' to read the file, and then 'lines = f.readlines()'", "Psudeo code: \nread the file,\n if the length of the array is less than or equal to 1: return the array,\n otherwise: take the center of the array as a pivot,\n take a slice of the left side of the array as everything smaller than the pivot,\n take a slice of the right side of the array as everything bigger than the pivot,\n take a slice of the array which only holds every instance of the pivot,\n return the result of recursively calling the function on the left slice, then the pivot_array, then recursively calling the function on the right slice.", "(recursive steps solution):\n\nif len(array) <= 1:\n    return array\npivot = array[len(array) // 2]\nleft = []\nright = []\npivot_array = []\nfor num in array:\n    if num < pivot:\n        left.append(num)\n    elif num > pivot:\n        right.append(num)\n    else:\n        pivot_array.append(num)\nreturn quicksort(left) + pivot_array + quicksort(right)"],
            9: ["The path to read the file is: ../generated_files/recur.txt", "use 'with open(PATH, 'r') as f:' to read the file, and then 'lines = f.readlines()' to get the lines of the file.", "Pseudo code: \nread the file,\n set low to 0 and high to the length of the array - 1,\n if low is greater than high, return -1 (base case for not found),\n find the middle index as (low + high) // 2,\n if the target is less than the middle element, recursively search the left half of the array (high becomes mid - 1),\n if the target is greater than the middle element, recursively search the right half of the array (low becomes mid + 1),\n if the target is equal to the middle element, return the middle index.", "(recursive steps solution):\n\nlow = 0\nhigh = len(array) - 1\nif low > high:\n    return -1\nmid = (low + high) // 2\nif target < array[mid]:\n    return binary_search(array, target, low, mid - 1)\nelif target > array[mid]:\n    return binary_search(array, target, mid + 1, high)\nelse:\n    return mid"],
            10: ["you'll need to 'sanitize' the input first; like setting the tolerance to the correct magnitude before calling the recursion", "You must first set phi to 1.0, then recursively calculate phi using the formula. Your base case is if phi is close enough to the golden ratio.", "to put tolerance into the correct magnitude, use tol = 10 ** (-tolerance), thus your base case will be if abs(phi - golden_ratio) < tol."],
            11: ["The Fibonacci sequence is defined as F(n) = F(n-1) + F(n-2) with base cases F(0) = 0 and F(1) = 1.", "You can implement the Fibonacci function recursively by calling itself with the two preceding numbers until it reaches the base cases.", "Pseudo code: \nif n <= 0 or 1:\n    return 0 or 1\n...\nelse:\n    return fibonacci(n-1) + fibonacci(n-2)"],
            12: ["The Fibonacci sequence can be efficiently calculated using an iterative approach by storing the 2 previously computed values.", "You can use a loop to iteratively calculate Fibonacci numbers up to n, storing the last two computed values at each step.", "Pseudo code: \na = 0\nb = 1\nfor i in range(2, n + 1):\n    c = a + b\n    a, b = b, c\nreturn b"],
            13: ["the file to read is: ../files/data_quad.txt", "You cannot use the sum function, instead use a loop adding to a cumulative sum variable", "use 'with open(PATH, 'r') as f:' to read the file, and then 'lines = f.readlines()' to get the lines of the file.", "You must covert the integers from strings. and divide by how many integers there are (len(array)) to get the average."],
            14: ["The file to write is: ../generated_files/recur2.txt", "Import the random module, and use random.seed(10), make sure the import is within the function.", "Use random.sample() [LOOK AT THE DOCUMENTATION] to generate unique random integers within a specified range.", "use 'with open(PATH, 'w') as f:' to write the file, and remember to convert the integers to strings before writing them to the file.", "you may use a nested loop, get the line, then add '\\n' to the end before writing to the file, and remember to reset the line variable after each row."],
            15: ["The file to read is: ../generated_files/recur2.txt and write to ../generated_files/recur3.txt", "use 'with open(PATH, 'r') as f:' to read the file, and then 'lines = f.readlines()' to get the lines of the file.", "dont run the sort command, instead implement:\nloop through the array length.\n    set an anchor to the current element. then set a starter variable as j=i (where i is the iterator number).\n   while j is greater than 0 and the element to the left of the anchor is greater than the anchor:\n        swap the element to the left of the anchor with the anchor\n        move j one step to the left (j -= 1)\n    repeat until the anchor is in the correct spot.\nwrite the sorted array to the new file, remember to convert the integers to strings before writing them to the file."],
            16: ["The file to read is: ../generated_files/recur2.txt", "use 'with open(PATH, 'r') as f:' to read the file, and then 'lines = f.readlines()' to get the lines of the file.", "Increment the appropriate key, or add that key to the dictionary", "the mode is just how frequent the most common number is. "],
            17: ["area formula: 2*(length*width) + 2*(width*height).\nthen multiply by the number of stories.\nfor the roof, the base is min(length+2, width+2),\nthe prism_length is max(length+2, width+2)\nUse pythagorean theorem (sqrt(base/2)**2 + (height+2)**2)\nThe final area for the roof is: (base*(width+2)) + (2*(prism_length * pythagorean theorem result))"],
            18: ["the file to read is: ../files/cipher_passage.txt", "use 'with open(PATH, 'r') as f:' to read the file, and then 'lines = f.readlines()' to get the lines of the file.", "loop through the characters, replacing each read character with the character in the mapping dictionary via lookup"],
            19: ["the input is EITHER a file or a string, you must check which on it is first.", "to check if the input is a file, use os.path.isfile(input)", "you'll need to reverse the keys and values (NOT MANUALLY) in the dictionary. There are 3 ways to do this, 2 of them are easier. all require a loop."],
            20: ["you'll have to loop through the possible list of words each time you encounter a correct unscramble of one of the words, increment the counter", "remember, since the unscrambled word can be anywhere, we must check each word after shifting", "when shifting each character over, the last character will become the first character."],
            21: ["multiplication is just repeated addition."],
            22: ["you will need to treat this as a photo. you will be changing 'the size'/'the bounds' of the photo.", "psudeo code: FUNCTION get_spiral_order(matrix):\n    IF matrix is empty OR first row of matrix is empty:\n        RETURN empty list\n\n    CREATE empty list called result\n\n    SET top = 0\n    SET bottom = (number of rows in matrix) - 1\n    SET left = 0\n    SET right = (number of columns in matrix) - 1\n\n    WHILE top <= bottom AND left <= right:\n\n        // 1. Traverse top row from left to right\n        FOR i FROM left TO right:\n            APPEND matrix[top][i] TO result\n        INCREMENT top BY 1\n\n        // 2. Traverse right column from top to bottom\n        FOR i FROM top TO bottom:\n            APPEND matrix[i][right] TO result\n        DECREMENT right BY 1\n\n        // 3. Traverse bottom row from right to left\n        IF top <= bottom:\n            FOR i FROM right DOWN TO left:\n                APPEND matrix[bottom][i] TO result\n            DECREMENT bottom BY 1\n\n        // 4. Traverse left column from bottom to top\n        IF left <= right:\n            FOR i FROM bottom DOWN TO top:\n                APPEND matrix[i][left] TO result\n            INCREMENT left BY 1\n\n    RETURN result"],
            23: ["def get_spiral_order(matrix):\n    result = []\n    if not matrix or not matrix[0]:\n        return result\n\n    def traverse(top, bottom, left, right):\n        if top > bottom or left > right:\n            return\n\n        for i in range(left, right + 1):\n            result.append(matrix[top][i])\n\n        for i in range(top + 1, bottom + 1):\n            result.append(matrix[i][right])\n\n        if top < bottom:\n            for i in range(right - 1, left - 1, -1):\n                result.append(matrix[bottom][i])\n\n        if left < right:\n            for i in range(bottom - 1, top, -1):\n                result.append(matrix[i][left])\n\n        traverse(top + 1, bottom - 1, left + 1, right - 1)\n\n    traverse(0, len(matrix) - 1, 0, len(matrix[0]) - 1)\n    return result"],
            24: ["use a loop and dictionary to count the frequency of each word, then return the dictionary, both count and remove the vowels at the same time."],
            25: ["to have the code 'save' multiple people to the class, each class is treated like an object and needs a variable to 'stay alive'. kinda how we have x=1, and y=2 is the same as x=integer(1), y=integer(2). they are a both integer classes and require their separate variables.", "create a class within the function. you can use self.'variable name' to create class scoped variables within the class.", "you'll need to do\ndef __init__(self, name, type, year, color):\n    self.name = name\n    self.type = type\n    self.year = year\n    self.color = color. within the class, then\ndef give_string():\n    return 'string here'" ],
            26: ["check out the hits for 25 - there is one more hint level for this one", "using try-except blocks, in the except portion, return the error message."],
            27: ["Use with open(PATH, 'r') as f: to read the file, and then lines = f.readlines() to get the lines of the file.", "Use multiple try-except blocks to catch the different types of errors."],
            28: ["call in a global variable with the 'global' keyword. modifying this variable will modify it for all functions in the file."],
            29: ["run your 28th problem function in here, each line calls the function, then you should store the result in a list. go to the next line and repeat, reset the global variable before running the 28th function again."],
            
            "rest": ['no hints here'],
            "final": ['no hints here']
            
            
            
            
        }
        pass



    def get_hint(self, problem_number, hint_level):
        if problem_number in [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]:
            problem_number = "final"
            hint_level = 1
        
        if problem_number in self.hint_dict:
            if problem_number in ["rest", "final"]:
                problem_number = "final"
                print("\033[36m"+f"{problem_number} problems only has 1 hint level, and it is:\n{self.hint_dict[problem_number][0]}"+ "\033[0m")
                return
            
            if 1 <= hint_level <= len(self.hint_dict[problem_number]):
                print(self.hint_dict[problem_number][hint_level - 1])
            else:
                print(f"\033[31mInvalid hint level. Please choose a hint level between 1 and {len(self.hint_dict[problem_number])} for problem {problem_number}.\033[0m")
        else:
            print("\033[31mInvalid problem number. Please choose a valid hint + hint level.\033[0m")



    def ask_hint(self):
        print("\033[36m"+
            "Problems 1-29 have 3 hints, 30-40 have 2 hints, and 41-43 have 1 hint.\n Question [4, 8, 16, 17, 19, 20, 22, 28] all have 4 hint levels."+
            "\033[0m")
        
        user_input = input("Enter the problem you would like a hint for\n(1-29) for the main ones,\n(30-40) for the fix_me ones, and\n(41-43) for the final problems!\nYou will be asked which hint level you want (bigger number = better hint).\n\nExample, 'i need a hint for problem 4, and i want a level 2 hint' -> '4 2' (SPACE SEPARATED): ")

        try:
            hint, level = user_input.strip().split()
        except ValueError:
            print("\033[31mInvalid input format. Please enter the problem number and hint level separated by a space.\033[0m")
            return
        except Exception as e:
            print(f"\033[31mAn error occurred: {e}\033[0m")
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
        
    
    
