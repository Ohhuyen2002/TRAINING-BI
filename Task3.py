#task 3
n=int(input('Enter a number: '))
while n<=0:
    n=int(input('Enter a number again: '))
def star_pynamid(n):
    k=2*n-2
    while(n>=1):
        for j in range(k,0,-1):
                print(end="  ")
        k = k +1
        for j in range(1, 2*n):
            print('*', end=" ")
        print('\t')
        n-=1
star_pynamid(n)