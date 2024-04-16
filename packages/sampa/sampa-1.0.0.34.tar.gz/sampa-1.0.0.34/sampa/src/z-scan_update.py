# SAMBA Copyright (C) 2024 - Closed source


import matplotlib.pyplot as plt
import numpy as np
import shutil
import os


#===============================================
shutil.copyfile('energy_scan.txt', 'z-scan.dat')
#===============================================

file    = np.loadtxt('z-scan.dat')
file.shape

date_z  = file[:,0]
date_E  = file[:,1]
E_min   = min(date_E)
E_max   = max(date_E) 
z_min   = min(date_z)
z_max   = max(date_z)
line    = np.argmin(date_E)
delta_z = date_z[line]

#==================================================
shutil.copyfile(str(delta_z) + '/POSCAR', 'POSCAR')
#==================================================



#===================================================
# Plot 2D ==========================================
#===================================================

fig, ax = plt.subplots()
plt.plot(date_z, date_E, color = 'black', linestyle = '-', linewidth = 1.0)
plt.plot([delta_z, delta_z], [-1000.0, +1000.0], color = 'red', linestyle = '--', linewidth = 1.0, alpha = 1.0)
plt.title('z-scan')
plt.xlim((z_min, z_max))
plt.ylim((E_min, E_max))
plt.xlabel('${\Delta}$Z(${\AA}$)')
plt.ylabel('E(eV)')
ax.set_box_aspect(1.25/1)

plt.savefig('z-scan.png', dpi = 600, bbox_inches='tight', pad_inches=0)
# plt.savefig('z-scan.pdf', dpi = 600, bbox_inches='tight', pad_inches=0)
# plt.savefig('z-scan.svg', dpi = 600, bbox_inches='tight', pad_inches=0)
# plt.savefig('z-scan.eps', dpi = 600, bbox_inches='tight', pad_inches=0)
