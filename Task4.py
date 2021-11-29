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