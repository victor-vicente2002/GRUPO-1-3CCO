## Importing the libraries
import numpy as np
import pandas as pd

## Importing the dataset
dataset = pd.read_csv('data.csv')
x = dataset.iloc[:, :].values

# print(x)

## Taking care of the missing data
from sklearn.impute import SimpleImputer

### Replacing None values with 0
# imputer = SimpleImputer(missing_values=np.nan, strategy='constant', fill_value=0)

### Replacing None values with column mean
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

imputer.fit(x[:, :])
x[:, :] = imputer.transform(x[:, :])

## Show lines
print(x[:, :])

## Write data to csv file with no index, no header and %.2f float format
dataset.to_csv('data_clean.csv', index=False, header=False, float_format='%.2f')
