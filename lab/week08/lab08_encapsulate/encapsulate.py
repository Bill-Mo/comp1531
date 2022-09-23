'''
I added two functions getName and getAge to let it pass tests. Also I imported datetime from datetime to get correct year to make getAge working. I applied getAge in main function so that it can print out corret age.
'''
from datetime import datetime
class Student:
    def __init__(self, firstName, lastName, birth_year):
        self.name = firstName + " " + lastName
        self.birth_year = birth_year
        
    def getName(self):
        return self.name

    def getAge(self):
        return datetime.now().year - self.birth_year

if __name__ == '__main__':
    s = Student("Rob", "Everest", 1961)
    years_old = s.getAge()
    print(f"{s.name} is {years_old} old")
