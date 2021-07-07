from astropy.io import fits 
import numpy
import urllib.request
import os
import requests
from matplotlib import pyplot as plt

url_list = [
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F0.00E_2B00.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.00E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.00E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.02E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.04E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.06E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.08E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.10E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.12E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.14E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.16E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.18E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.20E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.20E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.22E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.24E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.26E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.28E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.30E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.32E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.34E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.36E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.38E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.40E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.40E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.42E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.44E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.46E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.48E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.50E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.52E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.54E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.56E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.58E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.60E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.60E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.62E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.64E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.66E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.68E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.70E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.72E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.74E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.76E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.78E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.80E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.80E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.82E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.84E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.86E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.88E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.90E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.92E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.94E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.96E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F1.98E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.00E_2B05.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.00E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.00E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.02E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.04E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.06E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.08E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.10E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.12E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.14E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.16E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.18E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.20E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.20E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.22E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.24E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.26E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.28E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.30E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.32E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.34E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.36E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.38E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.40E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.40E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.42E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.44E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.46E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.48E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.50E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.52E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.54E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.56E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.58E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.60E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.60E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.62E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.64E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.66E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.68E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.70E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.72E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.74E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.76E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.78E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.80E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.80E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.82E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.84E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.86E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.88E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.90E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.92E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.94E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.96E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F2.98E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F3.00E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F3.00E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F3.02E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F3.04E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F3.06E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F3.08E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F3.10E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F3.12E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F3.14E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F3.16E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F3.18E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F3.20E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F3.20E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F3.22E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F3.24E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F3.26E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F3.28E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F3.30E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F3.32E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F3.34E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F3.36E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F3.38E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F3.40E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F3.40E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F3.42E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F3.44E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F3.46E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F3.48E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F3.50E_2B07.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F3.60E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F3.80E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F4.00E_2B05.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F4.00E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F4.20E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F4.40E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F4.60E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F4.80E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F5.00E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F5.20E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F5.40E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F5.60E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F5.80E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F6.00E_2B05.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F6.00E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F6.20E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F6.40E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F6.60E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F6.80E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F7.00E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F7.20E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F7.40E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F7.60E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F7.80E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F8.00E_2B05.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F8.00E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F8.20E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F8.40E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F8.60E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F8.80E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F9.00E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F9.20E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F9.40E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F9.60E_2B06.mw.dat',
'https://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?-plus=-+&J/A%2BA/530/A115/./iso/aiso_5F9.80E_2B06.mw.dat',
]
list_filenames = []
for i, url in enumerate(url_list):
    name =  url[85:]
    if not os.path.exists(name):
        urllib.request.urlretrieve(url, name)
    list_filenames.append(name)

def selection(param, min_val, max_val, list_rows):
    selected = []
    for i in list_rows:
        value = data[i][param]
        if (value >= min_val and value <= max_val):
            selected.append(i)
    return selected
    # length = len(list_rows)
    # i = 0
    # while i < length:
    #     id_row = list_rows[i]
    #     row = data[id_row]
    #     value = row[param]
    #     if not (value >= min_val and value <= max_val):
    #         del list_rows[i]
    #         length -= 1
    #     else:
    #         i += 1

dict_ages = {}
for number_file, fits_table_filename in enumerate(list_filenames):
    hdul = fits.open(fits_table_filename)
    data = hdul[1].data

    list_rows = [ i for i in range(len(data)) ]

    mass = 1
    luminosity = 3
    velocity = 7
    radius = 4
    gravity = 6
    temperature = 2
    list_rows = selection(mass, 13 , 14, list_rows)
    # list_rows = selection(gravity, 3.15 , 3.35, list_rows)
    list_rows = selection(luminosity, 4.5 , 5.2, list_rows)
    list_rows = selection(velocity, 120 , 140, list_rows)
    # list_rows = selection(radius, 16.8 , 23.6, list_rows)
    list_rows = selection(temperature, 24500 , 28000, list_rows)
    

    for i in list_rows:
        age = data[i][0]
        dict_ages.setdefault(age,0)
        dict_ages[age] += 1
    print(round(float(number_file)/len(list_filenames)*100),"%")


print(dict_ages)