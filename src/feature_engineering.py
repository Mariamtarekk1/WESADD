#(Feature Engineering)
#Windowing + Aggregation
#The raw physiological signals were segmented into fixed-size windows (50 samples per window).Each window was then summarized using the mean value to reduce dimensionality and create meaningful features.
# 0, 6, 7 not important
#using 1 = baseline , 2 = stress , 3 = amusement , 4 = meditation
#كل label فيها كام sample
unique, counts = np.unique(labels, return_counts=True)

for u, c in zip(unique, counts):
    print(f"Label {u}: {c}")
  
df_sample = (
    df.groupby('label', group_keys=False)
      .apply(lambda x: x.sample(n=min(len(x), 25000), random_state=42))
      .reset_index(drop=True)
)

df_sample = df_sample.sort_index()
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
