class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        new_str = f'Имя: {self.name} \nФамилия: {self.surname}\n'
        return new_str


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average(self):
        listing = []
        av = 0
        for values in self.grades.values():
            for value in values:
                av += value
                listing.append(value)
                continue
        return int(av / len(listing))

    def course_print(self):
        return ', '.join(self.courses_in_progress)

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average()}\n'
                f'Курсы в процессе изучения: {self.course_print()}\n'
                )

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)


class Lecturer(Mentor, Student):
    def __init__(self, name, surname):
        super(Lecturer, self).__init__(name, surname)
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average()}\n'
                )


first_student = Student('Ivan', 'Ivanov', 'man')
first_student.courses_attached += ['Python']
first_student.courses_attached += ['Git']
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Git']

second_student = Student('Masha', 'Ivanova', 'woman')
second_student.courses_attached += ['Python']
second_student.courses_attached += ['Git']
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Git']

first_mentor = Reviewer('Karl', 'Sagan')
first_mentor.courses_attached += ['Python']
second_mentor = Reviewer('Robert', 'Sapolsky')
second_mentor.courses_attached += ['Git']

first_lecturer = Lecturer('Robert', 'Sheckley')
first_lecturer.courses_in_progress += ['Python']
second_lecturer = Lecturer('Daria', 'Donzova')
second_lecturer.courses_in_progress += ['Git']

students_rate = [{first_mentor.rate_hw(first_student, 'Python', 9)},
                 {first_mentor.rate_hw(first_student, 'Python', 10)},
                 {first_mentor.rate_hw(first_student, 'Python', 8)},
                 {second_mentor.rate_hw(second_student, 'Git', 6)},
                 {second_mentor.rate_hw(second_student, 'Git', 5)},
                 {second_mentor.rate_hw(second_student, 'Git', 4)}
                 ]
lecturer_rate = [{first_student.rate_lecturer(second_lecturer, 'Git', 5)},
                 {second_student.rate_lecturer(second_lecturer, 'Git', 10)},
                 {first_student.rate_lecturer(first_lecturer, 'Python', 10)},
                 {second_student.rate_lecturer(first_lecturer, 'Python', 8)}
                 ]

print(first_student)

