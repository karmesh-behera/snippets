from math import floor 

def primes(n):
    arr = [2*i+1 for i in range(2, floor(n/2))]

    primes = [2]


    return arr



def sieve(n):
    prime = [True for i in range(n+1)]
    arr = []
    p = 2
    while (p * p <= n):
 
        if (prime[p] == True):
 
  
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
 
  
    for p in range(2, n):
        if prime[p]:
            arr.append(p)
    return arr
            









def main():
    print(sieve(100))


if __name__ == "__main__":
    main()