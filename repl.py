from evaluator import Evaluator
from tokenizer import Tokenizer

if __name__ == '__main__':

    t = Tokenizer()
    e = Evaluator()

    while True:

        expr = input('> ')

        t.tokenize(expr)

        results = e.eval(t)

        unit_count = 0

        for result in results:

            if result == () and unit_count == 0:
                print(result)
                unit_count += 1
            elif isinstance(result, tuple):
                for subresult in result:
                    print(subresult)
            elif result != None and result != ():
                print(result)
            


