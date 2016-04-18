#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 14:38:09 2012

@author: luca
"""

from simulationO import Simulation, build_path as build_path_single, post_process_queue, extract_aggregate_values_on_queue, extract_aggregate_values_on_network
#from random import getstate, setstate, gauss
import pickle
import ABMvars
import os
#from plots import Plot
from string import split
import numpy as np
import sys
#from multiprocessing import Pool

from multiprocessing import Process, Pipe
from itertools import izip
from time import time

def yes(question):
    ans=''
    while not ans in ['Y','y','yes','Yes','N','n','No','no']:
        ans=raw_input(question + ' (y/n)\n')
    return ans in ['Y','y','yes','Yes']

def spawn(f):
    def fun(pipe,x):
        pipe.send(f(x))
        pipe.close()
    return fun

def parmap(f,X):
    pipe=[Pipe() for x in X]
    proc=[Process(target=spawn(f),args=(c,x)) for x,(p,c) in izip(X,pipe)]
    [p.start() for p in proc]
    [p.join() for p in proc]
    return [p.recv() for (p,c) in pipe]

version='2.6.6'
main_version=split(version,'.')[0] + '.' + split(version,'.')[1]

#def build_path(paras, vers=version[:3], in_title=['tau', 'par', 'ACtot', 'nA']):
#    """
#    Used to build a path from a set of paras. 
#    New in 2.2.
#    """
#    loop_on=paras['para_iter']
#    name=build_path_single(paras, vers=vers, in_title=[p for p in in_title if p!=loop_on])
##    if loop_on=='AC' and type(paras['AC_iter'][0])!=type(1):
##        name+= '_loop_on_' + 'nA'
##    else:
#    name+='_loop_on_' + loop_on
#
#        
#    name+= '_iter'+ str(paras['n_iter'])
#        
#    return name
    
def build_path_average(paras, vers=main_version, in_title=['tau', 'par', 'ACtot', 'nA'], Gname=None):
    if Gname==None:
        Gname=paras['G'].name
    
    rep='../results/Sim_v' + main_version + '_' + Gname
    
    #build_path_single(paras) + '_iter' + str(paras['n_iter']) + '.pic'
    
    return rep, '/' + build_path_single(paras, only_name = True) + '_iter' + str(paras['n_iter']) + '.pic'

    
def iter_sim(paras, save=1):#, make_plots=True):#la variabile test_airports è stata inserita al solo scopo di testare le rejections
    """
    Used to loop and average the simulation. G can be passed in paras if fixnetwork is True.
    save can be 0 (no save), 1 (save agregated values) or 2 (save all queues).
    """
   # if 0:
   #     f=open('state.pic','w')
   #     pickle.dump(getstate(),f)
   #     f.close()
   # else:
   #     f=open('state.pic','r')
   #     setstate(pickle.load(f))
   #     f.close()
    
    if paras['fixnetwork']:
        G=paras['G']        
    else:
        G=None
        

    #loop({p:paras[p + '_iter'] for p in paras['paras_to_loop']}, paras['paras_to_loop'], paras, thing_to_do=average_sim, paras=paras, G=G)
    loop({p:paras[p + '_iter'] for p in paras['paras_to_loop']}, paras['paras_to_loop'], paras, thing_to_do=average_sim, paras=paras)
    
def loop(a, level, parass, thing_to_do=None, **args):
    """
    New in 2.6: Makes an arbitrary number of loops
    a: dictionnary, with keys as parameters to loop on and values as the values on which to loop.
    level: list of parameters on which to loop. The first one is the most outer loop, the last one is the most inner loop.
    """
    if level==[]:
        thing_to_do(**args)#(paras, G)
    else:
        assert level[0] in a.keys()
        for i in a[level[0]]:
            print level[0], '=', i
            parass.update(level[0],i)
            loop(a, level[1:], parass, thing_to_do=thing_to_do, **args)
    
def average_sim(paras=None, save=1):#, mets=['satisfaction', 'regulated_F', 'regulated_FPs']):
    """
    New in 2.6: makes a certain number of iterations (given in paras) and extract the averaged mettrics.
    Change in 2.6.?: parallelized.
    Changed in 2.6.6: added force.
    """

    def do((paras, i)):
        results={} 
        #print "I'm doing iteration number ", i
        sim=Simulation(paras, G=paras['G'].copy(), verbose=False)
        sim.make_simu()
        sim.queue=post_process_queue(sim.queue)

        #print 'Number of flights:', len(sim.queue)
        
        results_queue=extract_aggregate_values_on_queue(sim.queue, paras['par'])
        results_G=extract_aggregate_values_on_network(sim.G)

        #print 'res:', results_queue
        
        for met in results_G:
            results[met] = results_G[met]
                
        for met in results_queue:
            results[met]={tuple(p):[] for p in paras['par']}
            for p in paras['par']:
                results[met][tuple(p)] = results_queue[met][tuple(p)]

        del sim
        return results

    rep, name=build_path_average(paras, Gname=paras['G'].name)
    #print "paras['G'].name", paras['G'].name
    #print "rep:", rep

    if paras['force'] or not os.path.exists(rep + name):
        #pool = Pool(processes=2)  
        inputs = [(paras, i) for i in range(paras['n_iter'])]
        start_time=time()
        if paras['parallel']:
            print 'Doing iterations in parallel',
            results_list = parmap(do, inputs)
        else:
            results_list=[]
            for i,a in enumerate(inputs):
                sys.stdout.write('\r' + 'Doing simulations...' + str(int(100*(i+1)/float(paras['n_iter']))) + '%')
                sys.stdout.flush() 
                results_list.append(do(a))
            
            
        print '... done in', time()-start_time, 's'
        
        results={}
        for met in results_list[0].keys():
            if type(results_list[0][met])==type(np.float64(1.0)):
                results[met]={'avg':np.mean([v[met] for v in results_list]), 'std':np.std([v[met] for v in results_list])}
            elif type(results_list[0][met])==type({}):
                results[met]={tuple(p):[] for p in results_list[0][met].keys()}
                for company in results_list[0][met].keys():
                    results[met][company]={'avg':np.mean([v[met][company] for v in results_list]), 'std':np.std([v[met][company] for v in results_list])}
                    
        if save>0:
            os.system('mkdir -p ' + rep)
            with open(rep + name,'w') as f:
                pickle.dump(results, f)
            
    else:
        print 'Skipped this value because the file already exists and parameter force is deactivated.'
                    
    #return results
    
            
if __name__=='__main__':

    if yes('Ready?'):
        results=iter_sim(ABMvars.paras)
    #reduce_results(ABMvars.paras)
    
    print 'Done.'
    
