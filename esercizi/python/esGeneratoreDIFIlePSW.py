import itertools

def generate_passwords(filename):
    with open(filename, 'w') as file:
        for combination in itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=3):
            file.write(''.join(combination) + '\n')

generate_passwords("passwords.txt")