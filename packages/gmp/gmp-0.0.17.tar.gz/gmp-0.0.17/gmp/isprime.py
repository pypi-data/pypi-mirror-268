def isprime(num):
  primes = []
  for i in range(2,num):
    if num%i==2:
      primes.append(i)
  return len(primes) == 2