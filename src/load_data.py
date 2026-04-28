mport pandas as pd
import os
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
### Loading Dataset

#The WESAD dataset consists of multiple subjects, each containing physiological signals and labels.
### Loading Data
from google.colab import drive
drive.mount('/content/drive')
import zipfile
import os

zip_path = '/content/drive/MyDrive/data WESAD.zip'
extract_path = '/content/WESAD_data'

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)
