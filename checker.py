from checker_input import CheckerInput

MIN_LENGTH_SCORE = 0
MAX_LENGTH_SCORE = 60


class Checker:
    def check(self, left: str, right: str):
        left_input = CheckerInput(left)
        right_input = CheckerInput(right)
        if left_input.length == right_input.length:
            return MAX_LENGTH_SCORE
        else:
            long_str, short_str = self.make_long_short_input(left_input, right_input)
            if self.assert_min_length_score(long_str, short_str):
                return MIN_LENGTH_SCORE
            return self.calculate_partial_score(long_str, short_str)

    def calculate_partial_score(self, long_str, short_str):
        return ((short_str.length - (long_str.length - short_str.length)) / short_str.length
                * MAX_LENGTH_SCORE)

    def assert_min_length_score(self, long_str, short_str):
        return long_str.length >= short_str.length * 2

    def make_long_short_input(self, left_input, right_input):
        long_str = left_input if left_input.length >= right_input.length else right_input
        short_str = left_input if long_str != left_input else right_input
        return long_str, short_str
