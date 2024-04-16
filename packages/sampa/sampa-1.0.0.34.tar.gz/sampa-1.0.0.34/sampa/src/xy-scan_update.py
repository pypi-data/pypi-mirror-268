# SAMBA Copyright (C) 2024 - Closed source


import numpy as np
import shutil
#--------------------------
import plotly.offline as py
import plotly.graph_objects as go
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



file0 = np.loadtxt('energy_scan.txt', dtype=str)
file0.shape

date_xy  = file0[:,0]
date_E   = file0[:,1]
E_min    = min(date_E)
E_max    = max(date_E)
line     = np.argmin(date_E)
delta_xy = date_xy[line]

#===================================================
shutil.copyfile(str(delta_xy) + '/POSCAR', 'POSCAR')
#===================================================



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
label1 = 'A1'
label2 = 'A2'
label3 = 'E(eV)'

file1 = np.loadtxt('xy-scan.dat') 
file1.shape

eixo1 = file1[:,0]
eixo2 = file1[:,1]
eixo3 = file1[:,2]

# Create meshgrid for (x,y):
xi = np.linspace(min(eixo1), max(eixo1), n_d)
yi = np.linspace(min(eixo2), max(eixo2), n_d)
x_grid, y_grid = np.meshgrid(xi,yi)

# Grid data:
z_grid = griddata((eixo1,eixo2), eixo3, (x_grid,y_grid), method = 'cubic')

fig = go.Figure()
fig.add_trace(go.Surface(x = x_grid, y = y_grid, z = z_grid, name = 'xy-scan', opacity = 0.8, showscale = False))
fig.update_layout(title = 'xy-scan', scene = dict(xaxis_title = label1, yaxis_title = label2, zaxis_title = label3, aspectmode = 'cube'), margin = dict(r = 20, b = 10, l = 10, t = 10))
fig.update_layout(xaxis_range=[min(eixo1), max(eixo1)])
fig.update_layout(yaxis_range=[min(eixo2), max(eixo2)])
fig.write_html('Plot_3d.html')



#===================================================
# Plot 2D (Mapa de cores) ==========================
#===================================================

n_contour = 100
n_contour_energ = 250

cmap_gray = (mpl.colors.ListedColormap(['darkgray', 'darkgray']))

fig, ax = plt.subplots()
cp = plt.contourf(x_grid, y_grid, z_grid, levels = n_contour, cmap = "plasma", alpha = 1.0, antialiased = True)
cbar = fig.colorbar(cp, orientation = 'vertical', shrink = 1.0)


# levels_e = [0.0]*n_contour_energ
# for n in range(n_contour_energ):
#     level = E_min + ((E_max - E_min)/(n_contour_energ - 1))*(n)
#     levels_e[n] = level
# cs = plt.contour(x_grid, y_grid, z_grid, levels_e, linestyles = '-', cmap = cmap_gray, linewidths = 0.5, alpha = 1.0, antialiased = True)


plt.title('xy-scan')
plt.xlabel('A1')
plt.ylabel('A2')

ax.set_box_aspect(1.0/1)

plt.savefig('xy-scan.png', dpi = 600, bbox_inches='tight', pad_inches = 0)
# plt.savefig('xy-scan.pdf', dpi = 600, bbox_inches='tight', pad_inches = 0)
# plt.savefig('xy-scan.eps', dpi = 600, bbox_inches='tight', pad_inches = 0)
# plt.savefig('xy-scan.svg', dpi = 600, bbox_inches='tight', pad_inches = 0)
