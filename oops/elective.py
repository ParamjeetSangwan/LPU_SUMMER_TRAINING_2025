# Multilevel Inheritance

from oops.student import Student


class Elective(Student):
    def __init__(self, cname, caddr, no_of_dept, rno, sname, sminor, sph, m1, m2, m3,e1, e2):
        super()._init_(cname, caddr, no_of_dept, rno, sname, sminor, sph, m1, m2, m3)
        self.elec1=e1
        self.elec2=e2

    def calc_total(self):
        return self.marks1 + self.marks2 + self.marks3 + self.elec1 + self.elec2
    def calc_avg(self):
        return self.calc_total()/5