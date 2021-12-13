# Thuận toán: 
#Sắp xếp lại danh sách cho thỏa yêu cầu rồi lấy 3 người đầu tiên của danh sách


from typing import TYPE_CHECKING, List

class Employees:
   listEmployee=[]
   def __init__(self, name, birth, position, skill, beginning_year):
      self._name=name
      self._birth=birth
      self._position=position
      self._skill=skill
      self._beginning_year=beginning_year  
      Employees.recruit_employee(self)
            
   @classmethod         
   def recruit_employee(list, self):
        list.listEmployee.append(self) 
     
                   
   def info(self):
        print( f"Name: {self._name} - Birth: {self._birth} - \
Position: {self._position} - Skills: {self._skill} - Beginning-year: {self._beginning_year}")
        
       
   def compare_skill(self, other):
           if(self._skill<other._skill): return False
           elif(self._skill==other._skill): return 1
   
   
   def count_year(self):
          year=2021-self._beginning_year
          return year
   
   
   def experience(self, other):
          if(self.count_year()<other.count_year()): return False
          elif(self.count_year()==other.count_year()): return 1
          
   
   def compare_name(self, other):                        
       self_split = self._name.split()
       self_last_name = self_split[len(self_split)-1]
       other_split = other._name.split()
       other_last_name = other_split[len(other_split)-1]
       if (self_last_name>other_last_name): return False  
        
   @classmethod                          
   def sort(list):
         for i in range(0, len(list.listEmployee)-1):
                for j in range(i+1, len(list.listEmployee )):
                     if(list.compare_skill(list.listEmployee[i], list.listEmployee[j])==False):
                                list.listEmployee[i], list.listEmployee[j]=list.listEmployee[j], list.listEmployee[i] 
                     elif(list.compare_skill(list.listEmployee[i], list.listEmployee[j])==1):
                                   if(list.experience(list.listEmployee[i], list.listEmployee[j])==False):
                                           list.listEmployee[i], list.listEmployee[j]=list.listEmployee[j], list.listEmployee[i] 
                                   elif(list.experience(list.listEmployee[i], list.listEmployee[j])==1) :
                                          if(list.compare_name(list.listEmployee[i], list.listEmployee[j])==False):
                                                list.listEmployee[i], list.listEmployee[j]=list.listEmployee[j], list.listEmployee[i]
   
   
   @classmethod
   def output(list): 
            for i in range (0, 3):
                 list.info(list.listEmployee[i])  
                                                                                                 
          
          
def main(): 
       employee1 = Employees(name="EXO", birth=1995, position="Sales Team", skill=30, beginning_year=2020)
       employee2 = Employees("EXO-L", 2002, "IT Team", 30, 2021)
       employee3 = Employees("Vo Quang Thang", 1985, "Telesales Team", 10, 2019)
       employee4 = Employees("Ho Gia Loc",2002, "MKT Team", 20, 2018)
       employee5 = Employees("Le Hoang Phuc", 1992, "AI Team", 5, 2017)
       employee6 = Employees("Nguyen Thanh Tung", 1996, "Sales Team", 13, 2017)
       employee7 = Employees("Tran Tuan Thai", 1997, "Telesales Team", 22, 2016)
       employee8 = Employees("Trinh Hoang Long", 2000, "IT Team", 14, 2015)
       employee9 = Employees("Nguyen Minh Khoi", 1997, "MKT Team", 20, 2019)
       employee10 = Employees("Bui Trinh Trung", 1999, "Sales Team", 20, 2020)
       employee11 = Employees("Vo Hoai Linh", 1960, "Telesales Team", 19, 2017)
       employee12 = Employees("Oh Chansol", 2004, "Telesales Team", 30, 2014)
       employee13 = Employees("Nguyen Thuy Chi", 2002, "Sales Team", 17, 2018)
       employee14 = Employees("Hoang Thuy Linh", 2000, "IT Team", 16, 2017)
       employee15 = Employees("Nguyen Thanh Tung", 1995, "MKT Team", 17, 2018)
       employee16 = Employees("Nguyen Bao Khanh", 2001, "BI Team", 19, 2019)
       employee17 = Employees("Tran Phuong Tuan", 1997, "AI Team", 13, 2021)
       employee18 = Employees("Nguyen Duc Cuong", 1993, "BI Team", 7, 2017)
       employee19 = Employees("Nguyen Minh Hang", 1996, "IT Team", 17, 2013)
       employee20 = Employees("Khac Hung", 1992, "Telesales Team", 14, 2016)

       print("\n\n\n 3 BEST EMPLOYEES")
       Employees.sort()
       Employees.output()
       
       
if __name__ == "__main__":
    main()
   