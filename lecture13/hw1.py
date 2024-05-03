class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._grades = None
        self._avg = None
        self.subjects = ['Kor', 'Eng', 'Math']

    @property
    def grades(self):
        return self._grades

    @grades.setter
    def grades(self, value: dict):
        scores = value.values()
        if self._grades is not None:
            raise ValueError("Grades should be entered only one time!")

        for score in scores:
            if score < 0 or 100 < score:
                raise ValueError("Grade must be between 0 and 100")
            elif type(score) is not int:
                raise ValueError("Grade must be an integer")
        
        self._grades = value
