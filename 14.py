a=int(input('Enter a:'))
while a<=0:
    print('Invalid input!\n')
    a=int(input('a must be greater than 0!\nTry again:'))
b=int(input('Enter b:'))
while b<=a:
    b=int(input('b must be greater than a!\nTry again:'))
d=int(input('Enter d:'))
m=0
flag=True
lista=[]
for x in range(a,b+1):
        lista.append(x)
print (lista)
primes = []
for possiblePrime in lista:
    prime = True
    for number in range(2, possiblePrime):
        if possiblePrime % number == 0:
            prime = False
            break
    if prime:
        if possiblePrime != 1:
            primes.append(possiblePrime)
print (primes)
for l in primes:
    if (abs(l-primes[m-1])==d):
        print(primes[m-1],l)
        flag=False
    else:
        m=m+1
if flag:
    print('There is not such pair of prime numbers in [',a,',',b,'] to equal',d)