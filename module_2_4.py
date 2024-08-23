numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
devid =[2, 3, 5]
for i in range(1, len(numbers)):
    for j in devid:
        is_prim = False
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