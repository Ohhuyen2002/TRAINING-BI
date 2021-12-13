from task1 import Employees
class Tech_Em(Employees):
    
    listEmployee=[]
    
    
    def __init__(self, name, birth, position, skill, beginnig_year, program_language, project):
        super().__init__(name, birth, position, skill, beginnig_year)
        self.program_language =  program_language
        self.project = project
        Tech_Em.recruit_employee(self)
        
        
    def info(self):
        print( f"Name: {self._name} - Birth: {self._birth} - \
Position: {self._position} - Skills: {self._skill} - Started: {self._beginning_year} - \
Program Language: {self.program_language} - Project: {self.project}")
         
           
               
    def check_python(self):
        if("Python" in self.program_language):return True
    
    
    
    def check_age(self):
        old=2021-self._birth
        if(old>=30): return True
        
        
    def check_proj(self):
        if(self.project>5): return True
        
        
    @classmethod
    def python_team(list):
        Py_Team=[]
        for i in range(0, len(list.listEmployee)):
            if(list.check_python(list.listEmployee[i])==True):
                Py_Team.append(list.listEmployee[i])
                
        for i in range (0, len(Py_Team)):
                 Py_Team[i].info()
    
    
    @classmethod
    def experienced_team(list):
        Ex_Team=[]
        for i in range(0, len(list.listEmployee)):
            if(list.check_age(list.listEmployee[i])==True) and (list.check_proj(list.listEmployee[i])==True):
                Ex_Team.append(list.listEmployee[i])
        
        for i in range (0, len(Ex_Team)):
                 Ex_Team[i].info() 
                     

def main():   
    employee21 = Tech_Em("Nguyen Minh Phuc", 2002, "AI Team", 10, 2021,"Python", 6)
    employee22 = Tech_Em("Nguyen Thi Huyen", 2002, "IT Team", 10, 2021, "Python", 10)
    employee23 = Tech_Em("Do Ngoc Cuong", 1985, "BI Team", 15, 2020, "C#", 2)
    employee24 = Tech_Em("Nguyen Thi Hoa", 1984, "IT Team", 10, 2020, "Java", 3)
    employee25 = Tech_Em("Ngo Dinh", 1970, "AI Team", 15, 2021, "Javascript", 3)
    employee26 = Tech_Em("Nguyen Phuong Thao", 1975, "BI Team", 20, 2021, "Javascript", 3)
    employee27 = Tech_Em("Oh Sehun", 1979, "AI Team", 25, 2021, "C#", 21)
    employee28 = Tech_Em("Tieu Vy", 2001, "BI Team", 15, 2021, "C++", 20)
    employee29 = Tech_Em("Nguyen Ngoc Nguyen", 1970, "IT Team", 20, 2021, "Javascript", 4)
    employee30 = Tech_Em("Do Quoc Trung", 1995, "AI Team", 30, 2021, "Java", 3)
    employee31 = Tech_Em("Byun Baekhyun", 1970, "AI Team", 15, 2021, "C#", 30)
    employee32 = Tech_Em("Hai Dang", 1970, "AI Team", 15, 2021, "R, Python", 2)
    employee33 = Tech_Em("Nguyen Tam Nhu", 2003, "IT Team", 20, 2020, "Ruby", 4)
    employee34 = Tech_Em("Nguye Ngoc Duy", 2000, "IT Team", 15, 2021, "Swift, C", 2)
    employee35 = Tech_Em("Park Chanyeol", 1988, "IT Team", 10, 2019, "Scala, Swift", 26)
    print("\n\n\n Python Team have: ")
    Tech_Em.python_team()
    print("\n\n\n Experienced Team have: ")
    Tech_Em.experienced_team()
    
if __name__ == "__main__":
    main()

