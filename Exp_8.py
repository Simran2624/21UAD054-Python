
import pandas as pd

import numpy as np

df = pd.read_excel("customer.xlsx")

#Get the data types of the given excel data
df.dtypes

#Display the last ten rows
df.tail(10)

#Insert a column in the sixth position of the said excel sheet and fill it with NaN values
df.insert(5, 'NewColumn', np.nan)
df.head(5)





