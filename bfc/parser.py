from typing import Any, Tuple


class parser():
    def __init__(self):
        self.src = ""
        self.index = 0

    def peek(self):
        if len(self.src) <= self.index:
            return None
        else:
            return self.src[self.index]

    def next(self):
        self.index += 1
        if len(self.src) <= self.index:
            return None
        else:
            return self.src[self.index]

    def consume(self, ch: str) -> Tuple[bool, Any]:
        if self.peek() == ch:
            self.index += 1
            return True, ch
        else:
            return False, None
