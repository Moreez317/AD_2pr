import ssl
from sklearn.datasets import fetch_california_housing

ssl._create_default_https_context = ssl._create_unverified_context

data = fetch_california_housing(as_frame=True)

print(data)