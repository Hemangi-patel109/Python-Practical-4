#Write a python program to print list of prime numbers upto N using loop and else clause.

primes = []
n = int(input("Enter the value of N: "))

for num in range(2, n + 1):  
    for i in range(2, int(num ** 0.5) + 1):  
        if num % i == 0:
            break  
    else:
        primes.append(num)  

print(primes)