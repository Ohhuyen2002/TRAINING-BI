#task 3

def star_pynamid(number):
    num=2*number-2
    while(number>=1):
        for j in range(num,0,-1):
                print(end="  ")
        num = num +1
        for j in range(1, 2*number):
            print('*', end=" ")
        print('\t')
        number-=1
        
        
def main():
    number=int(input('Enter a number: '))
    while number<=0:
        number=int(input('Enter a number again: '))
    star_pynamid(number)
    
    
if __name__ == "__main__":
    main()