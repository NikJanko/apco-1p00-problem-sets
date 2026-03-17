import sys
sys.path.insert(0, __file__.rsplit('\\', 1)[0].rsplit('\\', 1)[0])

import code_problems as Problem
from helper_functions import verify_environment as VE
from helper_functions import hint as hint
import io

def see_only_output(func):
    """IGNORE THIS CODE SECTION, IT IS USED TO SET UP THE PROBLEMS FOR YOU."""
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    result = func()
    sys.stdout = old_stdout
    """IGNORE THIS CODE SECTION, IT IS USED TO SET UP THE PROBLEMS FOR YOU."""
    return result


if __name__ == "__main__":
    verify = VE.Verify_Environment()
    problems = Problem.Code_Problems()
    hint = hint.Hint()
    
    """
    Here is the main function that will run your code. You can change the problem number to run different problems.

    To see if you got the problem right, run the Test_Cases file. If you want to see hints, run the hint.py file. - all code should be done in the code_problems.py file.
    You should only be change the problem number you want to run here.

    all your solutions are imported via the code_problems import statement. Choose which problem you want to do by first selecting it here, running it (to see the problem statement), and then writing your code in the code_problems.py file.

    -------------------------------------------------------------------------------
    
    
    Each problem (that is not a 'generate file' problem) SHOULD print AND return the answer. if the output is 'generated file' and something else, then you should just print the answer. If the output is only 'generated file', then you do not need to print or return anything. The files you generated should be in the 'generated_files' folder so that my code may check if you actually generated them, and test the contents of the files you generated. If you are confused about what to print or return, check the problem statement for that problem, and if you are still confused, you may email me: nj21mf@brocku.ca
    
    NOTE: do not use AI. you may use your notes, the hints provided and the internet (Documentation, StackOverflow, etc.) to help you with the problems, but do not use AI to generate code for you. Although this is not graded this problem set has been made for you to practice your coding, reading and creative skills. In the case that you are really stuck you may ask AI for help understanding OR clarification. But best not to use it for answers. My solutions (minimized and multiline) are in the solutions folder for you to check your work against, or to guide you. Try to exhaust the hints before defaulting to looking at solutions.
    """
    
    # ------------------------------------------------------------------- #
    # ------------------------------------------------------------------- #
    """If you require a hint, uncomment the line below and run the file."""
    # hint.hint()
    
    # ------------------------------------------------------------------- #
    # ------------------------------------------------------------------- #
    
    
    
    # change the number to run different problems (1-29, fix_me_1-10, final_1-3)
    problems.run_problem(1) 
    
    """
    For some problems, you will need to return something, to avoid printing the problem statement each time, you can use the 'see_only_output()' function I have made. An example of its use is below. -> MAKE SURE TO COMMENT OUT THE LINE ABOVE 'problems.run_problem(n)' before using this function.
    """
    # print(see_only_output(problems.one)) 
    
    



