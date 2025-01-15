from z3 import *

class RegularExpressions(object):
    def __init__(self):
        """Constructor of this class"""

        # Solver
        self.s = Solver()
        self.s.set("timeout", 5000)

        self.diff = String('diff')

        # Here is an example regex encoding to help you get started (just for reference)
        # \d{3}-\d{2}-\d{4}
        digit = Range('0', '9')
        self.ssn_regex = Concat(Loop(digit, 3, 3), Re('-'), Loop(digit, 2, 2), Re('-'), Loop(digit, 4, 4))
        print(self.debug(self.ssn_regex))

        # PART 1

        # \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}
        self.ip_regex1 = ...

        # ([0-9]?[0-9]?[0-9]\.){3}[0-9]?[0-9]?[0-9]
        self.ip_regex2 = ...

        # ((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])
        self.ip_regex3 = ...

        # ((25[0-5]|2[0-4][0-9]|[0-1][0-9]{2}|[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|[0-1][0-9]{2}|[0-9]?[0-9])
        self.ip_regex4 = ...
    
    def debug(self, regex):
        """Returns a string (self.diff) that matches the supplied regex"""
        self.s.push()

        self.s.add(InRe(self.diff, regex))

        result = self.s.check()
        if result == sat:
            model = self.s.model()
            self.s.pop()
            return model[self.diff]
        else: 
            return None 

    def compare(self, regex1, regex2):
        """Returns a string (self.diff) that matches regex1 but not regex2"""
        self.s.push()

        self.s.add(InRe(self.diff, regex1))
        self.s.add(Not(InRe(self.diff, regex2)))

        result = self.s.check()
        if result == sat:
            model = self.s.model()
            self.s.pop()
            return model[self.diff]
        else: 
            return result

if __name__ == "__main__":
    r = RegularExpressions()

    # You can use debug and compare to build your understanding of the regexes you encoded
    print(r.debug(r.ip_regex1))
    print(r.compare(r.ip_regex1, r.ip_regex1))

    # PART 3
    # Compare 1 and 2
    print("1 ", "<your answer here>", " 2")
    # Compare 1 and 3
    print("1 ", "<your answer here>", " 3")
    # Compare 1 and 4
    print("1 ", "<your answer here>", " 4")
    # Compare 2 and 3
    print("2 ", "<your answer here>", " 3")
    # Compare 2 and 4
    print("2 ", "<your answer here>", " 4")
    # Compare 3 and 4
    print("3 ", "<your answer here>", " 4")
    