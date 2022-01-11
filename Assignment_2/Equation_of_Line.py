import numpy as np
import matplotlib.pyplot as plt
#from coeffs import *

import numpy as np
#from line.params import *
from params import *

#if using termux
import subprocess
import shlex
#end if


def dir_vec(A,B):
  return B-A

def norm_vec(A,B):
  return np.matmul(omat, dir_vec(A,B))

#Generate line points
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#line equation 

O=np.array([0,0])
C=np.array([-2,9])
M=C-O
N=np.matmul(omat,M)
B=N+C
A=2*C-B #from equation of directional vector C-A=B-C

#Generating all lines
x_OC = line_gen(O,C)
#x_BC = line_gen(B,C)
x_AB = line_gen(A,B)
#x_CA = line_gen(C,A)
#x_DE = line_gen(D,E)
#Plotting all lines
plt.plot(x_OC[0,:],x_OC[1,:],label='$OC$')
#plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
#plt.plot(x_DE[0,:],x_DE[1,:],label='$Perpendicular$')

plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 + 0.05), O[1] * (1 - 0.1) , 'O')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.05), C[1] * (1 - 0.1) , 'C')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1), A[1] * (1) , 'A')

#plt.plot(E[0], E[1], 'o')
#plt.text(E[0] * (1), E[1] * (1) , 'E')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
#plt.savefig('./figs/tri_sss.pdf')
#plt.savefig('./figs/tri_sss.png')
#subprocess.run(shlex.split("termux-open ./figs/tri_sss.pdf"))
#else
plt.show()
