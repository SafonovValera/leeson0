first = int(input('Inter the first number:'))
second = int(input('Inter the second number:'))
third = int(input('Inter the third number:'))
if first == second and second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else: print(0)