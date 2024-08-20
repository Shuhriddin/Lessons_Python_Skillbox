# TODO здесь писать код
def validate_data(data):
    name, email, age = data.split()
    if len(data.split()) < 3:
        raise IndexError("НЕ присутствуют все три поля: IndexError")
    if not name.isalpha():
        raise NameError("Поле «Имя» содержит НЕ только буквы")
    if '@' not in email or '.' not in email:
        raise SyntaxError("Поле «Имейл» НЕ содержит @ и точку")
    age = int(age)
    if age < 10 or age > 99:
        raise ValueError("Поле «Возраст» НЕ представляет число от 10 до 99")


with open("registrations.txt", 'r', encoding='utf-8') as file, \
     open("registrations_good.log", 'w', encoding='utf-8') as good_file, \
     open("registrations_bad.log", 'w', encoding='utf-8') as bad_file:
    for line in file:
        line = line.strip()
        try:
            validate_data(line)
            good_file.write(line + '\n')
        except (ValueError, NameError, SyntaxError, IndexError) as e:
            bad_file.write(f"{line} - {e}\n")