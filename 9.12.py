def prime_factors(n, fact=2):
    if n < 2:
        return []
    if n % fact == 0:
        return [fact] + prime_factors(n // fact, fact)
    return prime_factors(n, fact + 1)

print(list(set(prime_factors(60))))
