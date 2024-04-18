# SAMBA Copyright (C) 2024 - Closed source


import numpy as np
import shutil
#--------------------------
import plotly.offline as py
import plotly.graph_objects as go
#--------------------------------
import scipy.interpolate as interp
from scipy.interpolate import griddata
#-------------------------------------
import matplotlib as mpl
from matplotlib import cm
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.colors as mcolors


#===================================================
# Extraindo informações ============================
#===================================================
file0 = np.loadtxt('energy_scan.txt', dtype=str)
file0.shape
#--------------------
date_xy  = file0[:,0]
date_E   = np.array(file0[:,1],dtype=float)
E_min    = min(date_E)
E_max    = max(date_E)
line     = np.argmin(date_E)
delta_xy = date_xy[line]

#------------------------------
file = open('xy-scan.dat', "w")
#------------------------------
for i in range(len(date_xy)):
    temp = str(date_xy[i])
    temp = temp.replace('_', ' ')
    file.write(f'{temp} {date_E[i]} \n')
#-----------
file.close()
#-----------



#===================================================
# Plot 3D (.html) ==================================
#===================================================
n_d = 100
label1 = '\u0394' + 'A1'
label2 = '\u0394' + 'A2'
label3 = 'E(eV)'
#--------------------------------
file1 = np.loadtxt('xy-scan.dat') 
file1.shape
#-----------------
eixo1 = file1[:,0]
eixo2 = file1[:,1]
eixo3 = file1[:,2]
#---------------------------
# Create meshgrid for (x,y):
xi = np.linspace(min(eixo1), max(eixo1), n_d)
yi = np.linspace(min(eixo2), max(eixo2), n_d)
x_grid, y_grid = np.meshgrid(xi,yi)
# Grid data:
z_grid = griddata((eixo1,eixo2), eixo3, (x_grid,y_grid), method = 'cubic')
#-------------------------------------------------------------------------
fig = go.Figure()
fig.add_trace(go.Surface(x = x_grid, y = y_grid, z = z_grid, name = 'xy-scan', opacity = 0.8, showscale = False))
fig.update_layout(title = 'xy-scan', scene = dict(xaxis_title = label1, yaxis_title = label2, zaxis_title = label3, aspectmode = 'cube'), margin = dict(r = 20, b = 10, l = 10, t = 10))
fig.update_layout(xaxis_range=[min(eixo1), max(eixo1)])
fig.update_layout(yaxis_range=[min(eixo2), max(eixo2)])
fig.write_html('xy-scan_3D.html')



#===================================================
# Plot 2D (Mapa de cores) ==========================
#===================================================
n_contour = 100
#----------------------------------------------------------------
cmap_gray = (mpl.colors.ListedColormap(['darkgray', 'darkgray']))
#-----------------------
fig, ax = plt.subplots()
cp = plt.contourf(x_grid, y_grid, z_grid, levels = n_contour, cmap = "plasma", alpha = 1.0, antialiased = True)
cbar = fig.colorbar(cp, orientation = 'vertical', shrink = 1.0)
#-------------------
plt.title('xy-scan')
plt.xlabel('$\Delta{A_1}$')
plt.ylabel('$\Delta{A_2}$')
cbar.set_label('E(eV)')
#-----------------------
ax.set_box_aspect(1.0/1)
#-------------------------------------------------------------------------
plt.savefig('xy-scan.png', dpi = 600, bbox_inches='tight', pad_inches = 0)
# plt.savefig('xy-scan.pdf', dpi = 600, bbox_inches='tight', pad_inches = 0)
# plt.savefig('xy-scan.eps', dpi = 600, bbox_inches='tight', pad_inches = 0)
# plt.savefig('xy-scan.svg', dpi = 600, bbox_inches='tight', pad_inches = 0)



#=============================================================
# Obtendo a rede que minimiza a energia (via interpolação) ===
#=============================================================
line     = np.argmin(z_grid)
delta_A1 = x_grid[line]
delta_A2 = y_grid[line]

#==========================================================
# Obtendo os vetores de rede A1 e A2 da Heteroestrutura ===
#==========================================================
poscar = open('POSCAR.0', "r")
#-----------------------------
VTemp = poscar.readline()
VTemp = poscar.readline();  param = float(VTemp)
VTemp = poscar.readline().split();  A1x = float(VTemp[0])*param;  A1y = float(VTemp[1])*param;  A1z = float(VTemp[2])*param
VTemp = poscar.readline().split();  A2x = float(VTemp[0])*param;  A2y = float(VTemp[1])*param;  A2z = float(VTemp[2])*param
VTemp = poscar.readline().split();  A3x = float(VTemp[0])*param;  A3y = float(VTemp[1])*param;  A3z = float(VTemp[2])*param
#-------------
poscar.close()
#-------------

#================================================
# Gerando o arquivo POSCAR deslocado no plano ===
#================================================
displacement_X = (delta_A1*A1x) + (delta_A2*A2x)        
displacement_Y = (delta_A1*A1y) + (delta_A2*A2y)   
#-----------------------------------------------
poscar = open('POSCAR.0', "r")
poscar_new = open('POSCAR_temp', "w") 
#------------------------------------
VTemp = poscar.readline()
poscar_new.write(f'{VTemp}')
VTemp = VTemp.split()
nions1 = int(VTemp[1]);  nions2 = int(VTemp[2])
#----------------------------------------------
for k in range(7 + nions1):
    VTemp = poscar.readline()
    poscar_new.write(f'{VTemp}')
#-------------------------------
for k in range(nions2):
    VTemp = poscar.readline().split()
    poscar_new.write(f'{float(VTemp[0]) + displacement_X} {float(VTemp[1]) + displacement_Y} {VTemp[2]} \n')
#-----------------------------------------------------------------------------------------------------------
poscar.close()
poscar_new.close()
#-----------------

#===========================================================================
# Convertendo as coordenadas do arquivo POSCAR de cartesiano para direto ===
#===========================================================================
a = np.array([A1x, A1y, A1z])
b = np.array([A2x, A2y, A2z])
c = np.array([A3x, A3y, A3z])
T = np.linalg.inv(np.array([a, b, c]).T)  # Definindo a matriz de transformação
#------------------------------------------------------------------------------
poscar = open('POSCAR_temp', "r")
poscar_new = open('POSCAR', "w") 
#-------------------------------
for k in range(7):
    VTemp = poscar.readline()
    poscar_new.write(f'{VTemp}')
#------------------------
VTemp = poscar.readline()
poscar_new.write(f'Direct \n')

#----------------------------------------------------------------------------------------------------
# Convertendo as posições atomicas cartesianas de todos os átomos da Supercélula para a forma direta,
# e ajustando as posições dos átomos que se encontram fora da célula.
#--------------------------------------------------------------------
for k in range(nions1 + nions2):
    VTemp = poscar.readline().split()
    x = float(VTemp[0])
    y = float(VTemp[1])
    z = float(VTemp[2])    
    #----------------------
    r = np.array([x, y, z])        # Definindo o vetor posição cartesiano do átomo  
    #----------------------           
    f = np.dot(T, r)               # Calculando a correspondenre posição em coordenadas fracionárias
    for m in range(3):
        f = np.where(f < 0, f + 1, f)
        f = np.where(f > 1, f - 1, f)
    #-------------------------------- 
    for m in range(3):
        f[m] = round(f[m], 6)
        if (f[m] > 0.9999 or f[m] < 0.0001):
           f[m] = 0.0
    poscar_new.write(f'{f[0]} {f[1]} {f[2]} \n')
#-------------
poscar.close()
poscar_new.close()
#-----------------

os.remove('POSCAR_temp')
