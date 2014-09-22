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
    mpl.rcParams['figure.autolayout'] = True

#Load curve data subplot a
perco = []; rand = []; corre = []; std_perco = []; std_rand = []; std_corre = []
with open('fig_percentage\percentage_percolation.json', "r") as fichier:
    perco = json.load(fichier)
with open('fig_percentage\std_percolation.json', "r") as fichier:
    std_perco = json.load(fichier)
with open('fig_percentage\percentage_random.json', "r") as fichier:
    rand = json.load(fichier)
with open('fig_percentage\std_random.json', "r") as fichier:
    std_rand = json.load(fichier)
with open('fig_percentage\percentage_correlated.json', "r") as fichier:
    corre = json.load(fichier)
with open('fig_percentage\std_correlated.json', "r") as fichier:
    std_corre = json.load(fichier)

#Transform data
perco_sup = [a+b for a,b in zip(perco,std_perco)]
perco_inf = [a-b for a,b in zip(perco,std_perco)]
rand_sup = [a+b for a,b in zip(rand,std_rand)]
rand_inf = [a-b for a,b in zip(rand,std_rand)]
corre_sup = [a+b for a,b in zip(corre,std_corre)]
corre_inf = [a-b for a,b in zip(corre,std_corre)]

#Load curve data subplot b
perco2 = []; rand2 = []; corre2 = []; std_perco2 = []; std_rand2 = []; std_corre2 = []
with open('fig_SW\percentage_percolation.json', "r") as fichier:
    perco2 = json.load(fichier)
with open('fig_SW\std_percolation.json', "r") as fichier:
    std_perco2 = json.load(fichier)
with open('fig_SW\percentage_random.json', "r") as fichier:
    rand2 = json.load(fichier)
with open('fig_SW\std_random.json', "r") as fichier:
    std_rand2 = json.load(fichier)
with open('fig_SW\percentage_correlated.json', "r") as fichier:
    corre2 = json.load(fichier)
with open('fig_SW\std_correlated.json', "r") as fichier:
    std_corre2 = json.load(fichier)

#Transform data
perco_sup2 = [a+b for a,b in zip(perco2,std_perco2)]
perco_inf2 = [a-b for a,b in zip(perco2,std_perco2)]
rand_sup2 = [a+b for a,b in zip(rand2,std_rand2)]
rand_inf2 = [a-b for a,b in zip(rand2,std_rand2)]
corre_sup2 = [a+b for a,b in zip(corre2,std_corre2)]
corre_inf2 = [a-b for a,b in zip(corre2,std_corre2)]

#make the plot
matplotlib_setup(4,3)
Pmax = 11; phi = 0.15; alph = .3

fig = plt.figure()
ax = fig.add_subplot(121)
ax.set_ylim([0,3])
ax.plot( range(Pmax)[1:], perco2, 'o--', color='b', label='percolation')
ax.plot( range(Pmax)[1:], rand2, 'o--', color='r', label='random')
ax.plot( range(Pmax)[1:], corre2, 'o--', color='g', label='correlated')
ax.fill_between(range(Pmax)[1:], perco_sup2, perco2, facecolor='blue', alpha=alph)
ax.fill_between(range(Pmax)[1:], perco2, perco_inf2, facecolor='blue', alpha=alph)
ax.fill_between(range(Pmax)[1:], rand_sup2, rand2, facecolor='red', alpha=alph)
ax.fill_between(range(Pmax)[1:], rand2, rand_inf2, facecolor='red', alpha=alph)
ax.fill_between(range(Pmax)[1:], corre_sup2, corre2, facecolor='green', alpha=alph)
ax.fill_between(range(Pmax)[1:], corre2, corre_inf2, facecolor='green', alpha=alph)
ax.text(0.05, 0.95, 'a', transform=ax.transAxes, fontsize=16, fontweight='bold', va='top')
ax.set_xlabel(r" \textbf{ $ N_{COAL}$ }",fontsize=14)
ax.set_ylabel('Social Welfare')
ax.grid()

Pmax = 12; phi = 0.15; nb_coal = 7; alph = .3

ax2 = fig.add_subplot(122)
ax2.set_ylim([0,1.2])
ax2.set_xlim([0,11])
ax2.plot( range(Pmax), perco, 'o--', color='b', label='percolation')
ax2.plot( range(Pmax), rand, 'o--', color='r', label='random')
ax2.plot( range(Pmax), corre, 'o--', color='g', label='correlated')
ax2.fill_between(range(Pmax), perco_sup, perco, facecolor='blue', alpha=alph)
ax2.fill_between(range(Pmax), perco, perco_inf, facecolor='blue', alpha=alph)
ax2.fill_between(range(Pmax), rand_sup, rand, facecolor='red', alpha=alph)
ax2.fill_between(range(Pmax), rand, rand_inf, facecolor='red', alpha=alph)
ax2.fill_between(range(Pmax), corre_sup, corre, facecolor='green', alpha=alph)
ax2.fill_between(range(Pmax), corre, corre_inf, facecolor='green', alpha=alph)
ax2.text(1.5, 0.95, 'b', transform=ax.transAxes, fontsize=16, fontweight='bold', va='top')
ax2.legend(bbox_to_anchor=(1.05, 1), loc=2, ncol=3, fancybox=True, shadow=False)
ax2.set_xlabel(r" \textbf{ $ P_{\phi}^{MIN}$ }",fontsize=14)
ax2.set_ylabel('Valid coalition percentage')
ax2.grid()
plt.savefig('fig8.pdf')
plt.savefig('fig8.eps')
plt.savefig('fig8.png')
