from http.cookiejar import uppercase_escaped_char

calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(word):
    result = (len(word), word.upper(), word.lower())
    count_calls()
    return result

def is_contains(string, list_to_search):
    for i in range(len(list_to_search)):
        if string.lower() == list_to_search[i].lower():
            result = True
            break
        else:
            result = False
            continue
    count_calls()
    return result

print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)