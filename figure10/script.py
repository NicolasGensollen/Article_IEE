import numpy as np
import matplotlib.pyplot as plt
import random
import json

#matplotlib config
def matplotlib_setup(figsize_x=15, figsize_y=5):
    import matplotlib as mpl
    #cmap = cm.jet
    mpl.rcParams['axes.labelsize'] = 13
    mpl.rcParams['xtick.labelsize'] = 16
    mpl.rcParams['ytick.labelsize'] = 16
    mpl.rcParams['legend.fontsize'] = 14
    #rcParams['font.family'] = 'serif'
    #rcParams['font.serif'] = ['Computer Modern Roman']
    mpl.rcParams['text.usetex'] = True
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
    #mpl.rcParams['figure.autolayout'] = True

matplotlib_setup()
#Load curve data subplot a
perc_mean_utilities_percolation = []; perc_mean_utilities_random = []; perc_mean_utilities_corre = [] 
perc_std_utilities_percolation = []; perc_mean_utilities_Kmeans = []; perc_std_utilities_Kmeans = []
perc_std_utilities_random = []; perc_std_utilities_corre = []

with open('./perc_percolation_mean.json', "r") as fichier:
    perc_mean_utilities_percolation = json.load(fichier)
with open('./perc_percolation_std.json', "r") as fichier:
    perc_std_utilities_percolation = json.load(fichier)
with open('./perc_random_mean.json', "r") as fichier:
    perc_mean_utilities_random = json.load(fichier)
with open('./perc_random_std.json', "r") as fichier:
    perc_std_utilities_random = json.load(fichier)
with open('./perc_corre_mean.json', "r") as fichier:
    perc_mean_utilities_corre = json.load(fichier)
with open('./perc_corre_std.json', "r") as fichier:
    perc_std_utilities_corre = json.load(fichier)
with open('./perc_Kmeans_mean.json', "r") as fichier:
    perc_mean_utilities_Kmeans = json.load(fichier)
with open('./perc_Kmeans_std.json', "r") as fichier:
    perc_std_utilities_Kmeans = json.load(fichier)

Pmax = 16
alph = 0.3	
	

#Load curve data subplot a
mean_utilities_percolation = []; mean_utilities_random = []; mean_utilities_corre = [] 
std_utilities_percolation = []; mean_utilities_Kmeans = []; std_utilities_Kmeans = []
std_utilities_random = []; std_utilities_corre = []

with open('./percolation_mean.json', "r") as fichier:
    mean_utilities_percolation = json.load(fichier)
with open('./percolation_std.json', "r") as fichier:
    std_utilities_percolation = json.load(fichier)
with open('./random_mean.json', "r") as fichier:
    mean_utilities_random = json.load(fichier)
with open('./random_std.json', "r") as fichier:
    std_utilities_random = json.load(fichier)
with open('./corre_mean.json', "r") as fichier:
    mean_utilities_corre = json.load(fichier)
with open('./corre_std.json', "r") as fichier:
    std_utilities_corre = json.load(fichier)
with open('./Kmeans_mean.json', "r") as fichier:
    mean_utilities_Kmeans = json.load(fichier)
with open('./Kmeans_std.json', "r") as fichier:
    std_utilities_Kmeans = json.load(fichier)

#Transform data
percolation_sup = [ a + b for a,b in zip( mean_utilities_percolation, std_utilities_percolation ) ]
percolation_inf = [ a - b for a,b in zip( mean_utilities_percolation, std_utilities_percolation ) ]
random_sup = [ a + b for a,b in zip( mean_utilities_random, std_utilities_random)]
random_inf = [ a - b for a,b in zip( mean_utilities_random, std_utilities_random)]
Kmeans_sup = [ a + b for a,b in zip( mean_utilities_Kmeans, std_utilities_Kmeans)]
Kmeans_inf = [ a - b for a,b in zip( mean_utilities_Kmeans, std_utilities_Kmeans)]
corre_sup = [ a + b for a,b in zip( mean_utilities_corre, std_utilities_corre)]
corre_inf = [ a - b for a,b in zip( mean_utilities_corre, std_utilities_corre)]
	
fig = plt.figure()
ax = plt.subplot2grid((1,7),(0, 0), colspan = 3)

ax.plot( range(Pmax)[1:], mean_utilities_percolation, 'o--', color='b', label='percolation')
ax.plot( range(Pmax)[1:], mean_utilities_random, 'g^--', color='r', label='random')
ax.plot( range(Pmax)[1:], mean_utilities_Kmeans, 'bs--', color='y', label='Kmeans')
ax.plot( range(Pmax)[1:], mean_utilities_corre, 'D', color='g', label='correlated')

