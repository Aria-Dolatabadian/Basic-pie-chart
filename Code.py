import matplotlib.pyplot as plt
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'CNL', 'TNL', 'RLK', 'RLP'
sizes = [15, 10, 45, 30]
explode = (0, 0.3, 0, 0)  # only "explode" the 2nd slice (i.e. 'TNL')
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
