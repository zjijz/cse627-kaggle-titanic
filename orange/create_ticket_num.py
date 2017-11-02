import re
import numpy as np
from Orange.data import *

out_data = []
for row in in_data:
    ticket = str(row.metas[1])
    num = ticket.split(' ')[-1]
    digits_only = re.compile(r'\D+')
    num = digits_only.sub('', num)
    out_data.append([float(num) if len(num) > 0 else None])
out_data = Table(Domain([ContinuousVariable('TicketNum')]), np.array(out_data))