import sys
sys.path.insert(0, __file__.rsplit('\\', 1)[0].rsplit('\\', 1)[0])
import code_problems as Problem
from helper_functions import verify_environment as VE
from helper_functions import hint as hint
import io

def see_only_output(func, *args, **kwargs):
    """IGNORE THIS CODE SECTION, IT IS USED TO SET UP THE PROBLEMS FOR YOU."""
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    result = func(*args, **kwargs)
    sys.stdout = old_stdout
    """IGNORE THIS CODE SECTION, IT IS USED TO SET UP THE PROBLEMS FOR YOU."""
    return result


if __name__ == "__main__":
    verify = VE.Verify_Environment()
    verify.verify_environment(dir_name=verify.dir_name, dir_name2=verify.dir_name2)
    problems = Problem.Code_Problems()
    hint = hint.Hint_Manager()
    
    """
    Here is the main function that will run your code. You can change the problem number to run different problems.

    You will only need to write the code in the code_problems.py file.
    For hints, uncomment the hint line, 
    to see only what is returned (without the problem statement), uncomment the see_only_output line and comment out the normal run_problem line.
    if you messed up the file structure/files and nothing is working anymore, uncomment the fix_files line to reset the files to their original state (this will also reset the generated_files folder, so if you have files you want to keep, move them elsewhere before running this code).
    
    To test your code, uncomment the full_sweep line.
    
    Choose which problem you want to do by first selecting it here, running it (to see the problem statement), and then writing your code in the code_problems.py file.

    -------------------------------------------------------------------------------
    
    
    Each problem (that is not a 'generate file' problem) SHOULD print AND return the answer. if the output is 'generated file' and something else, then you should just print the answer. If the output is only 'generated file', then you do not need to print or return anything. The files you generated should be in the 'generated_files' folder so that my code may check if you actually generated them, and test the contents of the files you generated. printing is only to help you, but you must return the output, and if you are still confused, you may email me: nj21mf@brocku.ca
    
    NOTE: do not use AI. you may use your notes, the hints provided and the internet (Documentation, StackOverflow, etc.) to help you with the problems, but do not use AI to generate code for you. Although this is not graded this problem set has been made for you to practice your coding, reading and creative skills. In the case that you are really stuck you may ask AI for help understanding OR clarification. But best not to use it for answers. My solutions (minimized and multiline) are in the solutions folder for you to check your work against, or to guide you. Try to exhaust the hints before defaulting to looking at solutions.
    """
    
    # ------------------------------------------------------------------- #
    # ------------------------------------------------------------------- #
    """If you require a hint, uncomment the line below and run the file."""
    # hint.ask_hint()
    
    # ------------------------------------------------------------------- #
    # ------------------------------------------------------------------- #
    
    # change the number to run different problems (1-29, fix_me_problems: 30-39, final_problems: 40-42)
    problems.run_problem(1)
    
    
    """
    to see only the returned value (what your code is being tested on), uncomment the line below and comment out the normal run_problem line above.
    """
    print(see_only_output(problems.question[1], 'arguments here')) 
    
    
    """
    To fix the files and folders (this will delete the 'files' and 'generated_files' folders and re-create them, so if you have files in there you want to keep, move them elsewhere before running this code):

    """
    # verify.fix_files()
    
    
    
    # ------------------------------------------------ #
    """
    in case you delete anything, these are the functions:
    
    # hint.ask_hint()
    # print(see_only_output(problems.question[41], 'arguments here')) 
    # verify.fix_files()
    """
    
    



