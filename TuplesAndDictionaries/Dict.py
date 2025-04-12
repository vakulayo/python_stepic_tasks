def code_number(num):
    return ' '.join({'0': "zero",
                     '1': "one",
                     '2': "two",
                     '3': "three",
                     '4': "four",
                     '5': "five",
                     '6': "six",
                     '7': "seven",
                     '8': "eight",
                     '9': "nine"}.get(digit) for digit in str(num))


print(code_number(230))  # == "two three zero"
