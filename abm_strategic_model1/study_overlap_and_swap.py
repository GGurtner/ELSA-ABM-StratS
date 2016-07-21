#!/usr/bin/env python

# -*- coding: utf-8 -*-

import pickle
#from ABMvars import paras, give_airports_to_network, NoAirportsLeft
from performance_plots import get_results
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
from scipy.optimize import curve_fit
from scipy.stats.mstats import mquantiles
from math import sqrt
import os
import networkx as nx
import pandas as pd

pd.options.display.mpl_style = 'default'

nice_colors = ['#348ABD', '#7A68A6', '#A60628', '#467821', '#CF4457', '#188487', '#E24A33']

version='2.6.0'

def reduce_span(a,b,xmin=-1, xmax=1):
	aa=[p for p in a if xmin<=p<=xmax]
	bb=[p for i,p in enumerate(b) if xmin<=a[i]<=xmax]
	return aa, bb

def unique_sectors(paths):

	length = len(paths[0])
	#min_length=min([len(path) for path in paths])

	n_u=[]
	for i in range(length):
		# Add the set of unique sectors crossed at position i.
		n_u.append(len(np.unique([path[i] for path in paths if i<len(path)])))

	return n_u

def total_static_overlap(paths):
	overlaps=[]
	for i, p1 in enumerate(paths):
		for j, p2 in enumerate(paths):
			if i<j:
				# print 'Path p1:', p1
				# print 'Path p2:', p2
				# print 'Intersection:', set(p1).intersection(set(p2))
				common_elements = float(len(set(p1).intersection(set(p2))))
				# print 'Length of intersection:', common_elements
				all_elements = float(len(set(p1).union(set(p2))))
				# print 'Union:', set(p1).union(set(p2))
				# print 'Lenght of Union:', all_elements
				# print 'Ratio inter/union:', common_elements/all_elements
				# print
				overlaps.append(common_elements/all_elements)
	return np.mean(overlaps)

def compute_ratio(results_global):
	s_0_S=results_global[((1.0, 0.0, 0.001), (1.0, 0.0, 1.0))][0]['satisfaction']['avg']
	s_infty_S=results_global[((1.0, 0.0, 0.001), (1.0, 0.0, 1.0))][23]['satisfaction']['avg']
	s_0_R=results_global[((1.0, 0.0, 1000.), (1.0, 0.0, 1.0))][0]['satisfaction']['avg']
	s_infty_R=results_global[((1.0, 0.0, 1000.), (1.0, 0.0, 1.0))][23]['satisfaction']['avg']
	return (s_0_S - s_0_R)/(s_infty_S - s_infty_R)#, s_0_S, s_0_R, s_infty_S, s_infty_R

def check_swap(results_global):
	s_0_S=results_global[((1.0, 0.0, 0.001), (1.0, 0.0, 1.0))][0]['satisfaction']['avg']
	s_0_R=results_global[((1.0, 0.0, 1000.), (1.0, 0.0, 1.0))][0]['satisfaction']['avg']
	if (s_0_S - s_0_R)>0.:
		return 1.
	else:
		return 0.

def swap_magnitude(results_global):
	s_0_S=results_global[((1.0, 0.0, 0.001), (1.0, 0.0, 1.0))][0]['satisfaction']['avg']
	s_0_R=results_global[((1.0, 0.0, 1000.), (1.0, 0.0, 1.0))][0]['satisfaction']['avg']
	return s_0_S - s_0_R

def diff_infty(results_global):
	#s_0_S=results_global[((1.0, 0.0, 0.001), (1.0, 0.0, 1.0))][0]['satisfaction']['avg']
	try:
		s_infty_S=results_global[((1.0, 0.0, 0.001), (1.0, 0.0, 1.0))][23]['satisfaction']['avg']
		#s_0_R=results_global[((1.0, 0.0, 1000.), (1.0, 0.0, 1.0))][0]['satisfaction']['avg']
		s_infty_R=results_global[((1.0, 0.0, 1000.), (1.0, 0.0, 1.0))][23]['satisfaction']['avg']
	except KeyError:
		print results_global
		raise
	return (s_infty_S - s_infty_R)

