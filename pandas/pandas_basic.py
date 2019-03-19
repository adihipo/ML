import numpy as np

import pandas as pd

panda_name = pd.Series(['Ronie', 'Mayo', 'Sting'])
panda_age = pd.Series([1, 5, 2])
db_panda = pd.DataFrame({'Name' : panda_name, 'Age' : panda_age})

db_panda['Is 1 year old and starts with R'] = (db_panda['Age'] == 1) & db_panda['Name'].apply(lambda name: name.startswith('R'))
print(db_panda.head())