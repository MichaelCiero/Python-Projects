import random
import string
basic_length = 6
complex_length = 12
very_complex_length = 16
string.ascii_letters
string.ascii_lowercase
string.ascii_uppercase
characters = string.ascii_letters + string.digits
pass_type_quest = input("How complex do you want your password to be? (1) Basic, (2) Complex, (3) Very Complex: ")
if int(pass_type_quest) == 1 or pass_type_quest == "Basic" or pass_type_quest == "(1) Basic":
    password = ''.join(random.choice(string.digits) for item in range(basic_length))
elif int(pass_type_quest) == 2 or pass_type_quest == "Complex" or pass_type_quest == "(2) Complex":
    password = ''.join(random.choice(characters) for item in range(complex_length))
elif int(pass_type_quest) == 3 or pass_type_quest == "Very Complex" or pass_type_quest == "(3) Very Complex":
    password = ''.join(random.choice(characters) for item in range(complex_length))

print("Password: " + password)
