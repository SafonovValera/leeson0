immutable_var = (1, True, 'wood', 0.72)
print(immutable_var)
immutable_var[0] = 2 # eror это неизменяемые данные!
mutable_list = [2, False, 'nut', 123.456]
print(mutable_list)
mutable_list[1] = True
mutable_list[0] = 1
print(mutable_list)