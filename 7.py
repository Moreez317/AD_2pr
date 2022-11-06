import ssl
import pandas as pd
from sklearn.datasets import fetch_california_housing

ssl._create_default_https_context = ssl._create_unverified_context

df = fetch_california_housing(as_frame=True)

print(df.data.info())
