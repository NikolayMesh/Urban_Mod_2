numbers = [11, 22, 31, 49, 27]
primes = []
not_primes = []
is_prim = 0
for i in range(len(numbers)):
    for j in range(2, numbers[i]):
        if numbers[i] % j == 0 and numbers[i] != j:
            is_prim = False
            break
        else:
            is_prim = True
    if is_prim == False:
        not_primes.append(numbers[i])
    else:
        primes.append(numbers[i])
print('primes ', primes)
print('not_primes ', not_primes)
