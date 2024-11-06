class Number:
    def __init__(self, number):
        self.number = number

    def is_even(self):
        if self.number%2 == 0:
            print("even number")
        else:
            print("Odd number")



