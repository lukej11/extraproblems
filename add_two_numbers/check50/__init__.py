from check50 import *


class AddTwoNumbers(Checks):

    @check()
    def exists(self):
        """add_two_numbers.c exists"""
        self.require("add_two_numbers.c")

    @check("exists")
    def compiles(self):
        """add_two_numbers.c compiles"""
        self.spawn("clang -std=c11 -o add_two_numbers add_two_numbers.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test1(self):
        """"""
        self.spawn("./add_two_numbers").stdin("22").stdin("24").stdout("Total = 46\n").exit(0)

def number(num):
    return "(^|[^\d]){}[^\d]".format(num)
