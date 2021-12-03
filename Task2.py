#task 2

def least_common_multiple(number1, number2):
    if number1>number2:
        temp=number1
    else:
        temp=number2
    i=2
    LCM=temp
    while (LCM%number1!=0 or LCM %number2!=0):
        LCM=temp*i
        i+=1
    return LCM

def main():
    number1=int(input('Enter the firt number: '))
    number2=int(input('Enter the second number: '))
    print('LCM:', end=' ')
    print(least_common_multiple(number1, number2))
    
    
if __name__=="__main__":
    main()