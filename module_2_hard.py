def password(number):
    if number < 3 or number > 20:
        print('Введите число от 3 до 20: ')
        print(password(int(input())))
    else:
        result = ''
        for i in range(1, number):
            for j in range(i + 1, number):
                if number % (i + j) == 0:
                    result += str(i) + str(j)
        return result


print('Введите число от 3 до 20: ')
print(password(int(input())))