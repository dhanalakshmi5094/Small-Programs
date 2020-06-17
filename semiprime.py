def isSemiPrime(number):
    result = False

    primes = []
    #pdb.set_trace()
    for i in range(2, int(number / 2) + 1):

        while number % i == 0:
            number = int(number / i)
            primes.append(i)

            if len(primes) >= 2:
                break
    # end for loop

    if number > 1:
        primes.append(number)

    if len(primes) == 2:
        result = True
        n = primes[0] * primes[1]
        print(f"{primes[0]} * {primes[1]} = {n}")

    return result


number = int(input("Please enter number"))

print(isSemiPrime(number))
