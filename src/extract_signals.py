import os
os.listdir('/content/WESAD_data')
os.listdir('/content/WESAD_data/WESAD')
os.listdir('/content/WESAD_data/WESAD/S2')
import os

print(os.listdir('/content'))
import pickle

file_path = '/content/WESAD_data/WESAD/S2/S2.pkl'

with open(file_path, 'rb') as f:
    data = pickle.load(f, encoding='latin1')
  data.keys()
data['signal'].keys()
data['signal'] ['chest'].keys()
data['signal'] ['wrist'].keys()

signals = data['signal']
chest = signals['chest']
labels = data['label']
wrist = signals['wrist']
subject = data['subject']
print("Subject:", subject)
print("Labels shape:", labels.shape)

print("\nChest signals shapes:")
for key in chest.keys():
    print(key, chest[key].shape)

print("\nWrist signals shapes:")
for key in wrist.keys():
    print(key, wrist[key].shape)
  import numpy as np

print("Unique labels:", np.unique(labels))

