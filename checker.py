MIN_LENGTH_SCORE = 0
MAX_LENGTH_SCORE = 60


class Checker:
    def check(self, left: str, right: str):
        if len(left) == len(right):
            return MAX_LENGTH_SCORE
        else:
            long_str = left if len(left) >= len(right) else right
            short_str = left if long_str != left else right
            if len(long_str) >= len(short_str) * 2:
                return MIN_LENGTH_SCORE
            gap = len(long_str) - len(short_str)
            return (len(short_str) - gap) / len(short_str) * MAX_LENGTH_SCORE
