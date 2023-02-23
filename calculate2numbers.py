class calculateClass:
    def __init__(self, x, y, type):
        self.x = float(input("Enter the first number: "))
        self.y = float(input("Enter the second number: "))
        self.type = input("Enter the method to formula the earlier '2' entries or type 'help': ").lower()

    def calculate(self):
        if (self.type == "help"):
            output_math = f"Kindly enter: '/ as div', '+ as add', '- as sub', '* as multi', '^ as power."
        elif (self.type == "div"):
            output_math = f"The answers would have been {self.x / self.y}."
        elif (self.type == "sub"):
            output_math = f"The answers would have been {self.x - self.y}."
        elif (self.type == "add"):
            output_math = f"The answers would have been {self.x + self.y}."
        elif (self.type == "multi"):
            output_math = f"The answers would have been {self.x * self.y}."
        elif (self.type == "power"):
            output_math = f"The answers would have been {self.x ** self.y}."
        else:
            output_math = f"Sorry I do not understand you, kindly type 'help'."
        return output_math


number1 = calculateClass(0.0, 0.0, str)
print(number1.calculate())