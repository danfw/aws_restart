## This code display a list of prime numbers between 1 to 250 ##
## also add a prime.txt with the prime numbers list ##

# Define a function to check if a number is prime
def is_prime(n):
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

# Generate a list of prime numbers between 1 and 250
primes = []
for i in range(2, 251):
  if is_prime(i):
    primes.append(i)

# Store the prime numbers in a file
with open("prime.txt", "w") as f:
  for prime in primes:
    f.write(str(prime) + "\n")

# Display the prime numbers to the console
print("Prime numbers between 1 and 250:")
for prime in primes:
  print(prime)
