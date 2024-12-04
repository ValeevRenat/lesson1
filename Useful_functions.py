numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

prime = []
not_prime = []

for number in numbers:
    if number == 1:
        continue
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        prime.append(number)
    else:
        not_prime.append(number)

print("Primes:", prime)
print("Not Primes:", not_prime)
