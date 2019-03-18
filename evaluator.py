from dispatch import table, arity_table
from tokenizer import Tokenizer

class Evaluator:

    def _eval_proc(self, pname, *args):

        return table[pname](*args)

    def eval(self, tok, repcount=-1):

        results = []
        
        token = tok.get_next()

        while token != None:
            if token in table.keys():
                arity = arity_table[token]
                args = []
                i = 0

                while i < arity:
                    arg_token = tok.get_next()

                    if arg_token == 'repcount':
                        args.append(repcount)
                        i += 1
                    elif arg_token in table.keys():
                        args.append(arg_token)
                        i -= arity_table[arg_token] - 1
                    else:
                        args.append(arg_token)
                        i += 1

                arg_tok = Tokenizer()
                arg_tok.tokens = args
                
                result = self._eval_proc(token, *self.eval(arg_tok))
                if isinstance(result, list):
                    results += result
                elif result != None:
                    results.append(result)
            elif token == 'repeat':
                getting_count = True
                count_expr = []
                
                while getting_count:
                    if tok.peek_next() == '[':
                        getting_count = False
                    else:
                        count_expr.append(tok.get_next())

                cnt_tok = Tokenizer()
                cnt_tok.tokens = count_expr
                cnt = int(self.eval(cnt_tok)[0])

                start_idx = tok.tokens.index('[') + 1
                end_idx = len(tok.tokens) - 1 - tok.tokens[::-1].index(']')
                
                for i in range(cnt):
                    sub_tok = Tokenizer()
                    sub_tok.tokens = tok.tokens[start_idx:end_idx]
                    result = self.eval(sub_tok, repcount=i + 1)
                    if isinstance(result, list):
                        results += result
                    elif result != None:
                        results.append(result)

                tok.tokens = tok.tokens[end_idx + 1:]
                tok.lookahead = 0
            elif token == 'to':
                name = tok.get_next()
                getting_params = True
                params = []

                while getting_params:
                    if tok.peek_next()[0] == ':':
                        params.append(tok.get_next())
                    else:
                        getting_params = False

                getting_body = True
                body = []

                while getting_body:
                    if tok.peek_next() == 'end':
                        tok.get_next()
                        getting_body = False
                    else:
                        body.append(tok.get_next())

                table[name] = Procedure(body, *params)
                arity_table[name] = table[name].arity
            elif token == 'if':
                cond_expr = []
                getting_cond = True

                while getting_cond:
                    if tok.peek_next() == '[':
                        getting_cond = False
                    else:
                        cond_expr.append(tok.get_next())

                cond_tok = Tokenizer()
                cond_tok.tokens = cond_expr
                cond = self.eval(cond_tok)[-1]

                tok.get_next()
                body_toks = []
                getting_body = True

                while getting_body:
                    if tok.peek_next() == ']':
                        tok.get_next()
                        getting_body = False
                    else:
                        body_toks.append(tok.get_next())

                if cond:
                    body_tok = Tokenizer()
                    body_tok.tokens = body_toks
                    result = self.eval(body_tok)
                    if result == '__stop__':
                        return results
                    elif isinstance(result, list) and result[0] == 'output':
                        return result[-1]
                    elif isinstance(result, list):
                        results += result
                    elif result != None:
                        results.append(result)
            elif token == 'stop':
                return '__stop__'
            elif token == 'output':
                output_expr = []
                getting_output = True

                while getting_output:

                    if tok.peek_next() == None:
                        tok.get_next()
                        getting_output = False
                    else:
                        output_expr.append(tok.get_next())
                
                output_tok = Tokenizer()
                output_tok.tokens = output_expr
                result = self.eval(output_tok)
                return ['output', result]
            elif isinstance(token, float):
                results.append(token)
            elif isinstance(token, int):
                results.append(token)
            elif token.replace('.', '', 1).isdigit():
                results.append(float(token))

            token = tok.get_next()

        return results    

class Procedure:

    def __init__(self, body, *params):

        self.arity = len(params)
        self.params = params
        self.body = body
        self.args_dict = {}

    def __repr__(self):

        return 'Procedure({}, {})'.format(self.body, self.params)

    def _bind(self, *args):

        for i in range(len(args)):
            self.args_dict[self.params[i]] = args[i]

    def _substitute(self):

        substituted_body = []
        for token in self.body:
            if token in self.params:
                substituted_body.append(self.args_dict[token])
            else:
                substituted_body.append(token)

        return substituted_body

    def __call__(self, *args):

        self._bind(*args)

        substituted_body = self._substitute()

        body_tok = Tokenizer()
        body_tok.tokens = substituted_body

        e = Evaluator()

        return e.eval(body_tok)












