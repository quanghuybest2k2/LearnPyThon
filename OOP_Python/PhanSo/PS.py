import math


class PS:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def pstg(self):
        temp = math.gcd(self.x, self.y)
        self.x = self.x/temp
        self.y = self.y/temp

    def __str__(self):
        return "{}/{}".format(int(self.x), int(self.y))


if __name__ == "__main__":
    m = int(input())
    n = int(input())
    ps = PS(m, n)
    ps.pstg()
    print(ps)
