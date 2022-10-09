import sys                                                    #for path to external scripts
sys.path.insert(0,'/home/student/CoordGeo')         #path to my scripts


#import module
import random as rd
import subprocess
import shlex
import numpy as np
import matplotlib.pyplot as plt

# initialize x and y coordinates
x1 = [-2,4,3,-3,-2]
y1 = [ -1,0,3,2,-1]
pts1=['D','C','B','A']
c=['ro','bo','ko','go'] 
plt.scatter(x1,y1)

plt.plot(x1,y1)
vert_labels = ['A(-2,-1)','B(4,0)','C(3,3)','D(-3,2)']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (x1[i], y1[i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(2,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid() # minor
plt.axis([-8,8,-8,10])
plt.show()
    
#to check if given points are vertex of parallelogram


A=np.array([-2,-1])
B=np.array([4,0])
C=np.array([3,3])
D=np.array([-3,2])

P=B-A #vector p
Q=C-D #vector q
R=B-C
S=A-D

normp=np.linalg.norm(P)
normq=np.linalg.norm(Q)
normr=np.linalg.norm(R)
norms=np.linalg.norm(S)

PcrossQ= np.cross(P,Q)
RcrossS= np.cross(R,S)

if PcrossQ==0 and RcrossS==0 and normp==normq and normr==norms:
  print('since,the slope of opposite line are parallel the points form the vertices of the parallelogram');
else:
  print('the points are not the vertices of parallelogram');
    
 #to show plot on termux
 plt.savefig('/sdcard/Download/codes/Line_assignment.pdf)
 subprocess.run(shlex.split("termux-open '/sdcard/Download/codes/Line_assignment.pdf' "))

