import os
import shutil
import helper_functions.run_me_first as rmf

"""
You do not need to be here, you are free to look tho!
This simply verifies taht we have the files and the 'generated_files' folder that we need to run the problems.
"""

class Verify_Environment:
    def __init__(self):
        self.dir_name = "files"
        self.dir_name2 = "generated_files"
        
        self.run = rmf.Run_Me_First(dir_name=self.dir_name, dir_name2=self.dir_name2)
        # self.verify_environment(dir_name=self.dir_name, dir_name2=self.dir_name2)
        
    def fix_files(self):
        print("Fixing files and folders by deleting them and re-creating them.")
        if os.path.isdir(self.dir_name):
            shutil.rmtree(self.dir_name)
        
        if os.path.isdir(self.dir_name2):
            shutil.rmtree(self.dir_name2)
        
        # self.run.create_files(dir_name=self.dir_name, dir_name2=self.dir_name2)
    
    def verify_environment(self, dir_name, dir_name2):
        # Check if the 'files' directory exists
        if os.path.isdir(dir_name):
            # print(f"Directory '{dir_name}' exists.")
            pass
        else:
            print(f"Directory '{dir_name}' does not exist. Running 'run_me_first.py' to set up the environment.")
            self.run.create_files(dir_name=self.dir_name, dir_name2=self.dir_name2)
        
        # Check if the 'generated_files' directory exists
        if os.path.isdir(dir_name2):
            # print(f"Directory '{dir_name2}' exists.")
            pass
        else:
            print(f"Directory '{dir_name2}' does not exist. Running 'run_me_first.py' to set up the environment.")
            self.run.create_files(dir_name=self.dir_name, dir_name2=self.dir_name2)
