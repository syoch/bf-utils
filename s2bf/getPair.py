class Pair():
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        self.offs = 0

    def __str__(self) -> str:
        return f"({self.a}*{self.b}+{self.offs})"

    def get(self):
        if self.a == 1:
            return self.b+self.offs
        if self.b == 1:
            return self.a+self.offs

        return self.a+self.b+7+self.offs


def getPair(val: int):
    pair = Pair(1, val)
    minscore = val**4
    minpair = Pair(1, 1)
    for i in range(1, val+1):
        if val % i == 0:
            pair.a = i
            pair.b = val/i
            if pair.get() < minscore:
                minscore = pair.get()
                minpair.a = pair.a
                minpair.b = pair.b
    return minpair
