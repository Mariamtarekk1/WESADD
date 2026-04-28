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

# استخراج التسميات الصالحة فقط
valid_labels = [1, 2, 3, 4]
mask = np.isin(labels, valid_labels)

# تطبيق الاستخراج على إشارات الصدر
filtered_chest = {}
for key in chest.keys():
    filtered_chest[key] = chest[key][mask]
print("\nChest signals shapes:")

for key in chest.keys():
    print(key, chest[key].shape)

print("\nWrist signals shapes:")
for key in wrist.keys():
    print(key, wrist[key].shape)
import pandas as pd

df = pd.DataFrame({
    'ACC_x': filtered_chest['ACC'][:, 0],
    'ACC_y': filtered_chest['ACC'][:, 1],
    'ACC_z': filtered_chest['ACC'][:, 2],
    'ECG': filtered_chest['ECG'].flatten(),
    'EMG': filtered_chest['EMG'].flatten(),
    'EDA': filtered_chest['EDA'].flatten(),
    'Temp': filtered_chest['Temp'].flatten(),
    'Resp': filtered_chest['Resp'].flatten(),
    'label': filtered_labels.flatten()
})

print("Unique labels:", np.unique(labels))

