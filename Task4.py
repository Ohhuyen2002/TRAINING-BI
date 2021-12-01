#task 4

def read_file(name_file):
    file=open(name_file)
    data1=file.read()
    file.close()
    return (data1)


def transform_string_to_dict (data):
    newDict= dict((key.strip(), value.strip())
                     for key, value in (element.split(':')
                                  for element in data.split('\n')))
    return newDict


def find_position(day, array):
    for i in range(0, len(array)):
            if(day==array[i]):
                return i
            
            
def check_and_print (today, weatherForecast, weatherSymbol, week , number):
    
    if(today[1] in weatherForecast and today[0] in week):
        Ddmmyy=list(weatherForecast)
        positionDay=find_position(today[0], week)
        positionDdmmyy=find_position(today[1], Ddmmyy)
        
        for positionDdmmyy in range(positionDdmmyy, positionDdmmyy+number):
            if(positionDdmmyy>=len(Ddmmyy)):
                break
            print(week[positionDay], end=" - ")
            print(Ddmmyy[positionDdmmyy],end=": ")
            print(weatherSymbol[weatherForecast[Ddmmyy[positionDdmmyy]]])
            positionDay+=1
            if(positionDay==7):positionDay=0
    else:
        print('Isn\'t in file')


def main():
    week=['Monday', 'Tuesday', 'Wednesday',
     'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    data1=read_file("dubaothoitiet.txt")
    data2=read_file("kyhieu.txt")
    weatherForecast=transform_string_to_dict(data1)
    weatherSymbol=transform_string_to_dict(data2)
    
    day=input("Enter today (ex: Monday-2/10/2022): ")
    today=day.split('-')
    number=int(input("Enter a number: "))
    while(number<=0):
        number=int(input("Enter a number again:  "))
        
    check_and_print(today, weatherForecast, weatherSymbol, week, number)
    

if __name__=="__main__":
    main()


    
    