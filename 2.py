class Rect:
    def __init__(self,a,h):
        self.__a = a
        self.__h = h
    def S(self):
        return self.__a * self.__h * 0.5

rect = Rect(3,4)
print(rect.S())
