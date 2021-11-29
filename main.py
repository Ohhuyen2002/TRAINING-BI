#task 1
x=int(input('Enter a number: '))
def isPrime(x):
    if( x==2):
        return True
    if (x<=1):
        return False
    for i in range(2, x-1):
        if(x%i==0):
            return False
    return True
print(isPrime(x))
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
#task 4
#Read weather forecast file
file=open('dubaothoitiet.txt')
data1=file.read()
file.close()
print(data1)
#Read symbol file
fp=open('kyhieu.txt')
data2=fp.read()
fp.close()
print(data2)
#Transform string to dict
weather_forecast = dict((x.strip(), y.strip())
                     for x, y in (element.split(':')
                                  for element in data1.split('\n')))

print( weather_forecast)
symbol=dict((x.strip(), y.strip())
                     for x, y in (element.split(':')
                                  for element in data2.split('\n')))
week=['Monday', 'Tuesday', 'Wednesday',
     'Thursday', 'Friday', 'Saturday', 'Sunday']
print(symbol)
day=input("Enter today (ex: Monday-2/10/2022): ")
n=int(input("Enter a number: n="))
while(n<=0):
    n=int(input("Enter a number again: n= "))
today=day.split('-')
if(today[1] in weather_forecast and today[0] in week):
    temp=list(weather_forecast)
    for j in range(1, len(temp)):
        if(today[1]==temp[j]):
            break
    for i in range(0, len(week)):
        if(today[0]==week[i]):
            break
    for j in range(j, j+n):
        if(j>=len(temp)):
            break
        print(week[i], end=" - ")
        print(temp[j],end=": ")
        print(symbol[weather_forecast[temp[j]]])
        i+=1
        if(i==7):
            i=0
else:
    print('Is\'nt in file')