def save_fig(plot):
	def wrapper(*args, **kwargs):
		rep = kwargs['rep']
		kwargs.pop('rep', None)
		ret = plot(*args, **kwargs)
		print 'Graph saved in', rep
		if rep!='':
			plt.savefig(rep + '/' +plot.func_name + '.svg', close=False)
			plt.savefig(rep + '/' +plot.func_name + '.png')
		return ret
	return wrapper

@save_fig
def nu_vs_rank(n_u_avg, n_u_std, minn=[], maxx=[]):
	plt.figure()
	plt.errorbar(range(len(n_u_avg)), n_u_avg, n_u_std, fmt='o',color='r')
	if minn != []:
		plt.plot(minn, 'bo')
	if maxx != []:
		plt.plot(maxx, 'bo')
	#plt.plot(n_u, 'ro')
	plt.xlabel('Rank')
	plt.ylabel('Number of unique sectors')

@save_fig
def histo_ratios(ratios, bins=20):
	plt.figure()
	plt.hist(ratios, facecolor='blue', alpha=0.5, bins=bins)
	plt.xlabel('overlap')

@save_fig
def histo_swap(swap, bins=20, normed=False):
	plt.figure(figsize=(10,7))
	hh = plt.hist(swap, facecolor='blue', alpha=0.5, bins=bins, normed=normed)
	max_count = max(hh[0])
	med_swap = np.median(swap)
	plt.plot([med_swap, med_swap], [0., max_count], '--', c=nice_colors[2])
	plt.xlabel(r'$\delta\mathcal{S}(0)$',  fontsize=24, labelpad=-5)
	plt.ylabel('Counts', fontsize=24)
	plt.tick_params(labelsize = 18)

@save_fig
def histo_swap_cul(swap, bins=20, normed=False):
	plt.figure(figsize=(10,7))
	hh = plt.hist(swap, facecolor='blue', alpha=0.5, bins=bins, cumulative=True, normed=normed)
	max_count = max(hh[0])
	med_swap = np.median(swap)
	plt.plot([med_swap, med_swap], [0., max_count], '--', c=nice_colors[2])
	plt.xlabel(r'$\delta\mathcal{S}(0)$',  fontsize=24, labelpad=-5)
	plt.ylabel('Counts', fontsize=24)
	plt.tick_params(labelsize = 18)


@save_fig
def histo_overlap(overlap, bins=20):
	plt.figure()
	plt.hist(overlap, facecolor='green', alpha=0.5, bins=bins)
	plt.xlabel('overlap')

@save_fig
def ratio_vs_nu(n_u, ratios, rank=1):
	plt.figure()
	plt.suptitle('ratios versus n_u of rank ' + str(rank))
	x=[p[rank] for p in n_u]
	#ratios, x = reduce_span(ratios, x)
	plt.plot(x, ratios, 'ro')
	ratios_avg = [np.mean([r for i,r in enumerate(ratios) if x[i]==ns]) for ns in np.unique(x)]
	ratios_std = [np.std([r for i,r in enumerate(ratios) if x[i]==ns]) for ns in np.unique(x)]
	plt.errorbar(np.unique(x), ratios_avg, ratios_std, fmt='--', color='b')
	plt.ylim((-1,1))
	plt.xlabel('Number of unique sectors')
	plt.ylabel('Ratio')

@save_fig
def ratio_vs_static_overlap(overlap, ratios):
	def f_fit(x, a, b):
		return a*x +  b
	#ratios, overlap = reduce_span(ratios, overlap)
	overlap, ratios = zip(*sorted(zip(overlap,ratios)))
	popt, pcov = curve_fit(f_fit, overlap, ratios)
	plt.figure()
	plt.plot(overlap, ratios, 'ro')
	plt.plot(overlap, f_fit(overlap, *popt), 'b-')
	plt.xlabel('Mean overlap')
	plt.ylim((-1,1))
	plt.ylabel('Ratio')

# def ratio_vs_static_overlap(overlap, ratios, rep= []):
# 	def f_fit(x, a, b):
# 		return a*x +  b
# 	#ratios, overlap = reduce_span(ratios, overlap)
# 	overlap, ratios = zip(*sorted(zip(overlap,ratios)))
# 	popt, pcov = curve_fit(f_fit, overlap, ratios)
# 	plt.figure()
# 	plt.plot(overlap, ratios, 'ro')
# 	plt.plot(overlap, f_fit(overlap, *popt), 'b-')
# 	plt.xlabel('Mean overlap')
# 	plt.ylim((-1,1))
# 	plt.ylabel('Ratio')

