def print_greetings(language, times):
    """
    Print greetings based on the specified language and number of times.

    :param language: Language for greetings (English, Chinese, Russian)
    :param times: Number of times to print the greeting
    """
    while language.lower() not in ['english', 'chinese', 'russian']:
        language = input('Invalid input! Please choose language from English, Chinese, or Russian: ')

    greetings = {
        'english': 'hello',
        'chinese': 'ni hao',
        'russian': 'privet'
    }

    for _ in range(times):
        print(greetings[language.lower()])


if __name__ == '__main__':
    language = input('Please choose language from English, Chinese, or Russian: ')
    times = int(input('Please type the number of times to repeat the greeting: '))
    print_greetings(language, times)

