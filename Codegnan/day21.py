print("Codegnan university")
class person:
    def __init__(self,name,age,gender,phnno,place):
        self.name=name
        self.age=age
        self.phnno=phnno
        self.gender=gender
        self.place=place
    def display(self):
        print(f"Name:{self.name} \nAge:{self.age} \nGender:{self.gender} \nMobile:{self.phnno} \nPlace:{self.place}")
class student(person):
    std_count=0
    def __init__(self,name,age,gender,phnno,place,std_id,course,dept,dept_id,year):
        super().__init__(name,age,gender,phnno,place)
        self.std_id=std_id
        self.dept=dept
        self.dept_id=dept_id
        self.year=year
        self.course=course
        student.std_count+=1
    def display(self):
        print("================Student Details:==============")
        super().display()
        print(f"Student ID:{self.std_id} \nCourse:{self.course} \nDepartment:{self.dept} \ndepartment id:{self.dept_id} \nyear:{self.year}\n")
class faculty(person):
    fac_count=0
    def __init__(self,name,age,gender,phnno,place,fac_id,subj,dept,dept_id,exp,edu_bg):
        super().__init__(name,age,gender,phnno,place)
        self.dept=dept
        self.dept_id=dept_id
        self.edu_bg=edu_bg
        self.fac_id=fac_id
        self.exp=exp
        self.subj=subj
        faculty.fac_count+=1
    def display(self):
        print("==============Faculty Details=============")
        super().display()
        print(f"Faculty ID:{self.fac_id} \nSubject:{self.subj} \nDepartment:{self.dept} \ndepartment id:{self.dept_id} \nExperience:{self.exp} \nEducation background:{self.edu_bg}\n")
    

class non_tech(person):
    nt_cnt=0
    def __init__(self,name,age,gender,phnno,place,role,dept,dept_id,exp,edu_bg):
        super().__init__(name,age,gender,phnno,place)
        self.role=role
        self.dept=dept
        self.dept_id=dept_id
        self.exp=exp
        self.edu_bg=edu_bg
        non_tech.nt_cnt+=1
    def display(self):
        print("================Non-Technical Staff Details===============")
        super().display()
        print(f"Role:{self.role} \nDepartment:{self.dept} \ndepartment id:{self.dept_id} \nExperience:{self.exp} \nEducation background:{self.edu_bg}\n")

class security(person):
    sec_count=0
    def __init__(self,name,age,gender,phnno,place,role,block):
        super().__init__(name,age,gender,phnno,place)
        self.role=role
        self.block=block
        security.sec_count+=1
    def display(self):
        print("================Security Details======================")
        super().display()
        print(f"Role:{self.role} \nBlock:{self.block}\n")

class cleaning(person):
    c_cnt=0
    def __init__(self,name,age,gender,phnno,place,work):
        super().__init__(name,age,gender,phnno,place)
        self.work=work
        cleaning.c_cnt+=1
    def display(self):
        print("================Cleaning Staff Details==================")
        super().display()
        print(f"Work:{self.work}\n")

class dispensary(person):
    d_cnt=0
    def __init__(self,name,age,gender,phnno,place,role):
        super().__init__(name,age,gender,phnno,place)
        self.role=role
        dispensary.d_cnt+=1
    def display(self):
        print("=============Dispensary Details=============")
        super().display()
        print(f"Role:{self.role}\n")

class drivers(person):
    dr_cnt=0
    def __init__(self,name,age,gender,phnno,place,bus):
        super().__init__(name,age,gender,phnno,place)
        self.bus=bus
        drivers.dr_cnt+=1
    def display(self):
        print("===============Drivers List====================")
        super().display()
        print(f"Bus:{self.bus}\n")


obj=student("kavya",21,"F",3625464776,"Vizag","22vv1a0545","B.TECH","CSE",5,2023)
obj.display()
obj1=faculty("kanchana",40,"F",7583465767,"Vizag","34","AI","CSE",5,"7 years","Ph.D")
obj1.display()
obj2=non_tech("Rohan",35,"M",3432435345,"Vizag","Lab Assistant","CSE",5,"8 years","B.Tech")
obj2.display()
obj3=security("Latha",40,"F",4763657637,"Vizag","Hostel Warden","A")
obj3.display()
obj4=cleaning("Mahesh",45,"M",5465756763,"Vizag","Sweeping")
obj4.display()
obj5=dispensary("Kalyan",35,"M",5454644644,"Vizag","Ward Boy")
obj5.display()
obj6=drivers("Suresh",38,"M",3435435434,"Vizag","Bus A")
obj6.display()
obj7=student("kalavathi",21,"F",3625464776,"Vizag","22vv1a0545","B.TECH","CSE",5,2023)
obj7.display()
print("============Count of Members==============")
print(f"No. of Students:{student.std_count} \nNo. of Teaching staff members:{faculty.fac_count} \nNo. of non-teaching staff members:{non_tech.nt_cnt} \nNo. of Security Staff Members:{security.sec_count} \nNo. of Cleaning Staff Members:{cleaning.c_cnt} \nNo. of Dispensary Staff Details:{dispensary.d_cnt} \nNo. of Drivers:{drivers.dr_cnt}")










































                  
