#task 2
x=int(input('Enter the firt number: '))
y=int(input('Enter the second number: '))
def least_common_multiple(a, b):
    if a>b:
        temp=a
    else:
        temp=b
    i=2
    tmp=temp
    while (tmp%a!=0 or tmp %b!=0):
        tmp=temp*i
        i+=1
    return tmp
print(least_common_multiple(x, y))