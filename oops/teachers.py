from oops.college import College
class Teachers(College):
    def __init__(self, cname, caddr, no_of_dept, eid, tname, tdept, tsalary):
        super()._init_(cname, caddr, no_of_dept)
        self.empid = eid
        self.tname = tname
        self.tdept = tdept
        self.tsalary = tsalary

    def display_teachers_info(self):
        print(f'empid: {self.empid}, Name: {self.tname}, Dept: {self.tdept}, Salary: {self.tsalary}')