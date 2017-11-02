import numpy as np
from Orange.data import *

titles = ['Mr', 'Mrs', 'Miss', 'Master', 'Royal (M)', 'Royal (F)']
out_data = []
for row in in_data:
    name = row.metas[0]
    comma_ind = name.find(',')
    dot_ind = name.find('.', comma_ind + 2)
    title = name[comma_ind + 1:dot_ind].split(' ')[-1]
    if title in ['Mr', 'Rev', 'Major', 'Col', 'Capt']:
        title = 0
    elif title in ['Mrs', 'Mme']:
        title = 1
    elif title in ['Miss', 'Ms', 'Mlle']:
        title = 2
    elif title in ['Master']:
        title = 3
    elif title in ['Don', 'Sir', 'Jonkheer']:
        title = 4
    elif title in ['Lady', 'Countess']:
        title = 5
    else:
        if row[2] == 'female':
            title = 1
        else:
            title = 0
    out_data.append([title])
out_data = Table(Domain([DiscreteVariable('Title', values=titles)]), np.array(out_data))