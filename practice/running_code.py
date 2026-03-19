import sys
sys.path.insert(0, __file__.rsplit('\\', 1)[0].rsplit('\\', 1)[0])
import code_problems as Problem
from helper_functions import verify_environment as VE
from helper_functions import hint as hint
import io

def see_only_output(func, *args, **kwargs):
    """Unused testing function"""
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    result = func(*args, **kwargs)
    sys.stdout = old_stdout
    
    return result
    """IGNORE THIS CODE SECTION, IT IS USED TO SET UP THE PROBLEMS FOR YOU."""


if __name__ == "__main__":
    # set up problems and hints.
    verify = VE.Verify_Environment()
    verify.verify_environment(dir_name=verify.dir_name, dir_name2=verify.dir_name2)
    problems = Problem.Code_Problems()
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
    # Uncomment below to see all problem statements - creates a file 'all_problems.txt' in the parent directory with all problem statements.
    # problems.print_all_problems(print_to_file=False)
    
    # CHOOSE & RUN A PROBLEM :
    # problems.run_problem(1, 'arguments here if applicable')
    
    # GET A HINT :
    # hint.ask_hint()
    
    # RESET FILES/FOLDERS (WARNING: clears both folders) :
    # verify.fix_files()
    
    



