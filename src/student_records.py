def make_grades_table(arr):
    grades = {}
    for row in arr:
        if row[0] not in grades:
            grades[row[0]] = ['NA', 'NA']
        if row[1] == 'MS':
            grades[row[0]][0] = row[2]
        if row[1] == "HS":
            grades[row[0]][1] = row[2]
    return grades
