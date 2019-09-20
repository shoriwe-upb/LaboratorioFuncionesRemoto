def a_power_b(a, b):
    result = 1
    mult = 1
    while mult <= b:
        result *= a
        mult += 1
    return result


def main():
    while True:
        a = int(input("Numero a: "))
        if not a:
            break
        b = int(input("Numero b: "))
        result = a_power_b(a, b)

        print(result)


if __name__ == "__main__":
    main()
