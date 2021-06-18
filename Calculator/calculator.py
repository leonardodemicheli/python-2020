class Calculator:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    def add(self):
        result = self.number_1 + self.number_2
        return(result)

    def sub(self):
        result = self.number_1 - self.number_2
        return(result)

    def mul(self):
        result = self.number_1 * self.number_2
        return(result)

    def div(self):
        result = self.number_1 / self.number_2
        return(result)

    def mod(self):
        result = self.number_1 % self.number_2
        return(result)