phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for digit in phone:
    output += digits_mapping.get(digit, "!") + " "
    #"if phone ch doesn't exist in digitsmapping, instead add '!' to output"
print(output)