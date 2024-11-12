import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd

# Input parameters
file_path = 'path/file_name.csv'
out_path = 'path/plot_output.pdf'

# data_import
df = pd.read_csv(file_path)

# Extract rows with fixed values in the Well Position column.(example: A6, B8, C6, D8)
target_data = df[df['Well Position'].isin(['A6', 'B8', 'C6', 'D8'])]

# Split the data frame based on the values in the first column (Well Position column)
grouped = target_data.groupby('Well Position')

# data extract(example: A6, B8, C6, D8)
group1 = grouped.get_group('A6')
group2 = grouped.get_group('B8')
group3 = grouped.get_group('C6')
group4 = grouped.get_group('D8')

# make data
x1 = group1['Temperature']
y1 = group1['Derivative']
x2 = group2['Temperature']
y2 = group2['Derivative']
x3 = group3['Temperature']
y3 = group3['Derivative']
x4 = group4['Temperature']
y4 = group4['Derivative']

# create figure and axes
fig, ax = plt.subplots(figsize=(4, 3))

#-------------
# Set global font style
mpl.rcParams['font.family'] = 'Arial'  # Set the font to Arial.
mpl.rcParams['font.size'] = 12  # Set the font size to 12.

# Set the range of the horizontal axis.
plt.xlim(25,90)

# Set new horizontal axis scale.
new_xticks = [25, 45, 65, 85]  # New horizontal axis scale position
plt.xticks(new_xticks)

# hide spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Set the thickness of the coordinate axis
plt.gca().spines['bottom'].set_linewidth(1.5)
plt.gca().spines['left'].set_linewidth(1.5)

# Set the thickness of the axis scale.
plt.gca().yaxis.set_tick_params(width=1.5)
plt.gca().xaxis.set_tick_params(width=1.5)

#-------------
# plot the data on the same axes
ax.plot(x1, y1, label='0µM', linewidth=1.5, color='#FD059C')  # Set the line thickness to 1.5.
ax.plot(x2, y2, label='25µM', linewidth=1.5, color='#52429F')  # Set the line thickness to 1.5.
ax.plot(x3, y3, label='100µM', linewidth=1.5, color='#FFD150')  # Set the line thickness to 1.5.
ax.plot(x4, y4, label='250µM', linewidth=1.5, color='#916D99')  # Set the line thickness to 1.5.

# add labels and legend
ax.set_xlabel('Temperature (°C)')
ax.set_ylabel('-d(RFU)/d(T)')
ax.set_title('TITLE')
ax.legend()

#-------------
# save the plot as a PDF file
plt.savefig(out_path, format='pdf')

plt.show()