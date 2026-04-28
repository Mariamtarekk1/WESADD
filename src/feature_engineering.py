#(Feature Engineering)
#Windowing + Aggregation
#The raw physiological signals were segmented into fixed-size windows (50 samples per window).Each window was then summarized using the mean value to reduce dimensionality and create meaningful features.
# 0, 6, 7 not important
#using 1 = baseline , 2 = stress , 3 = amusement , 4 = meditation
#كل label فيها كام sample
unique, counts = np.unique(labels, return_counts=True)

for u, c in zip(unique, counts):
    print(f"Label {u}: {c}")
  
