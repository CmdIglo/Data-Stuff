"""
An easier way to produce the plots, created in mobility.py in this repo.
See mobility.py for further explaination of this project.
"""

import matplotlib.pyplot as plt

labels_m = "ÖPNV", "zu Fuß"
sizes_m = [360, 300]

labels = "Auto", "ÖPNV", "zu Fuß"
sizes = [450, 30, 300]

labels_s = "ÖPNV", "zu Fuß", "Auto"
sizes_s = [220, 180, 60]

labels_ich = "ÖPNV", "zu Fuß", "Auto"
sizes_ich = [180, 360, 60]

fig, axs = plt.subplots(2, 2)

axs[0,0].pie(sizes_m, labels=labels_m, autopct='%1.1f%%',
        shadow=True, startangle=90)
axs[0,0].set_title("Mobility p1")        

axs[1,0].pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
axs[1,0].set_title("Mobility p2")

axs[0,1].pie(sizes_s, labels=labels_s, autopct='%1.1f%%',
        shadow=True, startangle=90)
axs[0,1].set_title("Mobility p3")

axs[1,1].pie(sizes_ich, labels=labels_ich, autopct='%1.1f%%', 
        shadow=True, startangle=90)
axs[1,1].set_title("Mobility p4")

plt.show()