@save_fig
def swap_mag_vs_static_overlap(overlap, swap, n_quantiles=10):
	def f_fit(x, a, b):
		return a*x +  b
	#ratios, overlap = reduce_span(ratios, overlap)
	overlap, swap = zip(*sorted(zip(overlap,swap)))
	popt, pcov = curve_fit(f_fit, overlap, swap)


	plt.figure()
	plt.plot(overlap, swap, 'ro')
	plt.plot(overlap, f_fit(overlap, *popt), 'b-')
	plt.xlabel('Mean overlap')
	plt.ylim((-1,1))
	plt.ylabel('Swap magnitude')

@save_fig
def swap_mag_vs_static_overlap_averaged(overlap, swap, n_quantiles=10):
	plt.figure(figsize=(10,7))
	qs = mquantiles(overlap, prob=np.arange(min(overlap), max(overlap), (max(overlap) - min(overlap))/float(n_quantiles)))
	swap_avg = [np.mean([s for j,s in enumerate(swap) if qs[i]<=overlap[j]<qs[i+1]]) for i in range(len(qs)-1)]
	swap_std = [np.std([s for j,s in enumerate(swap) if qs[i]<=overlap[j]<qs[i+1]])/sqrt(len([s for j,s in enumerate(swap) if qs[i]<=overlap[j]<qs[i+1]])) for i in range(len(qs)-1)]
	overlap_avg = [np.mean([s for j,s in enumerate(overlap) if qs[i]<=overlap[j]<qs[i+1]]) for i in range(len(qs)-1)]

	plt.errorbar(overlap_avg, swap_avg, swap_std, fmt='o--', c='b')
	#plt.xlabel('Overlap (' + str(n_quantiles) + '-quantiles)')
	plt.xlabel('Overlap',  fontsize=24, labelpad=-3)
	#plt.ylabel('Averaged magnitude', fontsize=24))
	plt.ylabel(r'$\delta\mathcal{S}(0)$', fontsize=24, labelpad=-3)
	plt.tick_params(labelsize = 18)

@save_fig
def proba_swap(overlap, swap, n_quantiles=10):
	overlap, swap = zip(*sorted(zip(overlap,swap)))
	qs = mquantiles(overlap, prob=np.arange(min(overlap), max(overlap), (max(overlap) - min(overlap))/float(n_quantiles)))
	swap_avg = [np.mean([s for j,s in enumerate(swap) if qs[i]<=overlap[j]<qs[i+1]]) for i in range(len(qs)-1)]
	swap_std = [np.std([s for j,s in enumerate(swap) if qs[i]<=overlap[j]<qs[i+1]])/sqrt(len([s for j,s in enumerate(swap) if qs[i]<=overlap[j]<qs[i+1]])) for i in range(len(qs)-1)]
	overlap_avg = [np.mean([s for j,s in enumerate(overlap) if qs[i]<=overlap[j]<qs[i+1]]) for i in range(len(qs)-1)]

	plt.figure()
	plt.errorbar(overlap_avg, swap_avg,swap_std, fmt='o--', c='b')
	plt.xlabel('Overlap (' + str(n_quantiles) + '-quantiles)')
	plt.ylabel('Probability')

def fetch_pairs_airports():
	pairs_airports = []
	for f in os.listdir('.'):
		if f[:len('Sim_v2.6_NEWDEL1000_C_')] == 'Sim_v2.6_NEWDEL1000_C_' and f!='Sim_v2.6_NEWDEL1000_C_spatial':
			a = split(split(f,'C_')[1], '_')
			print f
			a1 = int(a[0])
			a2 = int(a[1])
			pairs_airports.append((a1, a2))

	print 'Found', len(pairs_airports), 'pairs of airports, selected the 1000 last ones'
	return  pairs_airports


