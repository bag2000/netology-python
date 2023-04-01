
best_student = [0, 1]
cool_lecturer = [0, 1]
coll_reviewer = [0, 1]


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def avg_grades(self):
        sum_grades = 0
        count_grades = 0
        for value in self.grades.values():
            for grade in value:
                count_grades += 1
                sum_grades += grade
        return str(round(sum_grades / count_grades, 1))

    def __str__(self):
        name = self.name
        surname = self.surname
        in_progress = ', '.join(self.courses_in_progress)
        finished = ', '.join(self.finished_courses)
        return f'Имя: {name}\n' \
               f'Фамилия: {surname}\n' \
               f'Средняя оценка за лекции: {self.avg_grades()}\n' \
               f'Курсы в процессе изучения: {in_progress}\n' \
               f'Завершенные курсы: {finished}'

    def __lt__(self, lecturer):
        if not isinstance(lecturer, Lecturer):
            print('Not a Student')
            return
        return self.avg_grades() < lecturer.avg_grades()

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_grades(self):
        sum_grades = 0
        count_grades = 0
        for value in self.grades.values():
            for grade in value:
                count_grades += 1
                sum_grades += grade
        return str(round(sum_grades / count_grades, 1))

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.avg_grades()}'

    def __lt__(self, student):
        if not isinstance(student, Student):
            print('Not a Student')
            return
        return self.avg_grades() < student.avg_grades()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def avg_lecturers_one_course(course):
    sum_grades = 0
    count_grades = 0
    for lecturer in cool_lecturer:
        for key, val in lecturer.grades.items():
            if key == course:
                sum_grades += sum(val)
                count_grades += len(val)
    return round(sum_grades / count_grades, 1)


def avg_students_one_course(course):
    sum_grades = 0
    count_grades = 0
    for student in best_student:
        for key, val in student.grades.items():
            if key == course:
                sum_grades += sum(val)
                count_grades += len(val)
    return round(sum_grades / count_grades, 1)


best_student[0] = Student('Irina', 'Demidova', 'female')
best_student[0].courses_in_progress += ['Python', 'Windows']
best_student[0].finished_courses += ['Git']

best_student[1] = Student('Polyakov', 'Roman', 'male')
best_student[1].courses_in_progress += ['Python', 'Linux']
best_student[1].finished_courses += ['Git']

cool_lecturer[0] = Lecturer('Igor', 'Viktorovich')
cool_lecturer[0].courses_attached += ['Python']

cool_lecturer[1] = Lecturer('Grigory', 'Ivanovich')
cool_lecturer[1].courses_attached += ['Windows', 'Linux']

coll_reviewer[0] = Reviewer('Ivan', 'Ivanov')
coll_reviewer[0].courses_attached += ['Python']

coll_reviewer[1] = Reviewer('Ivan', 'Ivanov')
coll_reviewer[1].courses_attached += ['Windows', 'Linux']

best_student[0].rate_lec(cool_lecturer[0], 'Python', 10)
best_student[0].rate_lec(cool_lecturer[1], 'Windows', 8)

best_student[1].rate_lec(cool_lecturer[0], 'Python', 8)
best_student[1].rate_lec(cool_lecturer[1], 'Linux', 10)

coll_reviewer[0].rate_hw(best_student[0], 'Python', 10)
coll_reviewer[0].rate_hw(best_student[0], 'Python', 7)
coll_reviewer[0].rate_hw(best_student[1], 'Python', 9)
coll_reviewer[0].rate_hw(best_student[1], 'Python', 10)

coll_reviewer[1].rate_hw(best_student[0], 'Windows', 10)
coll_reviewer[1].rate_hw(best_student[0], 'Windows', 8)
coll_reviewer[1].rate_hw(best_student[1], 'Linux', 9)
coll_reviewer[1].rate_hw(best_student[1], 'Linux', 10)


print(coll_reviewer[0])
print()
print(cool_lecturer[1])
print()
print(best_student[0])
print()
print(best_student[0] < cool_lecturer[1])
print()
print(avg_students_one_course('Python'))
print(avg_lecturers_one_course('Python'))
