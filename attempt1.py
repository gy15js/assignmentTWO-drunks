#import random
import matplotlib.pyplot
import csv


num_of_drunks = 25
num_of_iterations = 100

drunks = []
environment = []

f = open('drunkplan.txt', 'r')
#r is for read only
reader = csv.reader (f)
#imports csv reader module for importing raster files etc.
for row in reader:
    rowlist = []
    environment.append(rowlist)
    for value in row:
        rowlist.append(int(value))
#int was added to prevent the error regarding image
#need to ensure this is created before the agents list otherwise agents are 
#using an empty list
f.close()


for j in range(num_of_iterations):
    for i in range(num_of_drunks):
        drunks.append ([70,210])
        #drunks.append ([random.randint(0,299),random.randint(0,299)])
        '''or [70,75] or [210,75] or [210,210]''' #tried to add this in so they start at one of 4 pubs

#for j in range(num_of_iterations):
#    for i in range(num_of_drunks):
#
#        if random.random() < 0.5:
#            drunks[i][0] = (drunks[i][0] + 1) % 300
#        else:
#            drunks[i][0] = (drunks[i][0] - 1) % 300
#
#
 #       if random.random() < 0.5:
  #          drunks[i][1] = (drunks[i][1] + 1) % 300
   #     else:
    #        drunks[i][1] = (drunks[i][1] - 1) % 300

#print (agents)

#print (max(agents, key=operator.itemgetter(1)))

matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.imshow(environment)

matplotlib.pyplot.ylim(0, 299)
matplotlib.pyplot.xlim(0, 299)
for i in range (num_of_drunks):
    matplotlib.pyplot.scatter(drunks[i][1],drunks[i][0])
matplotlib.pyplot.show()


