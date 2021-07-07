from matplotlib import pyplot as plt
from astropy.io import fits
import numpy as np
import matplotlib.lines as lines
import matplotlib.style as stl
from collections import OrderedDict
import matplotlib.ticker as ticker
# stl.use('seaborn')

Vinit_start = 500
Vinit_min = Vinit_start - 2
Vinit_max = Vinit_start + 2
 
Mass_given = 13.5
Mass_err = 2
Teff_given = 26405
Teff_err = 1549
LogL_given = 4.86
LogL_err = 0.3
Vsurf = 130
R_given = 6.9
R_err = 0.2

list_ages = [1.02, 1.04, 1.06, 1.08,  1.12, 1.14]
# list_ages = [5.4]

colormap = plt.cm.jet   #gnuplot2, summer, cool, Set2, 
colors = [colormap(i) for i in np.linspace(0, 1,len(list_ages))]
linestyles = ['-', '--', '-.', 'dotted', (0, (1, 10)), (0, (3, 1, 1, 1, 1, 1)), (0, (3, 5, 1, 5, 1, 5))] 
fig, ax = plt.subplots()
for i_age, age in enumerate(list_ages):
    res = fits.open("_5F" + str(age) + "E_2B07.mw.dat")[1].data
    # res = fits.open("_5F" + str(age) + "0E_2B06.mw.dat")[1].data

    list_v = []
    list_vsurf = []
    for iv, v in enumerate(res['vinit']):
        if res['Mass'][iv] < Mass_given+Mass_err and res['Mass'][iv] > Mass_given-Mass_err and \
           res['Teff'][iv] > Teff_given-Teff_err and res['Teff'][iv] < Teff_given+Teff_err and \
           res['Vinit'][iv] > Vinit_min and res['Vinit'][iv] < Vinit_max and \
           res['logL'][iv] > LogL_given-LogL_err and res['logL'][iv] < LogL_given+LogL_err : 
            list_v.append(v)
            list_vsurf.append(res['vsurf'][iv])
            break

    track_l = { key: list() for key in list_v}
    track_t = { key: list() for key in list_v}
    for iv, v in enumerate(res['vinit']):
        if v in list_v: 
            track_t[v].append(res['Teff'][iv])
            track_l[v].append(res['logL'][iv])
    for iv, v in enumerate(list_v):
        track_line = lines.Line2D(track_t[v], track_l[v], label=str(age)+' Myr', linewidth=0.8, color=colors[i_age]) #,linestyle=linestyles[i])
        plt.gca().add_line(track_line)

plt.gca().set_xlim(5e4,3e3)
plt.gca().set_ylim(2.5,6.3)
plt.gca().legend(loc='lower left',  prop={'size': 13},  markerfirst=False, frameon=False)
plt.ylabel(r'$log  \ ( L \ / \ L_\odot)$', size=12)
plt.xlabel("$T_{eff}$", size=14)
plt.plot(Teff_given,LogL_given,marker="*",ms=15, color='black')
plt.errorbar(Teff_given,LogL_given, xerr=Teff_err, yerr=LogL_err,lw=1.5, fmt='.k', capsize = 4, capthick = 2, ecolor="black")
plt.ticklabel_format(scilimits=(3,3), axis='x')
plt.title(str(r'Возможные возрасты для скоростей '+ str(Vinit_start) + ' km/s'))
# plt.savefig('all11.eps', format='eps' )
plt.show()
plt.clf()

