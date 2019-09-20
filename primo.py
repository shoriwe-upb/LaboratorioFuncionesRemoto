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
    while True:
        try:
            number = int(input("Numero N: "))
            if number <= 0:
                break
            result = is_prime(number)

            if result:
                print(1)
            else:
                print(0)
        except:
            print(-1)


if __name__ == '__main__':
    main()
