#task1

def isPrime(number):
    if( number==2):
        return True
    if (number<=1):
        return False
    for i in range(2, number):
        if(number%i==0):
            return False
    return True


def main():
    number=int(input('Enter a number: '))
    print(isPrime(number))
    
    
if __name__=="__main__":
    main()
