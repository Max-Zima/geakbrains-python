rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
text_file_2 = open('text_file_2.txt', 'w')
with open('text_file_1.txt') as text_file_1:
    line = text_file_1.readline()
    while line:
        i = line.split(' ')
        print(rus[i[0]] + '-' + i[2], file = text_file_2)
        line = text_file_1.readline()
text_file_2.close()
