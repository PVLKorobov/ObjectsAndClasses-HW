class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lector(self, lecturer, cource, rating):
        if isinstance(lecturer, Lecturer) and rating >= 0 and rating <= 10 and cource in self.courses_in_progress and cource in lecturer.courses_attached:
            if cource in lecturer.ratings:
                lecturer.ratings[cource] += [rating]
            else:
                lecturer.ratings[cource] = [rating]
        else:
            print("Ошибка")

    def get_average_grade(self):
        grades_amount = 0
        sum = 0
        for cource_ratings in self.grades:
            grades_amount += len(self.grades[cource_ratings])
            for rating in self.grades[cource_ratings]:
                sum += rating
        return sum / grades_amount
    
    def __str__(self):
        return f" Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за домашние задания: {self.get_average_grade()} \n Курсы в процессе изучения: {', '.join(self.courses_in_progress)} \n Завершённые курсы: {', '.join(self.finished_courses)}"

    def __lt__(self, other_student):
       return self.get_average_grade() < other_student.get_average_grade()
    
    def __gt__(self, other_student):
       return self.get_average_grade() > other_student.get_average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.ratings = {}

    def get_average_rating(self):
        ratings_amount = 0
        sum = 0
        for cource_ratings in self.ratings:
            ratings_amount += len(self.ratings[cource_ratings])
            for rating in self.ratings[cource_ratings]:
                sum += rating
        return sum / ratings_amount
    
    def __lt__(self, other_lector):
       return self.get_average_rating() < other_lector.get_average_rating()
    
    def __gt__(self, other_lector):
       return self.get_average_rating() > other_lector.get_average_rating()        

    def __str__(self):
        return f" Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за лекции: {self.get_average_rating()}"

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            # return 'Ошибка' # Зачем этот return, если мы не делаем print этого метода? 
                              # Программа не выведет строку 'Ошибка' через return
            print('Ошибка')

    def __str__(self):
        return f"Имя: {self.name} \n Фамилия: {self.surname}"


# Функция подсчёта средней оценки лекторов по курсу cource
def lecturer_average_on_cource(cource, lecturer_list):
    overall_sum = 0
    overall_count = 0
    for lector in lecturer_list:
        if cource in lector.ratings:
            overall_count += len(lector.ratings[cource])
            for rating in lector.ratings[cource]:
                overall_sum += rating
    return overall_sum / overall_count

# Функция подсчёта среднего балла студентов по курсу cource
def student_average_on_cource(cource, student_list):
    overall_sum = 0
    overall_count = 0
    for student in student_list:
        if cource in student.grades:
            overall_count += len(student.grades[cource])
            for grade in student.grades[cource]:
                overall_sum += grade
    return overall_sum / overall_count


# Инициализация экземпляров класса Student
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Java', 'HTML']
best_student.finished_courses += ['Введение в программирование', 'Git']

second_best_student = Student('Leroy', 'Jenkins', 'attack_helicopter')
second_best_student.courses_in_progress += ['Введение в программирование', 'HTML', 'Git']
second_best_student.finished_courses += ['Python', 'Java']

# Инициализация экземпляров класса Lecturer
cool_lecturer = Lecturer('Elden', 'John')
cool_lecturer.courses_attached += ['Python', 'Git', 'HTML']

even_cooler_lecturer = Lecturer('Anton', 'Antonov')
even_cooler_lecturer.courses_attached += ['HTML', 'Введение в программирование', 'Java']

# Инициализация экземпляров класса Reviewer
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'Java']

cooler_reviewer = Reviewer('That', 'I used to know')
cooler_reviewer.courses_attached += ['HTML', 'Git', 'Введение в программирование']

# Выставление оценок студентам
cool_reviewer.rate_hw(best_student, 'Java', 7)
cool_reviewer.rate_hw(best_student, 'Python', 5)
cooler_reviewer.rate_hw(best_student, 'HTML', 10)

cooler_reviewer.rate_hw(second_best_student, 'Введение в программирование', 8)
cooler_reviewer.rate_hw(second_best_student, 'Git', 10)
cooler_reviewer.rate_hw(second_best_student, 'HTML', 6)

# Оценка лекторов студентами
best_student.rate_lector(cool_lecturer, 'Python', 8)
best_student.rate_lector(even_cooler_lecturer, 'Java', 10)

second_best_student.rate_lector(cool_lecturer, 'Git', 8)
second_best_student.rate_lector(even_cooler_lecturer, 'Введение в программирование', 10)
second_best_student.rate_lector(even_cooler_lecturer, 'HTML', 7)
best_student.rate_lector(cool_lecturer, 'HTML', 10)
best_student.rate_lector(cool_lecturer, 'HTML', 6)

# Сравнение студентов
if best_student > second_best_student:
    print(f"Оценки {best_student.name} {best_student.surname} выше чем у {second_best_student.name} {second_best_student.surname}")
else:
    print(f"Оценки {best_student.name} {best_student.surname} ниже чем у {second_best_student.name} {second_best_student.surname}")

# Сравнение лекторов
if cool_lecturer > even_cooler_lecturer:
    print(f"Рейтинг {cool_lecturer.name} {cool_lecturer.surname} лучше чем у {even_cooler_lecturer.name} {even_cooler_lecturer.surname}")
else:
    print(f"Рейтинг {cool_lecturer.name} {cool_lecturer.surname} хуже чем у {even_cooler_lecturer.name} {even_cooler_lecturer.surname}")

# Подсчёт среднего балла по всем студентам на одном курсе
student_list = [best_student, second_best_student]
print("Средний балл студентов на курсе HTML:" ,student_average_on_cource('HTML', student_list), '\n')

# Подсчёт средней оценки лекторов на одном курсе
lecturer_list = [cool_lecturer, even_cooler_lecturer]
print("Средний балл лекторов на курсе HTML:", lecturer_average_on_cource('HTML', lecturer_list), '\n')

# Вывод методов __str__ экземпляров классов

## Студентов
print(10 * '--')
print(best_student)
print()
print(second_best_student)

## Лекторов
print(10 * '--')
print(cool_lecturer)
print()
print(even_cooler_lecturer)

## Проверяющих
print(10 * '--')
print(cool_reviewer)
print()
print(cooler_reviewer)
