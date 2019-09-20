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
    primes = 0
    while True:
        try:
            number = int(input("Numero N: "))
            if number <= 0:
                break
            result = is_prime(number)

            if result:
                primes += 1
                print(1)
            else:
                print(0)
        except ValueError:
            print(-1)

    print(f"{primes} primes founded")
    if is_prime(primes):
        msg = "is prime"
    else:
        msg = "is not prime"
    print(f"{primes} {msg}")

if __name__ == '__main__':
    main()
