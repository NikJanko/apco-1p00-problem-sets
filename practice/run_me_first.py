import os

"""
you are welcome to look at this code, but you really do not need to be here.
"""

class Run_Me_First:
    def __init__(self, dir_name="files", dir_name2="generated_files"):
        self.dir_name = dir_name
        self.dir_name2 = dir_name2
        self.create_files(dir_name=self.dir_name, dir_name2=self.dir_name2)
    
    
    def create_files(self, dir_name, dir_name2):
        # 
        try:
            os.mkdir(dir_name)
            # print(f"Directory '{dir_name}' created successfully.")
        except FileExistsError:
            # print(f"Directory '{dir_name}' already exists.")
            pass
        except PermissionError:
            print(f"Permission denied: Unable to create directory '{dir_name}'.")
        except Exception as e:
            print(f"An error occurred while creating directory '{dir_name}': {e}")
            
        # 

        # 
        path = os.path.join(dir_name, "data_quad.txt")
        try:
            with open(path, 'w') as f:
                f.write("100 42 9 149\n")
                f.write("41 28 73 56\n")
                f.write("88 15 63 77")
            # print(f"File '{path}' created and data written successfully.")
        except PermissionError:
            print(f"Permission denied: Unable to write to file '{path}'.")
        except Exception as e:
            print(f"An error occurred while writing to file '{path}': {e}")

        #   
        path = os.path.join(dir_name, "data_tri.txt")
        try:
            with open(path, 'w') as f:
                f.write("100 42 149\n")
                f.write("28 73 56\n")
                f.write("88 15 63")
            # print(f"File '{path}' created and data written successfully.")
        except PermissionError:
            print(f"Permission denied: Unable to write to file '{path}'.")
        except Exception as e:
            print(f"An error occurred while writing to file '{path}': {e}")

        # 
        path = os.path.join(dir_name, "data_tri.txt")
        try:
            with open(path, 'w') as f:
                f.write("100 42 149\n")
                f.write("28 73 56\n")
                f.write("88 15 63")
            # print(f"File '{path}' created and data written successfully.")
        except PermissionError:
            print(f"Permission denied: Unable to write to file '{path}'.")
        except Exception as e:
            print(f"An error occurred while writing to file '{path}': {e}")

        #   
        path = os.path.join(dir_name, "data_duo.txt")
        try:
            with open(path, 'w') as f:
                f.write("28 40\n")
                f.write("1 23\n")
                f.write("97 23")
            # print(f"File '{path}' created and data written successfully.")
        except PermissionError:
            print(f"Permission denied: Unable to write to file '{path}'.")
        except Exception as e:
            print(f"An error occurred while writing to file '{path}': {e}")
            
        # 
        path = os.path.join(dir_name, "data_solo.txt")
        try:
            with open(path, 'w') as f:
                f.write("20\n")
                f.write("13\n")
                f.write("8")
            # print(f"File '{path}' created and data written successfully.")
        except PermissionError:
            print(f"Permission denied: Unable to write to file '{path}'.")
        except Exception as e:
            print(f"An error occurred while writing to file '{path}': {e}")
            