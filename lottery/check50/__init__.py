import re

from check50 import *

class Lottery(Checks):

    @check()
    def exists(self):
        """lottery.c exists."""
        self.require("lottery.c")

    @check("exists")
    def compiles(self):
        """lottery.c compiles."""
        self.spawn("clang -std=c11 -o lottery lottery.c").exit(1)
