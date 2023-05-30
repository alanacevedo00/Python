import calculadora


def main():
    sum = calculadora.suma(2, 2)
    res = calculadora.resta(10, 5)
    mul = calculadora.multiplicacion(4, 4)
    div = calculadora.division(8, 2)

    print("la suma es", sum)
    print("la resta es", res)
    print("la multiplicacion es", mul)
    print("la division es", div)




if __name__ == "__main__":
    main()