ax.fill_between(range(Pmax)[1:], percolation_sup, mean_utilities_percolation, facecolor='blue', alpha=alph)
ax.fill_between(range(Pmax)[1:], mean_utilities_percolation, percolation_inf, facecolor='blue', alpha=alph)
ax.fill_between(range(Pmax)[1:], random_sup, mean_utilities_random, facecolor='red', alpha=alph)
ax.fill_between(range(Pmax)[1:], mean_utilities_random, random_inf, facecolor='red', alpha=alph)
ax.fill_between(range(Pmax)[1:], Kmeans_sup, mean_utilities_Kmeans, facecolor='yellow', alpha=alph)
ax.fill_between(range(Pmax)[1:], mean_utilities_Kmeans, Kmeans_inf, facecolor='yellow', alpha=alph)
ax.fill_between(range(Pmax)[1:], corre_sup, mean_utilities_corre, facecolor='green', alpha=alph)
ax.fill_between(range(Pmax)[1:], mean_utilities_corre, corre_inf, facecolor='green', alpha=alph)

ax.text(0.05, 0.95, 'a', transform=ax.transAxes, fontsize=16, fontweight='bold', va='top')
ax.set_xlabel(r"  $ Nb_{COAL} $",fontsize=14)
ax.set_ylabel('Social Welfare', fontsize = 15)
ax.grid()
plt.xlim((0,15))
plt.ylim((0,3))
#ax.legend()
	

#Transform data
perc_percolation_sup = [ a + b for a,b in zip( perc_mean_utilities_percolation, perc_std_utilities_percolation ) ]
perc_percolation_inf = [ a - b for a,b in zip( perc_mean_utilities_percolation, perc_std_utilities_percolation ) ]
perc_random_sup = [ a + b for a,b in zip( perc_mean_utilities_random, perc_std_utilities_random)]
perc_random_inf = [ a - b for a,b in zip( perc_mean_utilities_random, perc_std_utilities_random)]
perc_Kmeans_sup = [ a + b for a,b in zip( perc_mean_utilities_Kmeans, perc_std_utilities_Kmeans)]
perc_Kmeans_inf = [ a - b for a,b in zip( perc_mean_utilities_Kmeans, perc_std_utilities_Kmeans)]
perc_corre_sup = [ a + b for a,b in zip( perc_mean_utilities_corre, perc_std_utilities_corre)]
perc_corre_inf = [ a - b for a,b in zip( perc_mean_utilities_corre, perc_std_utilities_corre)]

#ax2 = fig.add_subplot(132)
ax2 = plt.subplot2grid((1,7),(0, 3), colspan = 3)

ax2.plot( range(Pmax)[1:], perc_mean_utilities_percolation, 'o--', color='b', label='percolation')
ax2.plot( range(Pmax)[1:], perc_mean_utilities_random, 'g^--', color='r', label='random')
ax2.plot( range(Pmax)[1:], perc_mean_utilities_Kmeans, 'bs--', color='y', label='Kmeans')
ax2.plot( range(Pmax)[1:], perc_mean_utilities_corre, 'D', color='g', label='correlated')

ax2.fill_between(range(Pmax)[1:], perc_percolation_sup, perc_mean_utilities_percolation, facecolor='blue', alpha=alph)
ax2.fill_between(range(Pmax)[1:], perc_mean_utilities_percolation, perc_percolation_inf, facecolor='blue', alpha=alph)
ax2.fill_between(range(Pmax)[1:], perc_random_sup, perc_mean_utilities_random, facecolor='red', alpha=alph)
ax2.fill_between(range(Pmax)[1:], perc_mean_utilities_random, perc_random_inf, facecolor='red', alpha=alph)
ax2.fill_between(range(Pmax)[1:], perc_Kmeans_sup, perc_mean_utilities_Kmeans, facecolor='yellow', alpha=alph)
ax2.fill_between(range(Pmax)[1:], perc_mean_utilities_Kmeans, perc_Kmeans_inf, facecolor='yellow', alpha=alph)
ax2.fill_between(range(Pmax)[1:], perc_corre_sup, perc_mean_utilities_corre, facecolor='green', alpha=alph)
ax2.fill_between(range(Pmax)[1:], perc_mean_utilities_corre, perc_corre_inf, facecolor='green', alpha=alph)

#ax.text(0.05, 0.95, 'a', transform=ax.transAxes, fontsize=16, fontweight='bold', va='top')
ax2.set_xlabel(r"  $ P_{MIN} $",fontsize=14)
ax2.set_ylabel('Acceptance percentage', fontsize = 15)
ax2.grid()
#ax2.legend()
ax2.text(0.05, 0.95, 'b', transform=ax2.transAxes, fontsize=16, fontweight='bold', va='top')
plt.xlim((0,15))
plt.ylim((0,1.2))

box = ax2.get_position()
ax2.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#ax3 = fig.add_subplot(133)
ax3 = plt.subplot2grid((1,7),(0, 6), colspan = 1)
plt.axis('off')
plt.tight_layout()
plt.savefig('perc2.pdf', dpi = 300 )
