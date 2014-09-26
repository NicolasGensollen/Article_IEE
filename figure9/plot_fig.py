import json
import numpy as np
import matplotlib
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid

def matplotlib_setup(figsize_x=8.3, figsize_y=4.2):
    import matplotlib as mpl
    cmap = cm.jet
    mpl.rcParams['axes.labelsize'] = 9
    mpl.rcParams['xtick.labelsize'] = 9
    mpl.rcParams['ytick.labelsize'] = 9
    mpl.rcParams['legend.fontsize'] = 9
    #rcParams['font.family'] = 'serif'
    #rcParams['font.serif'] = ['Computer Modern Roman']
    mpl.rcParams['text.usetex'] = True
    mpl.rcParams['figure.figsize'] = 7.3, 4.2
    mpl.rcParams['axes.labelweight'] = 'bold'
    mpl.rcParams['font.weight'] = 'bold'
    mpl.rcParams['axes.linewidth'] = 0.75    
    mpl.rcParams['lines.linewidth'] = 2
    mpl.rcParams['axes.linewidth'] = 0.75    
    mpl.rcParams['lines.linewidth'] = 2
    mpl.rcParams['lines.markersize'] = 8
    mpl.rcParams['legend.numpoints'] = 1
    # figure size in inch
    mpl.rcParams['figure.figsize'] = figsize_x, figsize_y
    # figure dots per inch
    mpl.rcParams['figure.dpi'] = 300
    
matplotlib_setup(4,2)




fig = plt.figure()
grid = ImageGrid(fig, (1, 1, 1), nrows_ncols=(1, 2), axes_pad=0.2,
                 add_all=True, label_mode='L', cbar_mode='single',
                 cbar_location='right', cbar_pad=0.1)

with open("phi_Pmin_utility.json", "r") as fichier:
    M = json.load(fichier)
M = np.array(M)	
maxi = M.max()
normalized_M = np.vectorize(lambda x:float(x) / float(maxi))(M)
levels = np.arange(normalized_M.T.min(), normalized_M.T.max(), 0.2) 
extent = (0,6,0,7)
norm = cm.colors.Normalize(vmax=normalized_M.T.max(), vmin=normalized_M.T.min())
cmap = cm.jet
im = grid[0].imshow(normalized_M.T, origin='lower',extent=extent, cmap=cmap, norm=norm)
v = grid[0].axis()
grid[0].contour(normalized_M.T, levels, hold='on', colors = 'k', origin='lower', extent=extent)
grid[0].axis(v)
#ax2.title("Utility", fontsize=9)
grid[0].text(0.05, 0.95, 'a', transform=grid[0].transAxes, color='w', fontsize=16, fontweight='bold', va='top')
grid[0].set_xlabel(r" \textbf{ $ \phi*10 $ ( $ N_{COAL} = 10 $ ) }",fontsize=9)
grid[0].set_ylabel(r" \textbf{ $ P^{MIN}$ }",fontsize=10)

with open("Ncoal_Pmin_utility.json", "r") as fichier:
    M = json.load(fichier)

M = np.array(M)	
maxi = M.max()
normalized_M = np.vectorize(lambda x:float(x) / float(maxi))(M)
levels = np.arange(normalized_M.T.min(), normalized_M.T.max(), 0.15) 
extent = (1,9,0,7)
norm = cm.colors.Normalize(vmax=normalized_M.T.max(), vmin=normalized_M.T.min())
cmap = cm.jet
im = grid[1].imshow(normalized_M.T, origin='lower',extent=extent, cmap=cmap, norm=norm)
v = grid[1].axis()
grid[1].contour(normalized_M.T, levels, hold='on', colors = 'k', origin='lower', extent=extent)
grid[1].axis(v)
#ax.title(r" \textbf{ Normalized Utility ($\phi = 0.08$) }", fontsize=8)
grid[1].text(0.9, 0.95, 'b', transform=grid[1].transAxes, color='w', fontsize=16, fontweight='bold', va='top')
grid[1].set_xlabel(r" \textbf{ $ N_{COAL} $ (  $ \phi = 0.08 $ ) }",fontsize=8)
grid[1].set_ylabel(r" \textbf{ $ P^{MIN}$ }",fontsize=9)

grid.cbar_axes[0].colorbar(im)
grid[0].set_title(r" \textbf{ Normalized Utility}", fontsize=8)
grid[1].set_title(r" \textbf{ Normalized Utility}", fontsize=8)
plt.draw()



'''
fig = plt.figure()
ax2 = fig.add_subplot(121, sharey=True)
levels = np.arange(normalized_M.T.min(), normalized_M.T.max(), 0.2) 
extent = (0,6,0,7)
norm = cm.colors.Normalize(vmax=normalized_M.T.max(), vmin=normalized_M.T.min())
cmap = cm.jet
im = plt.imshow(normalized_M.T, origin='lower',extent=extent, cmap=cmap, norm=norm)
v = ax2.axis()
ax2.contour(normalized_M.T, levels, hold='on', colors = 'k', origin='lower', extent=extent)
ax2.axis(v)
#ax2.title("Utility", fontsize=9)
ax2.set_xlabel(r" \textbf{ $ \phi $ }",fontsize=9)
ax2.set_ylabel(r" \textbf{ $ P^{MIN}$ }",fontsize=10)
#ax2.colorbar(im)





ax = fig.add_subplot(122, sharey=True)
levels = np.arange(normalized_M.T.min(), normalized_M.T.max(), 0.15) 
extent = (1,9,1,10)
norm = cm.colors.Normalize(vmax=normalized_M.T.max(), vmin=normalized_M.T.min())
cmap = cm.jet
im = ax.imshow(normalized_M.T, origin='lower',extent=extent, cmap=cmap, norm=norm)
v = ax.axis()
ax.contour(normalized_M.T, levels, hold='on', colors = 'k', origin='lower', extent=extent)
ax.axis(v)
#ax.title(r" \textbf{ Normalized Utility ($\phi = 0.08$) }", fontsize=8)
ax.set_xlabel(r" \textbf{ $ N_{COAL} $ }",fontsize=8)
ax.set_ylabel(r" \textbf{ $ P^{MIN}$ }",fontsize=9)
#ax.colorbar(im)
'''
plt.savefig('util.pdf')
plt.savefig('util.png')