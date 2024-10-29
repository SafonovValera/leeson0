calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())


def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in [str.lower() for str in list_to_search]


print(string_info('Abrakadabra'))
print(string_info('Kamikaze'))
print(is_contains('Salt', ['Colt', 'bOLT', 'gOld']))
print(is_contains('Infection', ['Defect', 'politics', 'iNFECTION']))
print(calls)
