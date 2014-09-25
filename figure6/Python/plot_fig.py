import json
import numpy as np
import matplotlib
import matplotlib.cm as cm
import matplotlib.pyplot as plt

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
    
matplotlib_setup(4,3)

with open("Ncoal_Pmin_utility.json", "r") as fichier:
    M = json.load(fichier)

M = np.array(M)	
maxi = M.max()
normalized_M = np.vectorize(lambda x:float(x) / float(maxi))(M)

fig = plt.figure()
levels = np.arange(normalized_M.T.min(), normalized_M.T.max(), 0.15) 
extent = (1,9,1,10)
norm = cm.colors.Normalize(vmax=normalized_M.T.max(), vmin=normalized_M.T.min())
cmap = cm.jet
im = plt.imshow(normalized_M.T, origin='lower',extent=extent, cmap=cmap, norm=norm)
v = plt.axis()
plt.contour(normalized_M.T, levels, hold='on', colors = 'k', origin='lower', extent=extent)
plt.axis(v)
plt.title(r" \textbf{ Normalized Utility ($\phi = 0.08$) }", fontsize=8)
plt.xlabel(r" \textbf{ $ N_{COAL} $ }",fontsize=8)
plt.ylabel(r" \textbf{ $ P^{MIN}$ }",fontsize=9)
plt.colorbar(im)

plt.savefig('util.pdf')
plt.savefig('util.png')