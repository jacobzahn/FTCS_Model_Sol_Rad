from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import os

# Loading CO2 Data
#---------------------------------------------------------------------------
sheet_title = 'LOESS Fit'
fn = os.path.join(os.path.dirname(__file__), 'ncomms14845-s3-2.xlsx')
data = pd.read_excel(fn, sheetname = sheet_title, header = 2)
data.columns = ['Age [Ma]','Atmospheric CO2 [ppm]','LW95','LW68','UP68','UP95']
t_intermediate = data['Age [Ma]']      # Time Array (size = 838)


# Loop to convert t values from "My before present" to My since Earth Formation"
#---------------------------------------------------------------------------
t = np.zeros(len(t_intermediate))
for ii in range(len(t_intermediate)):
    t[ii] = 4700 - t_intermediate[ii]
#---------------------------------------------------------------------------


alpha = 0.1           # Diffusion Coefficient for Heat Equation
nx = 20               # number of x's
nt = 838              # number of t's
L = 1                 # Unit domain length
t = 1                 # Unit time
dx = 0.05263          # L/(nx-1)
dt = 0.0011995        # t/(nt-1)
r = alpha*dt/(dx**2)  # Diffusion number
r2 = 1-2*r            # Diffusion number for matrix
pi = 3.14159          
lat = np.arange(0,pi/2,pi/40)
u = np.sin(lat)
S = (5-3*u**2)/4  # Initial Condition for Latitudinal Solar Radiation
S_initial = np.array([S]).T
S_old = S_initial

A = np.matrix([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [r, r2, r, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, r, r2, r, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, r, r2, r, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, r, r2, r, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, r, r2, r, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, r, r2, r, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, r, r2, r, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, r, r2, r, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, r, r2, r, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, r, r2, r, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, r, r2, r, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, r, r2, r, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, r, r2, r, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, r, r2, r, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, r, r2, r, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, r, r2, r, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, r, r2, r, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, r, r2, r],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]])

for ii in range(nt-1):
    
    A[0,0] = A[0,0]
    S_new = A*(S_old + (0.05/nt))  # Way to have boundary condition change due to increasing solar flux
    S_append = np.c_[S_initial,S_new]  # Adding to Solar Radiation Matrix
    S_initial = S_append
    S_old = S_new  # Moving forward one timestep
    
S_final = S_initial

plt.figure(3)
plt.plot(lat,S_final[:,[0]],'r--',label="initial")
plt.plot(lat,S_final[:,[250]],'g--',label="intermediate")                   
plt.plot(lat,S_final[:,[-1]],'b--',label="final")
plt.xlabel('Latitude [Rad]',fontsize=10)
plt.ylabel('Radiative Forcing [W/m2]',fontsize=10)
plt.title('Latitudinal Solar Radiation Evolution with Time',fontsize=16)
plt.grid(True)
plt.legend()
plt.ion()
plt.show()