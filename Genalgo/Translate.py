from Genalgo.Decorators.InputTranslate import input_translate

@input_translate
def translate(list, n : float):
    b = list[0]
    a = list[-1] - b
    return a * n + b