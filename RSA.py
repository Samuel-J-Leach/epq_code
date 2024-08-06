from random import randint

#returns two prime numbers
def Primes(n):
    num = 12
    primes = [2, 3, 5, 7, 11]
    #loops until the last item in primes is larger than x
    while primes[len(primes)-1] < n:
        prime = True
        #half the list is compared to the current value of num
        for i in range((len(primes)//2) + 1):
            #if num is divisible by any other prime number, num is not prime
            if num % primes[i] == 0:
                prime = False
        #if num is prime it is added to primes
        if prime == True:
            primes.append(num)
        num += 1
    return primes

def prime_pair(limit):
    primes = Primes(limit)
    #prime1 is the largest prime number in the primes list
    prime1 = primes[len(primes)-1]
    #prime2 is a random item from the primes list
    prime2 = primes[randint(0,len(primes)-2)]
    #returns the two prime numbers as a tuple
    return prime1, prime2

#calculates the totient of two numbers
def Totient(a,b):
    return (a-1)*(b-1)

#returns a co-prime of x which is less than x
def coprime(num1):
    num2 = 2
    amount = 0
    coprimes = []
    primes = Primes(num1)
    while num2 < num1:
        coprime = True
        for i in primes:
            if num1 % i == 0 and num2 % i == 0:
                coprime = False
        if coprime == True:
            amount += 1
            coprimes.append(num2)
        num2 += 1
    num2 = coprimes[randint(0,len(coprimes)-2)]
    return num2

#returns the greatest common divisor of two given numbers
def gcd(a, b):
    gcd = 1
    for i in range(a):
        #checks if i is a common factor of a and b
        if a % (i+1) == 0 and b % (i+1) == 0:
            #updates gcd
            gcd = i+1
    return gcd

#finds two numbers that satisfy bezout's theorem and returns the largest
def D(x,y):
    #gcd of x and y
    gcdxy = gcd(x, y)
    #holds multiples of x
    x_multiples = []
    #holds multiples of y
    y_multiples = []
    
    count = 0
    while True:
        count += 1
        #adds a multiple of x to x_multiples
        x_multiples.append(x*count)
        #adds a multiple of y to y multiples
        y_multiples.append(y*count)
        
        for i in range(count):

            #checks if there are any combinations of multiples of x and y that satisfy bezout's identity
            
            if x_multiples[count-1] + (y_multiples[i] * -1) == gcdxy:
                return (x_multiples[count-1] / x)

            elif x_multiples[i] + (y_multiples[count-1] * -1) == gcdxy:
                return (x_multiples[i] / x)

            elif (x_multiples[count-1] * -1) + y_multiples[i] == gcdxy:
                return (y_multiples[i] / y)

            elif (x_multiples[i] * -1) + y_multiples[count-1] == gcdxy:
                return (y_multiples[count-1] / y)


#generates a public and private key
def Keys(x,y):
    n = x*y
    totient = Totient(x,y)
    e = coprime(totient)
    public_key = (n,e)

    d = D(totient, e)
    private_key = (n,int(d))
    return [public_key, private_key]

#converts plain text to cipher text and vice versa using the public/private key
def conversion(key,original):
    return ((original**key[1]) % key[0])

#creates a record of keys used
def log(keys):
    file = open("log.txt","a")
    record = "public:" + str(keys[0]) + "      private:" + str(keys[1]) + "\n"
    file.write(record)
    file.close()

#############main#################

#encrypts a number with a given public key or generates a public key to use
def ENCRYPT(num, public):
    private = "empty"
    if public == "empty":
        found = False
        while found == False:
            primes = prime_pair(num)
            keys = Keys(primes[0],primes[1])
            public = keys[0]
            private = keys[1]
            if conversion(public, num) != num:
                if conversion(private, conversion(public, num)) == num:
                    log([public, private])
                    found = True
    return (conversion(public, num), public, private)

#decrypts a number with a given private key    
def DECRYPT(num, private):
    return conversion(private, num)

#stands for 'brute force private key'
#obtains the private key linked to a given public key via brute force
def BFPK(num, public):
    n = int(public[0])
    e = int(public[1])
    limit = n // 2

    primes = Primes(limit)
    for i in range(len(primes)):
        if n % primes[i] == 0:
            x = primes[i]
            y = int(n / primes[i])
            
    totient = Totient(x, y)
    d = int(D(totient, e))
    original = conversion((n,d), int(num))
    private = (n,d)
    return (original, private)

#returns all keys that were generated previously and stored in an external file
def VIEWLOG():
    log = []
    file = open("log.txt","r")
    for line in file:
        log.append(line)
    file.close()
    return log


'''
num = int(input("enter numbrrrrr: "))

action = input("'encrypt', 'decrypt', or 'view log': ")
if action == "encrypt":
    primes = prime_pair(num)
    keys = Keys(primes[0],primes[1])
    print(keys)
    public = keys[0]
    private = keys[1]
    print(conversion(public, num))
elif action == "decrypt":
    n = int(input("n: "))
    d = int(input("d: "))
    private = (n,d)
    print(conversion(private, num))
elif action == "view log":
    file = open("log.txt","r")
    for line in file:
        print(line.strip())
    file.close()
'''

#returns the prime factors of x
'''
def prime_factors(x):
    prime_factors = []
    primelist = Primes(x)
    #loops loops through every item in primelist
    for i in range(len(primelist)):
        #if x is divisible by a prime number it is a prime factor of x
        if x % primelist[i] == 0:
            #the prime factor is added to prime_factors
            prime_factors.append(primelist[i])
    return prime_factors
'''
