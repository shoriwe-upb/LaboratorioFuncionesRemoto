def a_power_b(a, b):
    result = 1
    mult = 1
    while mult <= b:
        result *= a
        mult += 1
    return result


def _input(msg, is_b=False):
    while True:
        try:
            value = int(input(msg))
            if is_b:
                if value < 10000:
                    return value
                else:
                    print("El exponente genera demasiados cilclos para el computador\nExponente < 10000")
            else:
                return value
        except ValueError:
            pass


def main():
    while True:
        a = _input("Numero a: ")
        if not a:
            break
        b = _input("Numero b: ", True)

        result = a_power_b(a, b)

        print(f"Result: {result}")


if __name__ == "__main__":
    main()
