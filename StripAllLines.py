
file_path = './count.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()
with open(file_path, 'w') as file2:
    for line in lines:
        line = line.strip()
        if(' ' in line):
            line_splitted = line.split(' ')
            second_part = line_splitted[1]
            print(second_part)
            file2.write(f'{second_part}\n')
