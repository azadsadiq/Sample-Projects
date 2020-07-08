class Student:
  def __init__(self,name,year):
    self.name = name
    self.year = year
    self.grades = []

  def add_grade(self,grade):
    if type(grade) == Grade:
      self.grades.append(grade)
  def print_grades(self):
    for grade in self.grades:
      print (grade.score)


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)


class Grade:
  minimum_passing = 65
  def __init__(self,score):
    self.score = score

  def is_passing(self):
    if self.score >= self.minimum_passing:
      print("Pass")
    else:
      print ("Fail")

pi = Grade(100)
s = Grade(50)

pieter.add_grade(Grade(70))
pieter.add_grade(Grade(80))

s.is_passing()

pieter.print_grades()
