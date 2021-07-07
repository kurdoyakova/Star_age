from matplotlib import pyplot as plt
from astropy.io import fits
import numpy as np
import matplotlib.lines as lines
import matplotlib.style as stl
from collections import OrderedDict
import matplotlib.ticker as ticker
# stl.use('seaborn')
 
Mass_given = 13.5
Mass_err = 2
Teff_given = 26405
Teff_err = 1549
LogL_given = 4.86
LogL_err = 0.3

list_ages = [1.06]
# list_ages = [5.4]
list_vinit = [0,350,400,450,500]

colormap = plt.cm.jet   #gnuplot2, summer, cool, Set2, 
colors = [colormap(i) for i in np.linspace(0, 1,len(list_vinit))]
linestyles = ['-', '--', '-.', 'dotted', (0, (1, 10)), (0, (3, 1, 1, 1, 1, 1)), (0, (3, 5, 1, 5, 1, 5))] 
fig, ax = plt.subplots()
for i_age, age in enumerate(list_ages):
    res = fits.open("_5F" + str(age) + "E_2B07.mw.dat")[1].data
    # res = fits.open("_5F" + str(age) + "0E_2B06.mw.dat")[1].data

    for i, vinit in enumerate(list_vinit):
        globals()['list_vinit'+str(vinit)] = []

    delta=2
    for iv, v in enumerate(res['vinit']):
        for i, vinit in enumerate(list_vinit):
            if res['vinit'][iv] < vinit + delta and res['vinit'][iv] > vinit - delta:
                globals()['list_vinit'+str(vinit)].append(iv) 

    for i,vinit in enumerate(list_vinit):
        v = globals()['list_vinit'+str(vinit)]
        track_l = []
        track_t = []
        for iv, vi in enumerate(v):
            track_t.append(res['Teff'][vi])
            track_l.append(res['logL'][vi])
        track_line = lines.Line2D(track_t, track_l, label=str(vinit)+' km/s', linewidth=1.2, color=colors[i])# linestyle=linestyles[i])
        plt.gca().add_line(track_line)

plt.gca().set_xlim(5e4,3e3)
plt.gca().set_ylim(2.5,6.3)
plt.gca().legend(loc='lower left',  prop={'size': 13},  markerfirst=False, frameon=False)
plt.ylabel(r'$log  \ ( L \ / \ L_\odot)$', size=12)
plt.xlabel("$T_{eff}$", size=14)
plt.plot(Teff_given,LogL_given,marker="*",ms=15, color='black')
plt.errorbar(Teff_given,LogL_given, xerr=Teff_err, lw=1.5, fmt='.k', capsize = 4, capthick = 2, ecolor="black")
plt.title(str(list_ages[0]) + ' Myrs')
plt.ticklabel_format(scilimits=(3,3), axis='x')
plt.show()
plt.clf()

