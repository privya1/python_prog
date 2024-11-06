class Number:
    def __init__(self, number = 0):
        self.number = number

    def is_even(self):
        if self.number % 2 == 0:
            print('given number', self.number, 'is an even number')
        if self.number % 2 != 0:
            print('given number', self.number, 'is an odd number')

    def is_prime(self):
        a = 2
        while a <= self.number/2:
            if self.number % a == 0:
                print('given number is not a prime')
                break
            a = a +1
        else:
            print('given number is a prime')

    def is_palindrome(self):
        str_num = str(self.number)
        if str_num == str_num[::-1]:
            print("given number is palindrome")
        else:
            print("given number is not a palindrome")



    def print(self):
        print(self.number)


p = Number()

p.print()
p.is_even()
p.is_prime()
p.is_palindrome()
