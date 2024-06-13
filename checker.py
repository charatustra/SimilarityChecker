MAX_LENGTH_SCORE = 60


class Checker:
    def check(self, left: str, right: str):
        if len(left) == len(right):
            return MAX_LENGTH_SCORE
