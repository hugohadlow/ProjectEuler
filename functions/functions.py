import math

def sumMultiples(factors, n): #Question 001
    total = 0
    for x in range(1, n):
        for f in factors:
            if x%f==0:
                total += x
                break
    return total

def sumEvenTerms(list): #Question 002
    sum = 0
    for x in list:
        if x%2==0: sum+=x
    return sum

def fibonacci(n): #Terms <= n
    list=[]
    a=1
    b=2
    c=0
    while(a<=n):
        list.append(a)
        c = a+b
        a = b
        b = c
    return list

def nextPrime(ps):
    if not ps: return 2
    i = ps[-1] + 1
    while(True):
        isPrime = True
        for p in ps:
            if i%p==0:
                isPrime = False
                break
        if isPrime: break
        i+=1
    return i

def primes(n:int):
    ps = []
    while(True):
        np = nextPrime(ps)
        if np>n: break
        ps.append(np)
    return ps

def primeFactors(n):
    primes = [2]
    p = 2
    factors = []

    while (True):
        if n%p==0:
            factors.append(p)
            n = n//p
            if n==1: break
        else:
            p = nextPrime(primes)
            primes.append(p)

    if not factors: return [n]
    return factors

def palindrome(n:int):
    s = str(n)
    l = len(s)
    for i in range(0, (l//2)):
        if s[i]!=s[(l-i)-1]: return False
    return True

def largestPalindromeProduct(d):
    n = (10**d) - 1
    nn = (10**(d-1)) - 1
    for i in range(n,nn, -1):
        pairs = pairsWhichSum(n, i)
        products = map(lambda x: x[0]*x[1], pairs)
        palindromes = list(filter(lambda x: palindrome(x), products))
        if palindromes: return max(palindromes)

def pairsWhichSum(a, b):
    result = []
    while (a>=b):
        result.append([a,b])
        a-=1
        b+=1
    return result

def smallestMultiple(n):
    primeFactorLists = []
    for i in range(2, n+1): #Fetch prime factors for each number from 1 to n
        primeFactorLists.append(primeFactors(i)) #Should make this more efficient by reusing calculated primes
    d = {}
    for primeFactorList in primeFactorLists:
        consolidated = {}
        for pf in primeFactorList:
            if pf in consolidated:
                consolidated[pf]+=1
            else: consolidated[pf]=1

        for k in consolidated:
            if k in d:
                if consolidated[k]>d[k]: d[k]=consolidated[k]
            else:
                d[k] = consolidated[k]

    product = 1
    for k in d:
        product *= k**d[k]
    return product