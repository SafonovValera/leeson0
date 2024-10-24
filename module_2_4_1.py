numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
for i in numbers[1:]:
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        primes.append(i)
print('Primes:', primes)
not_primes = list(set(numbers[1:]) - set(primes))
print('Not Primers:', not_primes)
