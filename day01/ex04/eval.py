#!/usr/bin/env python3
""" Evaluator class

"""
class Evaluator:
    """A class capable of processing text with coeffs, two different ways"""

    def zip_evaluate(self, coefs, words):
        """Evaluate with zip()"""
        if self.valid(coefs, words):
            zipped = zip(coefs, words)
            total = 0
            for elem in zipped:
                total += elem[0] * len(elem[1])
            return total
        return -1

    def enumerate_evaluate(self, coefs, words):
        """Evaluate with enumerate()"""
        if self.valid(coefs, words):
            total = 0
            for count, value in enumerate(words):
                total += coefs[count] * len(value)
            return total
        return -1

    def valid(self, coefs, words):
        """Evaluates validity of the arguments"""
        if not isinstance(coefs, list) or not isinstance(words, list):
            return False
        invalid_coefs = [x for x in coefs if not isinstance(x, (int, float))]
        invalid_words = [x for x in words if not isinstance(x, str)]
        if len(coefs) != len(words) or invalid_coefs or invalid_words:
            return False
        return True


def test_evaluator(coefs, words):
    """A function to test the Evaluator class"""
    evl = Evaluator()
    zip_result = evl.zip_evaluate(coefs, words)
    enum_result = evl.zip_evaluate(coefs, words)
    print("Testing with")
    print(f"words = {words}")
    print(f"coefs = {coefs}")
    print(f"zip_evaluate() : {zip_result}")
    print(f"enumerate_evaluate() : {enum_result}")
    print()

if __name__ == '__main__':
    test_evaluator([1.0, 2.0, 1.0, 4.0, 0.5], ["Le", "Lorem", "Ipsum", "est", "simple"])
    test_evaluator([1, 2, 3], ["a", "b", "c"])
    test_evaluator([1], ["one", "two"])
    test_evaluator([1, 2, 3], 42.0)
    test_evaluator([1, "two", 3], ["a", "b", "c"])
