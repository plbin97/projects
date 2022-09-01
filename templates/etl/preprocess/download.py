# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
from pathlib import Path
import urllib

# %%
from pyunpack import Archive

# %% tags=["parameters"]
upstream = None
product = None

# %%
url = 'https://archive.org/download/stackexchange/arduino.stackexchange.com.7z'
urllib.request.urlretrieve(url, product['zipped'])

Path(product['extracted']).mkdir(exist_ok=True)
Archive(product['zipped']).extractall(product['extracted'])
