import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('nox_domain_details_f_no_mut', sep=' ')
print(data)

main_id=[]#contains pdb id clusters which have same id till H level
main_cath=[]#contain cath id clusters which have same id till H level. Corresponding ids of the above

for i in range(len(data)):
    if data.iloc[i,0] in sum(main_id,[]):
        continue
    else:
        cath_i='.'.join(str(m) for m in data.loc[i][1:5])
        x=[]
        y=[]
        for j in range(len(data)):
            cath_j='.'.join(str(m) for m in data.loc[j][1:5])
            if cath_i == cath_j:
                x.append(data.loc[j][0])
                y.append('.'.join(str(m) for m in data.loc[j][1:]))
        main_id.append(x)
        main_cath.append(y)
        
non_singleton_pdbid=[i for i in main_id if len(i)!=1]
non_singleton_cath=[i for i in main_cath if len(i)!=1]
counts=[len(i) for i in non_singleton_cath]#number of members
labels=['.'.join(i[0].split('.')[0:4]) for i in non_singleton_cath]


#^^^^^^^^^^^^^Making dataframes for plotting

df=pd.DataFrame({"Name":labels,"Value":counts})#non_singleton clusters
df['Both']=[labels[i]+'---'+str(counts[i]) for i in range(len(counts))]#cath id+'---'+count

singleton_cluster_labels=['.'.join(i[0].split('.')[0:4]) for i in main_cath if len(i)==1]#clusters having only single member
df_single=pd.DataFrame({"Name":singleton_cluster_labels, "Value":[1 for i in range(len(singleton_cluster_labels))], "Both":[singleton_cluster_labels[i]+'---'+str(1) for i in range(len(singleton_cluster_labels))]})

df=df.append(df_single,ignore_index=True)#all clusters including single and non-sinlge. Total 235 clusters
#````````````````````````````````````````
#PLOTTING done for non-singleton clusters
#plt.figure(figsize=(20,10))

# plot polar axis
#ax = plt.subplot(111, polar=True)

# remove grid
#plt.axis('off')

# Set the coordinates limits
upperLimit = 100
lowerLimit = 10
#This means 0 values are set to a circular bar height of 10. Max height is 100. The df values are scaled accordingly

# Compute max and min in the dataset
max = df['Value'].max()

# Let's compute heights: they are a conversion of each item value in those new coordinates
# In our example, 0 in the dataset will be converted to the lowerLimit (10)
# The maximum will be converted to the upperLimit (100)
slope = (max - lowerLimit) / max
heights = slope * df.Value + lowerLimit

# Compute the width of each bar. In total we have 2*Pi = 360°
width = 2*np.pi / len(df.index)

# Compute the angle each bar is centered on:
indexes = list(range(1, len(df.index)+1))
angles = [element * width for element in indexes]
angles

"""
# Draw bars
bars = ax.bar(
    x=angles, 
    height=heights, 
    width=width, 
    bottom=lowerLimit,
    linewidth=2, 
    edgecolor="white")
"""

##---Include labels
# initialize the figure
plt.figure(figsize=(20,10))
ax = plt.subplot(111, polar=True)
plt.axis('off')

# Draw bars
bars = ax.bar(
    x=angles, 
    height=heights, 
    width=width, 
    bottom=lowerLimit,
    linewidth=1, 
    edgecolor="black",
    #color="#61a4b2",
    color=['red' if h>=17 else 'yellow' for h in heights],#if df['Value'] is >=10 then red. 17.7272 comes from slope and height calculations.
)

# little space between the bar and the label
labelPadding = 3

# Add labels
for bar, angle, height, label in zip(bars,angles, heights, df["Both"]):

    # Labels are rotated. Rotation must be specified in degrees :(
    rotation = np.rad2deg(angle)

    # Flip some labels upside down
    alignment = ""
    if angle >= np.pi/2 and angle < 3*np.pi/2:
        alignment = "right"
        rotation = rotation + 180
    else: 
        alignment = "left"

    # Finally add the labels
    ax.text(
        size='xx-small',
        x=angle, 
        y=lowerLimit + bar.get_height() + labelPadding, 
        s=label, 
        ha=alignment, 
        va='center', 
        rotation=rotation, 
        rotation_mode="anchor") 
plt.show()
#plt.savefig('trial.png',format='png',dpi=1300)

#df.to_csv('cluster_labels',index=False,columns=['Name'])#only non-singleton clusters

#with open('single_cluster_labels','w') as filehandle:
#    filehandle.writelines('\n'.join(singleton_cluster_labels))
    