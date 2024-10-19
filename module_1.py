grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sorted = sorted(students)
print(students_sorted)
a=len(grades[0])
b=sum(grades[0])
grades_0=b/a
print(grades_0)
a=len(grades[1])
b=sum(grades[1])
grades_1=b/a
print(grades_1)
a=len(grades[2])
b=sum(grades[2])
grades_2=b/a
print(grades_2)
a=len(grades[3])
b=sum(grades[3])
grades_3=b/a
print(grades_3)
a=len(grades[4])
b=sum(grades[4])
grades_4=b/a
print(grades_4)
students_grades= dict([(students_sorted[0], grades_0), (students_sorted[1], grades_1), (students_sorted[2], grades_2), (students_sorted[3], grades_3), (students_sorted[4], grades_4)])
print(students_grades)