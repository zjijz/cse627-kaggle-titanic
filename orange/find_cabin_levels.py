levels = []

for row in in_data:
    cabin = row.metas[2]
    print(row)
    print(str(cabin))
    if str(cabin) != ' ' and str(cabin) != '?' and str(cabin) != 'nan' and str(cabin) != '':
        level = str(cabin)[0]
        if level not in levels:
            levels.append(level)

print(levels)