from helper_functions import ProblemStatement
ps = ProblemStatement()


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
    

    def one(self, test_arg):
        ps.display(1)
        """
        Add your code here.
        """
        
        return test_arg

    def two(self):
        ps.display(2)
        """
        Add your code here.
        """

    def three(self):
        ps.display(3)
        """
        Add your code here.
    """

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

    def six(self):
        ps.display(6)
        """
        Add your code here.
        """

    def seven(self):
        ps.display(7)
        """
        Add your code here.
        """

    def eight(self):
        ps.display(8)
        """
        Add your code here.
        """

    def nine(self):
        ps.display(9)
        """
        Add your code here.
        """

    def ten(self):
        ps.display(10)
        """
        Add your code here.
        """

    def eleven(self):
        ps.display(11)
        """
        Add your code here.
        """

    def twelve(self):
        ps.display(12)
        """
        Add your code here.
        """

    def thirteen(self):
        ps.display(13)
        """
        Add your code here.
        """


    def fourteen(self):
        ps.display(14)
        """
        Add your code here.
        """

    def fifteen(self):
        ps.display(15)
        """
        Add your code here.
        """

    def sixteen(self):
        ps.display(16)
        """
        Add your code here.
        """

    def seventeen(self):
        ps.display(17)
        """
        Add your code here.
        """

    def eighteen(self):
        ps.display(18)
        """
        Add your code here.
        """

    def nineteen(self):
        ps.display(19)
        """
        Add your code here.
        """
        
    def twenty(self):
        ps.display(20)
        """
        Add your code here.
        """

    def twenty_one(self):
        ps.display(21)
        """
        Add your code here.
        """

    def twenty_two(self):
        ps.display(22)
        """
        Add your code here.
        """

    def twenty_three(self):
        ps.display(23)
        """
        Add your code here.
        """

    def twenty_four(self):
        ps.display(24)
        """
        Add your code here.
        """

    def twenty_five(self):
        ps.display(25)
        """
        Add your code here.
        """

    def twenty_six(self):
        ps.display(26)
        """
        Add your code here.
        """

    def twenty_seven(self):
        ps.display(27)
        """
        Add your code here.
        """

    ping_pong = 0

    def twenty_eight(self):
        ps.display(28)
        """
        Add your code here.
        """

    def twenty_nine(self):
        ps.display(29)
        """
        Add your code here.
        """

    def fix_me_1(self, test_arg):
        ps.display("rest")
        """
        Add your code here.
        """
        return 

    def fix_me_2(self):
        ps.display("rest")
        """
        Add your code here.
        """

    def fix_me_3(self):
        ps.display("rest")
        """
        Add your code here.
        """

    def fix_me_4(self):
        ps.display("rest")
        """
        Add your code here.
        """

    def fix_me_5(self):
        ps.display("rest")
        """
        Add your code here.
        """

    def fix_me_6(self):
        ps.display("rest")
        """
        Add your code here.
        """

    def fix_me_7(self):
        ps.display("rest")
        """
        Add your code here.
        """

    def fix_me_8(self):
        ps.display("rest")
        """
        Add your code here.
        """

    def fix_me_9(self):
        ps.display("rest")
        """
        Add your code here.
        """

    def fix_me_10(self):
        ps.display("rest")
        """
        Add your code here.
        """

    def final_1(self):
        ps.display("final")
        """
        Add your code here.
        """

    def final_2(self):
        ps.display("final")
        """
        Add your code here.
        """

    def final_3(self):
        ps.display("final")
        """
        Add your code here.
        """
