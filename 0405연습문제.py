
class Student:
  def __init__(self, korean, english, math):
    self.korean = korean
    self.english = english
    self.math = math

def main():
  n = int(input("학생 수를 입력하세요: "))
  students = []
  for i in range(n):
    korean = int(input("국어 점수를 입력하세요: "))
    english = int(input("영어 점수를 입력하세요: "))
    math = int(input("수학 점수를 입력하세요: "))
    students.append(Student(korean, english, math))

  total_korean = 0
  total_english = 0
  total_math = 0
  for student in students:
    total_korean += student.korean
    total_english += student.english
    total_math += student.math

  average_korean = total_korean / n
  average_english = total_english / n
  average_math = total_math / n

  print("국어 평균점수:", average_korean)
  print("영어 평균점수:", average_english)
  print("수학 평균점수:", average_math)

if __name__ == "__main__":
  main()







