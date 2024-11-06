class Point:
    def reset(self):
        self.x = 0
        self.y = 0
        print(self.x, self.y)

    def square(this):
        this.x = this.x**2 
        this.y = this.y**2
        print(this.x, this.y)
        
        
    def print(current):
        print(current.x, current.y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def add(self, x, y):
        self.x = self.x + x
        self.y = self.y + y

    
# p1 = Point()
# p2 = Point()

# p1.x = 5
# p2.x = 6
# p1.y = 7
# p2.y = 8

# p1.print()
# p2.print()
# p1.square()
# p2.square()
# p1.reset()
# p2.reset()

p = Point()

p.x = 2
p.y = 3
p.print()
p.move(4,5)
p.print()
p.add(7,8)
p.print()