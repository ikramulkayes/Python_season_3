1
class Test5:

    def __init__(self):

        self.sum, self.y = 0, 0

    def methodA(self):

        x = 0

        z = 0

        while (z < 5):

            self.y = self.y + self.sum

            x = self.y + 1

           # print(x, self.y, self.sum)

            self.sum = self.sum + self.methodB(x, self.y)
            print(f"x = {x} y = {self.y} sum = {self.sum}")
            z += 1

    def methodB(self, m, n):

        x = 0

        sum = 0

        self.y = self.y + m

        x = n - 4

        sum = sum + self.y

        print(x, self.y, sum)

        return self.sum

t5 = Test5()
t5.methodA()