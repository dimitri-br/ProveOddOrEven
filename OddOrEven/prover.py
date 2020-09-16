from .utilities import split
# Splits the function into an array so we can read each function accordingly
class Parser:
    def __init__(self):
        self.function = ""
        self.parsed_function = []

    def set_function(self, function="f(x)=x/2"):
        self.function = function

    def parse(self):
        split_func = self.function.split("=")

        if len(split_func) <= 1:
            return False

        i = 0
        for value in split(split_func[1]):
            self.parsed_function.append(value)
            i += 1

# This class will prove that the function is even, by assigning x to 1 and seeing if f(x) == f(-x)
class ProveEven:
    def __init__(self, func):
        self.func = func

    def prove(self):
        # To prove a function is even, f(x) = f(-x)
        fin_1 = 0  # Final value 1
        fin_2 = 0  # Final value 2
        flag = 0  # Flags - Used to define last operation

        for value in self.func:
            if value == "x":
                fin_1 += 1
            elif flag != 0:
                if flag == 1:
                    fin_1 += int(value)
                if flag == 2:
                    fin_1 -= int(value)
                if flag == 3:
                    fin_1 /= int(value)
                if flag == 4:
                    fin_1 *= int(value)
                if flag == 5:
                    fin_1 **= int(value)

            flag = self.set_flags(value)  # Check the current value, and set flag
        for value in self.func:
            if value == "x":
                fin_2 -= 1
            elif flag != 0:
                if flag == 1:
                    fin_2 += int(value)
                if flag == 2:
                    fin_2 -= int(value)
                if flag == 3:
                    fin_2 /= int(value)
                if flag == 4:
                    fin_2 *= int(value)
                if flag == 5:
                    fin_2 **= int(value)

            flag = self.set_flags(value)  # Check the current value, and set flag
        return fin_1 == fin_2, fin_1, fin_2  # Returns a boolean and the values

    @staticmethod
    def set_flags(value):
        flag = 0
        if value == "+":
            flag = 1
        elif value == "-":
            flag = 2
        elif value == "/":
            flag = 3
        elif value == "*":
            flag = 4
        elif value == "^":
            flag = 5
        return flag

# This class will prove that the function is odd, by assigning x to 1 and seeing if -f(x) == f(-x)
class ProveOdd:
    def __init__(self, func):
        self.func = func

    def prove(self):
        # To prove a function is odd, -f(x) = f(-x)
        fin_1 = 0  # Final value 1
        fin_2 = 0  # Final value 2
        flag = 0  # Flags - Used to define last operation

        for value in self.func:
            if value == "x":
                fin_1 += 1
            elif flag != 0:
                if flag == 1:
                    fin_1 += int(value)
                if flag == 2:
                    fin_1 -= int(value)
                if flag == 3:
                    fin_1 /= int(value)
                if flag == 4:
                    fin_1 *= int(value)
                if flag == 5:
                    fin_1 **= int(value)

            flag = self.set_flags(value)  # Check the current value, and set flag

        for value in self.func:
            if value == "x":
                fin_2 -= 1
            elif flag != 0:
                if flag == 1:
                    fin_2 += int(value)
                if flag == 2:
                    fin_2 -= int(value)
                if flag == 3:
                    fin_2 /= int(value)
                if flag == 4:
                    fin_2 *= int(value)
                if flag == 5:
                    fin_2 **= int(value)

            flag = self.set_flags(value)  # Check the current value, and set flag

        return -fin_1 == fin_2, -fin_1, fin_2  # Returns a boolean and the values

    @staticmethod
    def set_flags(value):
        flag = 0
        if value == "+":
            flag = 1
        elif value == "-":
            flag = 2
        elif value == "/":
            flag = 3
        elif value == "*":
            flag = 4
        elif value == "^":
            flag = 5
        return flag