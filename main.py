from logging import raiseExceptions


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
            return 'Ошибка' # Зачем этот return, если мы не делаем print этого метода? 
                            # Программа не выведет строку 'Ошибка'
    def __str__(self):
        return f" Имя: {self.name} \n Фамилия: {self.surname}"


 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_lecturer = Lecturer('Elden', 'John')
cool_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Java']
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

best_student.rate_lector(cool_lecturer, 'Python', 8)
best_student.rate_lector(cool_lecturer, 'Python', 10)
 
# print(best_student.grades)
# print(best_student.courses_in_progress)
# print(cool_lecturer.courses_attached)
print(cool_lecturer.ratings)
# print(cool_reviewer.courses_attached)

# print(cool_reviewer)
print(cool_lecturer)
print()