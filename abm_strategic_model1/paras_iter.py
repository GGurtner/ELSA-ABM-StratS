# -*- coding: utf-8 -*-

"""
Template for a parameter file for iterated simulations.
The user chooses the parameters to sweep by putting their name in the list 
paras_to_loop. The values on which to loop amust be given in a variable which
has the same name than the parameter to loop, plus '_iter'.
"""

import sys as _sys
_sys.path.insert(1,'..')
import pickle as _pickle
import numpy as _np
from math import ceil as _ceil

from utilities import read_paras as _read_paras
from libs.general_tools import yes as _yes

version = '2.6.7' # Based on version 2.9.5 in Model.

# ============================================================================ #
# =============================== Parameters ================================= #
# ============================================================================ #

paras_file = 'paras.py'
paras = _read_paras(paras_file=paras_file) # Import main parameters

if paras['file_net'] == None:
	fixnetwork = True       			#if fixnetwork='False' a new graph is generated at each iteration.
else:
	fixnetwork = True

paras['file_list_of_net_file'] = None

# ---------------- Companies ---------------- #

tau_iter = _np.arange(0.0001,1.01,0.05)           # factor for shifting in time the flight plans.

# -------------- Density and times of departure patterns -------------- #
    
if paras['file_traffic']==None:
	density_iter = [2.*_i for _i in range(1,11)]
	ACtot_iter = [20*i for i in range(1,11)]
	if paras['file_times'] == None:
		if paras['departure_times']=='square_waves':
			Delta_t_iter = _np.array([0.,1., 5., 23.])
			Delta_t_iter = _np.array(Delta_t_iter*paras['unit'])
			ACsperwave_iter=[10*_i for _i in range(1,11)]			# Relevant for choosing a number of ACs per wave rather than a total number
			
noise_iter = range(0,30,2)

# ----------------- Behavioral parameters -------------- #
_range1 = list(_np.arange(0.02,0.1,0.02))
_range2 = list(_np.arange(0.9,0.98,0.02))
_range3 = list(_np.arange(0.1,0.9,0.1))
_range4 = list(_np.arange(0., 1.05, 0.1))
_range5 = list(_np.arange(0., 1.,0.2))

nA_iter = _range5

par_iter = [[[1.,0.,10.**_e], [1.,0.,1.]] for _e in range(-3,4)]

# ------------------ From M0 to M1 ------------------- #
mode_M1 = 'standard' # sweep or standard
if mode_M1 == 'standard':
	N_shocks_iter = range(0,5,1)
else: 
	STS_iter = paras['G'].nodes()

# --------------------System parameters -------------------- #
n_iter = 100 # Number of iterations for each set of parameters.

# --------------------- Paras to loop --------------- #
# Set the parameters to sweep by indicating their name. You can 
# put an empty list if you just want to have several iterations 
# of a single set of parameters.

paras_to_loop = ['nA, density']


if paras_to_loop==['nA'] and par!=tuple([tuple([float(_v) for _v in _p])  for _p in [[1.,0.,0.001], [1.,0.,1000.]]]) :
	assert _yes('The set of par does not seem consistent with the loop on nA. Proceed?')

if paras['control_density'] and not 'density' in paras_to_loop:
	assert _yes('You control density but it is not in the list of variables. Proceed?')

if not paras['control_density'] and 'density' in paras_to_loop:
	assert _yes("You don't control density but it is in the list of variables. Proceed?")

if 'control_ACsperwave' in paras.keys() and paras['control_ACsperwave'] and not 'ACsperwave' in paras_to_loop:
	assert _yes('You control ACsperwave but it is not in the list of variables. Proceed?')

if 'control_ACsperwave' in paras.keys() and not paras['control_ACsperwave'] and 'ACsperwave' in paras_to_loop:
	assert _yes("You don't control ACsperwave but it is in the list of variables. Proceed?")

if 'control_ACsperwave' in paras.keys() and (paras['control_ACsperwave'] or paras['control_density']) and 'ACtot' in paras_to_loop:
	assert _yes("You don't control ACtot but it is in the list of variables. Proceed?")

# -------------- Stuff useful if G or airports is iterated ----------- #
# You can also loop on "airports" or networks.

if 'airports' in paras_to_loop and paras_to_loop[0]!='airports':
	if not _yes("You did not put 'airports' first in the sequence!. This is going to take much more time ! Continue?"):
		_sys.exit("")

# if 'G' in paras_to_loop:
# 	G_iter=[_network_whose_name_is(_n) for _n in ['DEL_C_4A', 'DEL_C_65_20' , 'DEL_C_4A2']]#, 'DEL_C_6A']]
# 	for GG in G_iter:
# 		GG.choose_short(paras['Nsp_nav'])

##################################################################################
################################# Post processing ################################
##################################################################################
# DO NOT MODIFY THIS SECTION.

# -------------------- Post-processing -------------------- #
# Add new parameters to the dictionary.
paras['n_iter'] = n_iter
paras['par_iter'] = tuple([tuple([tuple([float(_v) for _v in _pp])  for _pp in _p])  for _p in par_iter]) # transformation in tuple, because arrays cannot be keys for dictionaries.
paras['fixnetwork'] = fixnetwork

for k,v in vars().items():
    if k[-4:]=='iter' and k[:-5] in paras_to_loop:
        paras[k] = v

paras['paras_to_loop'] = paras_to_loop

if 'file_list_of_net_file' in paras.keys() and paras['file_list_of_net_file']!=None:
	with open(paras['file_list_of_net_file'], 'r') as f:
		list_files = _pickle.load(f)

	print 'Loading networks...'
	paras['airports_iter'] = []
	for fil in list_files:
		with open(fil, 'r') as f:
			G = _pickle.load(f)
			paras['airports_iter'].append(G)

paras['paras_file'] = paras_file