if __name__=='__main__':
	#name = 'DEL_C_65_22'
	#name = 'NEWDEL1000_C_spatial'

	#name = 'DEL29_C5_65_20_v2'
	#name = 'DEL29_C5_65_20_v2'
	
	#with open('../networks/' + name + '.pic', 'r') as f:
	#	GG=pickle.load(f)

	dirr = '../results/study_overlap'

	

	distance = 7
	assert distance == paras['distance']
	# pairs_distance=[]
	# for i,n in enumerate(GG.nodes()):
	#     for j,m in enumerate(GG.nodes()):
	#         if i<j:
	#             if len(nx.shortest_path(GG,n,m))==distance:
	#                 pairs_distance.append([n,m])

	G=paras['G']
	paras['paras_to_loop']=paras['paras_to_loop'][:2]

	os.system('mkdir -p ' + dirr + '/' + G.name)

	assert paras['paras_to_loop'] == ['par', 'Delta_t']

	n_u_tot = []
	static_overlap_tot=[]
	#ratios = []
	swap_tot = []
	non_positive = []
	swap_mag_tot = []

	print "Number of pairs of airports:", len(paras['airports_iter'])
	for airports in paras['airports_iter']:
		print 'Doing airports', airports
		try:
			give_airports_to_network(G, airports, distance=distance, repetitions=False)#, paras['Nsp_nav'])
		except NoAirportsLeft:
			print "Skipping airports", airports
			continue

		try:
			assert len(nx.shortest_path(G,airports[0], airports[1], weight = 'weight'))==7
		except:
			print 'The shortest path is longer than 7:', len(nx.shortest_path(G,airports[0], airports[1], weight = 'weight'))
		
		print G.short.keys()
		paras['G']=deepcopy(G)
		try:
			n_u = unique_sectors(G.short[tuple(G.airports)])  # Just one direction.
		except KeyError:
			print ("problem of airports, I skyp this value.")
			continue

		n_u_tot.append(n_u)
		static_overlap = total_static_overlap(G.short[tuple(G.airports)])
		static_overlap_tot.append(static_overlap)
		results, results_global = get_results(paras, vers='2.6')
		#ratio = compute_ratio(results_global)
		if diff_infty(results_global)<0.:
		#if diff_infty(results_global[(airports[0], airports[1])])<0.:
			print 'Difference between S and R for big Delta_t is negative!', diff_infty(results_global)
			non_positive.append((G.airports, diff_infty(results_global)))
		swap = check_swap(results_global)
		swap_tot.append(swap)
		swap_mag = swap_magnitude(results_global)
		swap_mag_tot.append(swap_mag)

		#if airports == (800, 939):
		#	raise Exception('')
		#ratios.append(ratio)

		if 1:
			print 'Unique sectors:', n_u
			print 'Static overlap:', static_overlap
			#print 'Ratio:', ratio
			#print 's_0_S, s_0_R, s_infty_S, s_infty_R', s_0_S, s_0_R, s_infty_S, s_infty_R
			#print results_global
		print 

	print 'There were', len(non_positive), 'pairs for which the difference between S and R for big Delta_t was negative:'
	#print non_positive
		
	#print [[n_u[i] for n_u in n_u_tot] for i in range(distance)]
	n_u_min = [min([n_u[i] for n_u in n_u_tot]) for i in range(distance)]
	n_u_max = [max([n_u[i] for n_u in n_u_tot]) for i in range(distance)]
	n_u_avg = [np.mean([n_u[i] for n_u in n_u_tot]) for i in range(distance)]
	n_u_std = [np.std([n_u[i] for n_u in n_u_tot]) for i in range(distance)]

	nu_vs_rank(n_u_avg, n_u_std, minn=n_u_min, maxx=n_u_max, rep= dirr + '/' + G.name)
	histo_overlap(static_overlap_tot, rep= dirr + '/' + G.name, bins=30)
	histo_swap(swap_mag_tot, rep = dirr+'/'+G.name, bins=30)
	histo_swap_cul(swap_mag_tot, rep = dirr+'/'+G.name, bins=30, normed=True)
	
	#ratio_vs_nu(n_u_tot, swap_tot, rank=1)
	#ratio_vs_nu(n_u_tot, swap_tot, rank=2)
	#ratio_vs_nu(n_u_tot, swap_tot, rank=3)
	#ratio_vs_static_overlap(static_overlap_tot, swap_tot)
	
	proba_swap(static_overlap_tot, swap_tot, rep= dirr + '/' + G.name, n_quantiles=10)
	swap_mag_vs_static_overlap(static_overlap_tot, swap_mag_tot, rep= dirr + '/' + G.name, n_quantiles=10)
	swap_mag_vs_static_overlap_averaged(static_overlap_tot, swap_mag_tot, rep= dirr + '/' + G.name, n_quantiles=10)

	plt.show()
