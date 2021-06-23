subj = {}
file_6 = open('file_6.txt', 'r')
line = file_6.readline()
while line:
    summa = 0
    row = line.split()
    subject = row[0]
    for i in range(1, len(row)):
        digit = ''
        for j in range(len(row[i])):
            if (row[i][j] >= '0') and (row[i][j] <= '9'):
                digit += str(row[i][j])
        summa += int(digit)
    subj[subject] = summa
    line = file_6.readline()
print(f'Общее количество часов по предмету: \n {subj}')
