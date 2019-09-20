def is_prime(number):
    if not number:
        return False
    number = abs(number)
    half = number / 2
    div = 2
    while div <= half:
        if not number % div:
            return False
        div += 1
    return True


def main():
    number = int(input("Numero N: "))
    result = is_prime(number)

    if result:
        print("Is a prime number")
    else:
        print("Is NOT a prime number")


if __name__ == '__main__':
    main()
