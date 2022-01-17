"""
This is a code used for a geography lesson in my school where we were discussing the uses of
different mobility concepts and offers.
I wrote this code to display the approximate use of cars (Autos), busses and trains (ÖPNV) and 
the time walked in a week. None of the numbers are correct, they are just approximated values 
to showcase the percentual distribution of the usecases. The figures are made by using the 
mobilities used by four imaginary people p1, p2, p3 and p4.
"""

# ÖPNV = Busses and trains publicly available for use
# Auto = Car
# Zu Fuß = Walking

import matplotlib.pyplot as plt

"""Chart p1"""
# Pie Chart for the mobility of p1
labels_m = "ÖPNV", "zu Fuß"
sizes_m = [360, 300]

# create the pie chart figure
fig0, ax0 = plt.subplots()
# labelling the chart
ax0.pie(sizes_m, labels=labels_m, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax0.axis('equal') 
# setting the title of the chart
ax0.set_title("Mobilität p1")            # "mobility of p1"
"""End Chart p1"""

"""Chart p2"""
# Pie Chart for the mobility of p2
labels = "Auto", "ÖPNV", "zu Fuß"
sizes = [450, 30, 300]

# create the pie chart figure
fig1, ax1 = plt.subplots()
# labelling the chart
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
# setting the title of the chart
ax1.set_title("Mobilität p2")            # "mobility of p2"
"""End Chart p2"""

"""Chart p3"""
# Pie Chart for the mobility of p3
labels_s = "ÖPNV", "zu Fuß", "Auto"
sizes_s = [220, 180, 60]

# create the pie chart figure
fig3, ax3 = plt.subplots()
# labelling the chart
ax3.pie(sizes_s, labels=labels_s, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax3.axis('equal') 
# setting the title of the chart
ax3.set_title("Mobilität p3")            # "mobility of p3"
"""End Chart p3"""

"""Chart p4"""
# Pie Chart for the mobility of p4
labels_ich = "ÖPNV", "zu Fuß", "Auto"
sizes_ich = [180, 360, 60]

# create the pie chart figure
fig4, ax4 = plt.subplots()
# labelling the chart
ax4.pie(sizes_ich, labels=labels_ich, autopct='%1.1f%%', 
        shadow=True, startangle=90)
ax4.axis('equal')
# setting the title of the chart
ax4.set_title("Mobilität p4")            # "mobility of p4"
"""End Chart p4"""

plt.show()