import json
import matplotlib.pyplot as plt
import matplotlib.cm as cm

#matplotlib config
def matplotlib_setup(figsize_x=8.3, figsize_y=4.2):
    import matplotlib as mpl
    cmap = cm.jet
    mpl.rcParams['axes.labelsize'] = 9
    mpl.rcParams['xtick.labelsize'] = 9
    mpl.rcParams['ytick.labelsize'] = 9
    mpl.rcParams['legend.fontsize'] = 9
    #rcParams['font.family'] = 'serif'
    #rcParams['font.serif'] = ['Computer Modern Roman']
    #mpl.rcParams['text.usetex'] = True
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
    mpl.rcParams['figure.autolayout'] = True
    
#Load curve data
perco = []; rand = []; corre = []; std_perco = []; std_rand = []; std_corre = []
with open('.\percentage_percolation.json', "r") as fichier:
    perco = json.load(fichier)
with open('.\std_percolation.json', "r") as fichier:
    std_perco = json.load(fichier)
with open('.\percentage_random.json', "r") as fichier:
    rand = json.load(fichier)
with open('.\std_random.json', "r") as fichier:
    std_rand = json.load(fichier)
with open('.\percentage_correlated.json', "r") as fichier:
    corre = json.load(fichier)
with open('.\std_correlated.json', "r") as fichier:
    std_corre = json.load(fichier)	

#make the plot
matplotlib_setup(4,3)
Pmax = 12; phi = 0.15

axes = plt.gca()
axes.set_ylim([0,3])
plt.rc('text', usetex=True)
plt.errorbar( range(11)[1:], perco, yerr = std_perco, fmt='o--', color= 'b', label='percolation')
plt.errorbar( range(11)[1:], rand, yerr = std_rand, fmt='o--', color= 'r', label='random')
plt.errorbar( range(11)[1:], corre, yerr = std_corre, fmt = 'o--', color= 'g', label='correlated')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
plt.xlabel(r" \textbf{ $ N_{COAL}$ }",fontsize=14)
plt.ylabel('Social Welfare')

plt.savefig('test.pdf')
plt.savefig('test.png')
