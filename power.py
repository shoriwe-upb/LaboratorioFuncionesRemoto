def a_power_b(a, b):
    result = 1
    mult = 1
    while mult <= abs(b):
        result *= a
        mult += 1
    if b < 0:
        result = 1 / result
    return result


def _input(msg, is_b=False):
    err = 0
    while True:
        try:
            value = int(input(msg))
            if is_b:
                if value < 10000:
                    return err, value
                else:
                    print("El exponente genera demasiados cilclos para el computador\nExponente < 10000")
            else:
                return err, value
        except ValueError:
            err += 1


def main():
    errs = 0
    even = 0
    odds = 0
    while True:
        err, a = _input("Numero a: ")
        errs += err
        if not a:
            print()
            break
        err, b = _input("Numero b: ", True)
        errs += err

        result = a_power_b(a, b)
        print(f"Result: {result}")

        if result % 2:
            odds += 1
        else:
            even += 1
        print()
    print(f"Potencias calculadas {even + odds}")
    print(f"Resultados pares: {even}")
    print(f"Resultados impares: {odds}")
    print(f"Numero de errores: {errs}")


if __name__ == "__main__":
    main()
