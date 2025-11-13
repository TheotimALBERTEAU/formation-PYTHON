import functools

def input_translate(func):
    @functools.wraps(func)
    def wrapper(genome, **fct_cfg):
        inputs = []
        for gene in genome:
            inputs.append((fct_cfg['higher'] - fct_cfg['lower']) * gene + fct_cfg['lower'])

        return func(inputs, **fct_cfg)

    return wrapper