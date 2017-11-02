titles = []

for row in in_data:
    name = row.metas[0]
    comma_ind = name.find(',')
    next_space_ind = name.find(' ', comma_ind + 2)
    title = name[comma_ind+1:next_space_ind].replace(' ', '').replace('.', '')
    
    if title not in titles:
        titles.append(title)
        
print(titles)