groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Рикардо",
        "surname": "Бичи",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [2, 3, 4]
    },
    {
        "name": "Аслбек",
        "surname": "Равшанов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 3, 3]
    }
]
import time
SB=float(input())

def print_students(students,float):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        if (sum(student["marks"])/len(student["marks"])>=SB):
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30),
              str(student["marks"]).ljust(20))
print_students(groupmates,SB)
time.sleep(10)
