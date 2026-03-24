import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# 按列求和（默认axis=0）
print(df.sum(axis=0))
# A     6
# B    15
# C    24
# dtype: int64

# 按行求和（axis=1）
print(df.sum(axis=1))
# 0    12
# 1    15
# 2    18
# dtype: int64

def row_func(x):
    return x.mean()

print(df.apply(row_func, axis=1))