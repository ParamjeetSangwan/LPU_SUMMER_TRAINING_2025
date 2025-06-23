# Single Inheritance
from oops.elective import Elective
from oops.teachers import Teachers

cname = input('Enter your College Name: ')
caddr = input('Enter your College Address: ')
dept = input('Enter your Department: ')
rollno = int(input('Enter your Roll No: '))
sname = input('Enter Student Name: ')
sminor = input('Enter Student Minor: ')
sphone = int(input('Enter Student Phone Number: '))
m1 = int(input('Marks1: '))
m2 = int(input('Marks2: '))
m3 = int(input('Marks3: '))
e1 = int(input('Elective1: '))
e2 = int(input('Elective2: '))

empid = input('Enter your Teacher ID: ')
tname = input('Enter your Teacher Name: ')
tdept = input('Enter your Teacher Department: ')
tsalary = int(input('Enter your Teacher Salary: '))

'''stud = Student(cname=cname, caddr=caddr, no_of_dept=dept, rno=rollno, sname=sname, sminor=sminor,
            sph=sphone, m1=m1, m2=m2, m3=m3)
'''
stud = Elective(cname=cname, caddr=caddr, no_of_dept=dept, rno=rollno, sname=sname, sminor=sminor,
            sph=sphone, m1=m1, m2=m2, m3=m3, e1=e1, e2=e2)

stud.display_clg_info()
stud.calc_total()
stud.calc_avg()

print(f'Stu Rno: {stud.rno} \n Name: {stud.sname} \n Department: {stud.sminor} \n'
      f' Total Marks: {stud.calc_total()}\n'
      f' Avg Marks: {stud.calc_avg():.2f}')

teacher = Teachers(caddr=caddr, no_of_dept=dept, eid=empid, tname=tname, tdept=tdept, tsalary=tsalary)
teacher.display_teachers_info()



