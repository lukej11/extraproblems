from check50 import *


class MadLibs(Checks):

    @check()
    def exists(self):
        """mad_libs.c exists"""
        self.require("mad_libs.c")

    @check("exists")
    def compiles(self):
        """mad_libs.c compiles"""
        self.spawn("clang -std=c11 -o mad_libs mad_libs.c -lcs50 -lm").exit(0)
