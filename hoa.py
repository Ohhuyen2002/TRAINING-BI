data1=open('dubaothoitiet.txt','r')
print(data1)
data2=open('kyhieu.txt','r')
print(data2)
weekdays=[ 'Monday','Tuesday','Wednesday','Thursday', 'Friday', 'Saturday', 'Sunday']
Forecast=dict(
        (key.strip(),value.strip())
            for key, value in (tmp.split(':')
                for tmp in data1.split('\n'))
    )
print(Forecast) 

weatherSymbol=dict(
        (Key.strip(), Value.strip())
            for Key, Value in (temp.split(':')
                for temp in data2.split('\n'))
    )
print(weatherSymbol)