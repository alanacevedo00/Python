from functools import reduce

numeros = [1,2,3,4,5,6,7,8,9,10]

def impares(x):
    if x % 2 > 0:
        return True

    return False


resultados = filter(impares, numeros)
print(reduce(lambda a, b: a+b, resultados))