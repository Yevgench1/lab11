import json

students = [
    {"name": "Біг бой", "grade": 85},
    {"name": "Кібі бой", "grade": 90},
    {"name": "Ванька встанька", "grade": 70},
    {"name": "Артем Кузя", "grade": 95},
    {"name": "Дімка Бед бой", "grade": 80},
]

with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, ensure_ascii=False, indent=4)

with open("students.json", "r", encoding="utf-8") as file:
    students_data = json.load(file)

sorted_students = sorted(students_data, key=lambda x: x["grade"], reverse=True)

top_percentage = 0.4
num_scholarship_students = int(len(sorted_students) * top_percentage)

print("Студенти, які можуть претендувати на стипендію:")
for student in sorted_students[:num_scholarship_students]:
    print(student["name"])
