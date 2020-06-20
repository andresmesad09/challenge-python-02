# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')
#Incluyo minusculas, mayusculas y digitos.
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits

def generate_password():
    
    #Genero un entero de 2 a 4, para que la contraseña tome de a 2 a max 4  items de cada lista
    items = random.randint(2,4)
    #Genero la contraseña vacía para luego añadirle los caracteres
    password = ""

    #Creo una lista para cada uno (min, mayus, digits, symbols)
    aleatoriosMinus = random.sample(lower, items)
    aleatoriosMayus = random.sample(upper, items)
    aleatoriosSymbols = random.sample(SYMBOLS, items)
    aleatoriosDigits = random.sample(digits, items)
    #Creo una lista que contenga las cuatro listas anteriores
    passwordlist = aleatoriosMinus + aleatoriosMayus + aleatoriosSymbols + aleatoriosDigits

    #Inserto la lista como texto en la password vacía que tenia anteriormente
    password = password.join(passwordlist)

    return password

def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
