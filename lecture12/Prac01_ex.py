class Student():
    name = 'James'
    kor = 90
    eng = 100
    math = 100

    def getAvg(self):
        average = (self.kor + self.eng + self.math) / 3

        return average
    pass


student = Student()
print(f"{student.name}'s scores")
print(f"Kor: {student.kor}")
print(f"English: {student.eng}")
print(f"Math: {student.math}")
print(f"Average: {student.getAvg()} ")
