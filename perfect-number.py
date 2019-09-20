def extract_divisors(number):
    if number >= 0:
        div = 1
        while div < number:
            if not number % div:
                yield div
            div += 1
    else:
        div = -1
        while div > number:
            if not number % div:
                yield div
            div += -1


def perfect_number(number):
    divisors = tuple(extract_divisors(number))
    return sum(divisors) == number


def near_to_perfect(number):
    divisors = tuple(extract_divisors(number))
    sumatory = sum(divisors)
    print(sumatory)
    return sumatory - 3 <= number <= sumatory + 3


def main():
    number = int(input("Numero: "))
    result = perfect_number(number)
    if result:
        print("Es un numero perfecto")
    else:
        print("No es un numero perfecto")
        result = near_to_perfect(number)
        if result:
            print("Es un numero casi perfecto")
        else:
            print("Tampoco es casi perfecto")


if __name__ == '__main__':
    main()
