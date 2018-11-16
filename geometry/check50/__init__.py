from check50 import *


class Geometry(Checks):

    @check()
    def exists(self):
        """geometry.c exists"""
        self.require("geometry.c")

    @check("exists")
    def compiles(self):
        """geometry.c compiles"""
        self.spawn("clang -std=c11 -o geometry geometry.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test1(self):
        """Compiles and then runs invalid menu item 1, then area of rectangle 10 x 10"""
        self.spawn("./geometry").stdin("-1").stdin("0").stdin("1").stdin("1").stdin("10").stdin("10").stdout("The rectangle's area is 100.\n").exit(0)

    @check("compiles")
    def test2(self):
        """Compiles and then runs invalid rectangle lengths (negative and 0), then area of rectangle 4 x 5"""
        self.spawn("./geometry").stdin("1").stdin("1").stdin("-1").stdin("0").stdin("4").stdin("5").stdout("The rectangle's area is 20.\n").exit(0)

    @check("compiles")
    def test3(self):
        """Compiles and then runs invalid menu item 2, then area of square 4"""
        self.spawn("./geometry").stdin("1").stdin("-1").stdin("4").stdin("2").stdin("4").stdout("The square's area is 16.\n").exit(0)

    @check("compiles")
    def test4(self):
        """Compiles and then runs invalid square length negative or 0, then area of square 7"""
        self.spawn("./geometry").stdin("1").stdin("2").stdin("-7").stdin("0").stdin("7").stdout("The square's area is 49.\n").exit(0)

    @check("compiles")
    def test5(self):
        """Compiles and then runs invalid triangle length negative or 0, then invalid lengths, area of triangle 3, 4, 5"""
        self.spawn("./geometry").stdin("1").stdin("3")\
            .stdin("-7").stdin("0").stdin("7").stdout("Invalid inputs. All sides must be > 0.\n")\
            .stdin("3").stdin("4").stdin("50").stdout("Invalid inputs. The sum of two sides must be > the third side.")\
            .stdin("3").stdin("4").stdin("5").stdout("The triangle's area is 6.0.\n").exit(0)

    @check("compiles")
    def test6(self):
        """Compiles and then runs invalid rectangle lengths (negative and 0), then perimeter of rectangle 4 x 5"""
        self.spawn("./geometry").stdin("2").stdin("1").stdin("-1").stdin("0").stdin("4").stdin("5").stdout("The rectangle's perimeter is 18.\n").exit(0)

    @check("compiles")
    def test7(self):
        """Compiles and then runs invalid square length negative or 0, then perimeter of square 7"""
        self.spawn("./geometry").stdin("2").stdin("2").stdin("-7").stdin("0").stdin("7").stdout("The square's perimeter is 28.\n").exit(0)

    @check("compiles")
    def test8(self):
        """Compiles and then runs invalid triangle length negative or 0, then invalid lengths, then perimeter of triangle 3, 4, 5"""
        self.spawn("./geometry").stdin("2").stdin("3")\
            .stdin("-7").stdin("0").stdin("7").stdout("Invalid inputs. All sides must be > 0.\n")\
            .stdin("3").stdin("4").stdin("50").stdout("Invalid inputs. The sum of two sides must be > the third side.")\
            .stdin("3").stdin("4").stdin("5").stdout("The triangle's perimeter is 12.\n").exit(0)


def number(num):
    return "(^|[^\d]){}[^\d]".format(num)
