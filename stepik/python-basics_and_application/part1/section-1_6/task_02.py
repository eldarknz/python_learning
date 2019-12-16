# https://stepik.org/lesson/24462/step/8?unit=6768

class ExtendedStack(list):
    def popLastElems(self, num):
        for i in range(num):
            self.pop()

    def sum(self):
        tmp = self[-1] + self[-2]
        self.popLastElems(2)
        self.append(tmp)

    def sub(self):
        tmp = self[-1] - self[-2]
        self.popLastElems(2)
        self.append(tmp)

    def mul(self):
        tmp = self[-1] * self[-2]
        self.popLastElems(2)
        self.append(tmp)

    def div(self):
        tmp = self[-1] // self[-2]
        self.popLastElems(2)
        self.append(tmp)
