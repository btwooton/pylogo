class Tokenizer:

    def __init__(self):

        self.tokens = []

    def tokenize(self, expression):

        self.tokens += expression.split()
        self._preprocess_tokens()

    def _preprocess_tokens(self):

        preprocessed = []

        for token in self.tokens:

            if token == '+' or token == '-' or token == '*' or token == '/':
                last = preprocessed[-1]
                preprocessed = preprocessed[:-1]
                preprocessed.append(token)
                preprocessed.append(last)
            elif token == '=' or token == '<' or token == '>':
                last = preprocessed[-1]
                preprocessed = preprocessed[:-1]
                preprocessed.append(token)
                preprocessed.append(last)
            else:
                preprocessed.append(token)

        self.tokens = preprocessed

    def get_next(self):

        if len(self.tokens) > 0:
            result = self.tokens[0]
            self.tokens = self.tokens[1:]
            return result
        else:
            return None

    def peek_next(self):

        if len(self.tokens) > 0:
            return self.tokens[0]
        else:
            return None

    def __repr__(self):

        return 'Tokenizer({})'.format(self.tokens)
