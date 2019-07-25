#!/usr/bin/python3

import csv
import numpy as np
import matplotlib.pyplot as plt


def parsecsvdata():
    '''retrns a list. [0] is lan and [1] wan data'''
    summary = [] # list that will contain [(LAN), (WAN)]

    #open csv data
    with open("/home/student/mikerauer/graphing/2018summary.csv",\
            "r") as downtime:
        # parse csv data with csv.reader
        downdata = csv.reader(downtime, delimiter=",")
        for row in downdata:
            rowdat = (row[0], row[1], row[2], row[3])
            summary.append(rowdat) # add dict to list
    return summary

def main():
    N = 4
    summary = parsecsvdata() # grabs data
    localnetMeans = summary[0]  #LAN Length of outage (mins)
    wanMeans = summary[1]  #WAN length of outage (min)
    
    ind = np.arange(N)  # the x locations for the group
    # the width of the cars: can also be len(x) sequence
    width = 0.35
    
    #describe where to display p1
    p1 = plt.bar(ind, localnetMeans, width)
    #stack p2 on top of p1
    p2 = plt.bar(ind, wanMeans, width, bottom=localnetMeans)
    
    #Describe the table metadata
    plt.ylabel("Length of Outage (mins)")
    plt.title("2018 Network Summary")
    plt.xticks(ind, ("Q1", "Q2", "Q3", "Q4"))
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ("LAN", "WAN"))

#display graph
#plt.show()

#Save the graph
plt.savefig\
        ("/home/student/mikerauer/graphing/2018summary2.png")
print("graph created")

main()
