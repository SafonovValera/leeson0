grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sorted = sorted(students)
grades_0=sum(grades[0])/len(grades[0])
grades_1=sum(grades[1])/len(grades[1])
grades_2=sum(grades[2])/len(grades[2])
grades_3=sum(grades[3])/len(grades[3])
grades_4=sum(grades[4])/len(grades[4])
students_grades= dict([(students_sorted[0], grades_0), (students_sorted[1], grades_1), (students_sorted[2], grades_2), (students_sorted[3], grades_3), (students_sorted[4], grades_4)])
print(students_grades)