from Genalgo.Translate import Translate

def input_translate(func):
    def wrapper(genome):
        inputs = []
        for gene in genome:
            inputs.append(Translate(genome, gene))

        return func(inputs)

    return wrapper