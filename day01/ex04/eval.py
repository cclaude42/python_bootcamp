class Evaluator:

    def zip_evaluate(coefs, words):
        if len(coefs) == len(words):
            zipped = zip(coefs, words)
            total = 0
            for elem in zipped:
                total += elem[0] * len(elem[1])
            return (total)
        else:
            return (-1)

    def enumerate_evaluate(coefs, words):
        if len(coefs) == len(words):
            total = 0
            for count, elem in enumerate(words):
                total += coefs[count] * len(elem)
            return (total)
        else:
            return (-1)
