x=int(input('Enter a number: '))


def isPrime(x):
    if( x==2):
        return True
    if (x<=1):
        return False
    for i in range(2, x):
        if(x%i==0):
            return False
    return True

print(isPrime(x))