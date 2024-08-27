calls = 0


def count_calls(call):
    global calls
    calls += call
    return calls


def string_info(string):
    a = [len(string), string.upper(), string.lower()]  # переменная а - локальная, видна только в string_info.
    count_calls(1)
    return a


def is_contains(string, list_to_search):
    string.lower()
    a = []         # переменная а - локальная, видна только в is_contains.
    count_calls(1)
    for i in list_to_search:
        a.append(i.lower())
    return string.lower() in a


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cucle', ['recucle', 'cuclic']))
print(calls)
