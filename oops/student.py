from oops.college import College

class Student(College):
    def __init__(self, cname, caddr, no_of_dept, rno, sname, sminor, sph,m1, m2, m3):
        super()._init_(cname, caddr, no_of_dept)
        self.rno = rno
        self.sname = sname
        self.sminor = sminor
        self.contact = sph
        self.marks1 = m1
        self.marks2 = m2
        self.marks3 = m3

    def calc_total(self):
        return self.marks1 + self.marks2 + self.marks3
    def calc_avg(self):
        return self.calc_total()/3