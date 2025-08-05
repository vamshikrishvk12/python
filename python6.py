# prime numbers program #
n=int(input())
is_prime=True
for i in range(2,n):
    if n%i==0:
      is_prime=False
print("is a prime" if is_prime else "is not prime")