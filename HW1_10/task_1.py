class Mentor:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


class Review:
    def rate_hw(self, student, course, grade):
        if isinstance(student, Mentor) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Reviewer(Mentor, Review):
    pass


class Student(Mentor, Review):
    def __init__(self, name, surname, gender):
        super.__init__(self, name, surname, gender)
        self.finished_courses = []


class Lecturer(Mentor):
    def __init__(self, name, surname, gender):
        super.__init__(self, name, surname, gender)



best_student = Mentor('Ruoy', 'Eman', 'man')
best_student.courses_in_progress += ['Python']

best_lecturer = Mentor('Some', 'Buddy', 'woman')
best_lecturer.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy', 'woman')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_lecturer, 'Python', 12)
cool_reviewer.rate_hw(best_lecturer, 'Python', 13)

cool_reviewer.rate_hw(best_student, 'Python', 5)
cool_reviewer.rate_hw(best_student, 'Python', 6)
cool_reviewer.rate_hw(best_student, 'Python', 78)

print(best_student.grades)
print(best_lecturer.grades)
print(best_lecturer)
print(cool_reviewer)
print(best_student)