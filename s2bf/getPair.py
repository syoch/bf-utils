class PairInt():
    def __init__(self, num: int):
        self.num = num

    def getscore(self):
        return self.num


class Pair():
    def __init__(self, a: int, b: int):
        self.a: int = a
        self.b: int = b
        self.offs: int = 0

    def __str__(self) -> str:
        return f"({self.a}*{self.b}+{self.offs})"

    def get(self, ch="+") -> str:
        if self.a == 1:
            return 0, ch*(self.b+self.offs)
        if self.b == 1:
            return 0, ch*(self.a+self.offs)

        da, a = getPair(self.a).get("+")
        db, b = getPair(self.b).get(ch)
        o = (
            "-" if (
                -1 if ch == "-"
                else +1
            ) * self.offs < 0
            else "+"
        )*abs(self.offs)
        return max(da, db)+1, f"{a}[<{b}>-]<{o}>"

    def adjust(self) -> None:
        if type(self.a) == int:
            self.a = PairInt(self.a)
        if type(self.b) == int:
            self.b = PairInt(self.b)

    def getscore(self) -> int:
        if self.a == 1:
            return self.b+abs(self.offs)
        if self.b == 1:
            return self.a+abs(self.offs)

        return self.a.getscore()+self.b.getscore()+7+abs(self.offs)


def _getPair(val: int) -> Pair:
    pair = Pair(1, val)
    minscore = val**4
    minpair = Pair(1, 1)
    for i in range(1, int(val**.5)+1):
        if val % i == 0:
            pair.a = i
            pair.b = val//i
            if pair.getscore() < minscore:
                minscore = pair.getscore()
                minpair = pair

    return minpair


def getPair(val: int):
    pair = Pair(1, val)
    minscore = val**4
    minpair = Pair(1, 1)
    for i in range(-val, val, 1):
        pair = _getPair(val-i)
        pair.offs = i
        print(pair.getscore(), minscore)
        if pair.getscore() < minscore:
            minscore = pair.getscore()
            minpair = pair
    return minpair
