'''
Using conda imports things automatically
So conda install instead of pip install
'''

import requests
import pandas as pd
import numpy as np

response = requests.get("http://google.com")
print(response)

s = pd.Series([1, 3, 5, np, 6, 8])
print(s)
