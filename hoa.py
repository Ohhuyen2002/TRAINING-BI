def weatherForecast():
    data1=open('dubaothoitiet.txt')
    data1=data1.read()
    print(data1)
    data2=open('kyhieu.txt','r')
    data2=data2.read()
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