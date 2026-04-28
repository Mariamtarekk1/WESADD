valid_labels = [1, 2, 3, 4] # 1=baseline, 2=stress, 3=amusement, 4=meditation

mask = np.isin(labels, valid_labels)

filtered_labels = labels[mask]
filtered_chest = {}

for key in chest.keys():
    filtered_chest[key] = chest[key][mask]
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
df_sample = (
    df.groupby('label', group_keys=False)
      .apply(lambda x: x.sample(n=min(len(x), 25000), random_state=42))
      .reset_index(drop=True)
)

df_sample = df_sample.sort_index()
