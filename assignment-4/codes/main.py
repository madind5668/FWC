import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.insert(0,'/sdcard/fwc/matrices/CoordGeo')

m=10
n=5
theta=np.pi/3
k=1
l=4/3
j=2/3
A=np.array(([0,0]))
B=m*np.array(([np.cos(0),np.sin(0)]))
D=n*np.array(([np.cos(theta),np.sin(theta)]))
C=B+D

E=(k*A+B)/(k+1)
F=(k*B+C)/(k+1)
G=(k*C+D)/(k+1)
H=(k*D+A)/(k+1)
P=(l*E+G)/(l+1)
Q=(j*E+G)/(j+1)

def line_gen(X,Y):
  len =10
  dim = X.shape[0]
  x_XY = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = X + lam_1[i]*(Y-X)
    x_XY[:,i]= temp1.T
  return x_XY

x_AB=line_gen(A,B)
x_BC=line_gen(B,C)
x_CD=line_gen(C,D)
x_DA=line_gen(D,A)
x_EF=line_gen(E,F)
x_FG=line_gen(F,G)
x_GH=line_gen(G,H)
x_HE=line_gen(H,E)
x_EG=line_gen(E,G)
x_HP=line_gen(H,P)
x_FQ=line_gen(F,Q)

plt.plot(x_AB[0,:],x_AB[1,:],'-r')
plt.plot(x_BC[0,:],x_BC[1,:],'-r')
plt.plot(x_CD[0,:],x_CD[1,:],'-r')
plt.plot(x_DA[0,:],x_DA[1,:],'-r')
plt.plot(x_EF[0,:],x_EF[1,:],'-g')
plt.plot(x_FG[0,:],x_FG[1,:],'-g')
plt.plot(x_GH[0,:],x_GH[1,:],'-g')
plt.plot(x_HE[0,:],x_HE[1,:],'-g')
plt.plot(x_EG[0,:],x_EG[1,:],'-y')
plt.plot(x_HP[0,:],x_HP[1,:],'-b')
plt.plot(x_FQ[0,:],x_FQ[1,:],'-b')

tri_coords = np.vstack((A,B,C,D,E,F,G,H,P,Q)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','D','E','F','G','H','P','Q']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(-2,4), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axis('equal')
plt.show()
