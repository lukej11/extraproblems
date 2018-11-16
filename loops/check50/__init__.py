from check50 import *


class Loops(Checks):

    @check()
    def exists(self):
        """loops.c exists"""
        self.require("loops.c")

    @check("exists")
    def compiles(self):
        """loops.c compiles"""
        self.spawn("clang -std=c11 -o loops loops.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test1(self):
        """Correct for inputs 3 and 3"""
        self.spawn("./loops").stdin("3").stdout("3 x 0 = 0\n3 x 1 = 3\n3 x 2 = 6\n3 x 3 = 9\n3 x 4 = 12\n3 x 5 = 15\n3 x 6 = 18\n3 x 7 = 21\n3 x 8 = 24\n3 x 9 = 27\n3 x 10 = 30\n3 x 11 = 33\n3 x 12 = 36\n").stdin("3").stdout("0\n1\n2\n3\n").exit(0)

    @check("compiles")
    def test2(self):
        """Correct for inputs 6 and 2"""
        self.spawn("./loops").stdin("2").stdout("2 x 0 = 0\n2 x 1 = 2\n2 x 2 = 4\n2 x 3 = 6\n2 x 4 = 8\n2 x 5 = 10\n2 x 6 = 12\n2 x 7 = 14\n2 x 8 = 16\n2 x 9 = 18\n2 x 10 = 20\n2 x 11 = 22\n2 x 12 = 24\n").stdin("6").stdout("0\n1\n2\n3\n4\n5\n6").exit(0)

    #@check("compiles")
    #def test2(self):
    #    """"""
    #    self.spawn("./loops").stdin("0").stdout("That response is invalid\n").stdin("2").stdout("That response is valid\n").stdin("30").stdout("That response is valid\n").exit(0)

    @check("compiles")
    def test_reject_negative(self):
        """rejects a negative input like -.1"""
        self.spawn("./loops").stdin("-1").reject()

    @check("compiles")
    def test_reject_foo(self):
        """rejects a non-numeric input of "foo" """
        self.spawn("./loops").stdin("foo").reject()

    @check("compiles")
    def test_reject_empty(self):
        """rejects a non-numeric input of "" """
        self.spawn("./loops").stdin("").reject()

def number(num):
    return "(^|[^\d]){}[^\d]".format(num)
