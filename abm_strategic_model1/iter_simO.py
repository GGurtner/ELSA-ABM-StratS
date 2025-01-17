#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
===========================================================================
This is the main interface to the model. The main functions are 
 - average_sim, which makes several iterations of the model with the same
parameters, 
 - iter_sim, which makes iterations of average_sim over several values of 
 parameters. 

 How to use:
 ./iter_simO.py paras_iter.py
===========================================================================
"""

import sys
sys.path.insert(1,'..')

from os.path import join as jn
import pickle
import os
from string import split
import numpy as np
from multiprocessing import Process, Pipe
from itertools import izip
from time import time, gmtime, strftime

from simAirSpaceO import Net
from simulationO import do_standard, build_path as build_path_single #post_process_queue, extract_aggregate_values_on_queue, extract_aggregate_values_on_network
from utilities import read_paras_iter
from prepare_network import soft_infrastructure

from libs.general_tools import yes
from libs.paths import result_dir

version = '3.1.1'
main_version = split(version,'.')[0] + '.' + split(version,'.')[1]

# This is for parallel computation.
def spawn(f):
    def fun(pipe, x):
        pipe.send(f(x))
        pipe.close()
    return fun

def parmap(f, X):
    pipe = [Pipe() for x in X]
    proc = [Process(target=spawn(f), args=(c,x)) for x, (p,c) in izip(X,pipe)]
    [p.start() for p in proc]
    [p.join() for p in proc]
    return [p.recv() for (p,c) in pipe]

#--------------------------------------------------------#

def header(paras, paras_to_display=['departure_times','par','nA', 'ACtot', 'density','Delta_t','ACsperwave']):
    """
    Show the main parameters in the console.
    """
    if paras_to_display==[]:
        paras_to_display=paras.keys()
        
    for p in paras['paras_to_loop']:
        try:
            paras_to_display.remove(p)
        except:
            pass
        
    first_line='------------------------ Program iter_sim version ' + version + ' ------------------------'
    l=len(first_line)
    trait='-'*l
    
    head=trait + '\n' + first_line + '\n' + trait + '\n'
    head+='Network: ' + paras['G'].name + ' ; '
    head+='Paras to loop on: ' + str(paras['paras_to_loop']) + ' ;\n'
    line=''
    for k in paras_to_display:
        try:
            v=paras[k]
            pouic=k + ': ' + str(v) +  ' ; '
            if len(line) < l - len(pouic):
                line = line + pouic
            else:
                head = head + line + '\n' 
                line=pouic
        except:
            pass
    head +=line + '\n' + trait +'\n'
    head += 'Started on ' + strftime("%a, %d %b %Y %H:%M:%S", gmtime()) + '\n'
    head += trait + '\n'
    return head

def build_path_average(paras, vers=main_version, in_title=['tau', 'par', 'ACtot', 'nA'], Gname=None, rep=result_dir):
    """
    Build the path for results.
    """

    #if Gname==None:
    #    Gname = paras['G'].name
    
    #rep = jn(rep, Gname)
    
    return build_path_single(paras, vers=vers, rep=rep, name_G=Gname) + '_iter' + str(paras['n_iter']) + '.pic'

def aggregate_results(results_list):
    results = {}
    for met in results_list[0].keys():
        if type(results_list[0][met])==type(np.float64(1.0)):
            results[met] = {'avg':np.mean([v[met] for v in results_list]), 'std':np.std([v[met] for v in results_list])}
        elif type(results_list[0][met])==type({}):
            results[met] = {tuple(p):[] for p in results_list[0][met].keys()}
            for company in results_list[0][met].keys():
                results[met][company] = {'avg':np.mean([v[met][company] for v in results_list]), 'std':np.std([v[met][company] for v in results_list])}
    return results

def average(args_do=None, save=1, do=None, build_pat=None, args_pat=None,\
    kwargs_pat={}, rep=None, aggregator=None, verbose=True, force=False, parallel=False,\
    n_iter=2):
    """
    More general function than average_sim.
    """
    #rep = build_pat(paras, Gname=G.name, rep=rep)
    rep = build_pat(*args_pat, **kwargs_pat)
    if force or not os.path.exists(rep):
        inputs = [args_do for i in range(n_iter)]
        start_time = time()
        if parallel:
            if verbose:
                print 'Doing', len(inputs), 'iterations in parallel...',
            results_list = parmap(do, inputs)
        else:
            if verbose:
                print 'Doing', len(inputs), 'iterations sequentially...',
            results_list = []
            for i, a in enumerate(inputs):
                #sys.stdout.write('\r' + 'Doing simulations...' + str(int(100*(i+1)/float(paras['n_iter']))) + '%')
                #sys.stdout.flush() 
                results_list.append(do(a))
            
        if verbose:
            print ' done in', time()-start_time, 's'
            print
        
        results = aggregator(results_list)
                    
        if save>0:
            os.system('mkdir -p ' + os.path.dirname(rep))
            with open(rep, 'w') as f:
                pickle.dump(results, f)
    else:
        if verbose:
            print 'Skipped this value because the file already exists and parameter force is deactivated.'

def average_sim2(paras=None, G=None, save=1, do=do_standard, build_pat=build_path_average, rep=result_dir,\
    aggregator=aggregate_results, verbose=True):

    average(args_do=(paras, G), save=save, do=do, build_pat=build_pat, args_pat=(paras),\
    kwargs_pat={'Gname':G.name, 'rep':rep}, rep=rep, aggregator=aggregator, verbose=verbose,\
    force=paras['force'], parallel=paras['parallel'], n_iter=paras['n_iter'])

def average_sim(paras=None, G=None, save=1, do=do_standard, build_pat=build_path_average, rep=result_dir,\
    aggregator=aggregate_results, verbose=True, max_parallel_computation=100):
    """
    Average some simulations which have the same paras.
    
    Notes
    -----
    Changed in 3.0.0: taken from Model 2 (unchanged).

    (From Model 2)
    New in 2.6: makes a certain number of iterations (given in paras) and extract the averaged mettrics.
    Change in 2.7: parallelized.
    Changed in 2.9.1: added force.
    Changed in 2.9.2: added do and build_pat kwargs. 
    Changed in 2.9.4: removed integer i in the call of do_standard. Updated build_pat output.
    
    """
    rep = build_pat(paras, Gname=G.name, rep=rep)
    if paras['force'] or not os.path.exists(rep): 
        inputs = [(paras, G) for i in range(paras['n_iter'])]
        start_time = time()
        if paras['parallel']:
            if verbose:
                print 'Doing', len(inputs), 'iterations in parallel...',
            if len(inputs)<=max_parallel_computation:
                results_list = parmap(do, inputs)
            else:
                print '(with splitted lists)...',
                splitlists = [inputs[i:i+max_parallel_computation] for i in range(0, len(inputs), max_parallel_computation)]
                results_list = []
                for inpt in splitlists:
                    results_list += parmap(do, inpt)
        else:
            if verbose:
                print 'Doing', len(inputs), 'iterations sequentially...',
            results_list = []
            for i, a in enumerate(inputs):
                #sys.stdout.write('\r' + 'Doing simulations...' + str(int(100*(i+1)/float(paras['n_iter']))) + '%')
                #sys.stdout.flush() 
                results_list.append(do(a))
            
        if verbose:
            print ' done in', time()-start_time, 's'
            print
        results = aggregator(results_list)
                    
        if save>0:
            os.system('mkdir -p ' + os.path.dirname(rep))
            with open(rep, 'w') as f:
                pickle.dump(results, f)
    else:
        if verbose:
            print 'Skipped this value because the file already exists and parameter force is deactivated.'

def loop(a, level, parass, results={}, thing_to_do=None, tot_lvl=0, show_detailed_evo=False, it=0, **args):
    """
    Generic recursive function to make several levels of iterations.
   
    Parameters
    ----------
    a : dictionnary, 
        with keys as parameters to loop on and values as the values on which to loop.
    level: list,
        of parameters on which to loop. The first one is the most outer loop, the last
        one is the most inner loop.
    results: dict,
        recursive dictionnary with all results.
    thing_to_do: function,
        function to call with args *args at the bottom of the recursion.
    tot_lvl: int, optional
        Informational only. Should be the total number of levels. Passed unchanged.
    show_detailed_evo:boolean,
        if True, prints the value of parameters for each loop. Otherwise, prints
        aggregated information
    it: int,
        used to count the total number of loopts (unfolded).
    
    Notes
    -----
    New in 2.6: Makes an arbitrary number of loops
    Changed in 3.0.0: added gather option
    Changed in 3.1.1: added automatic gathering of results with a dictionnary

    """

    all_stuff = []
    if level==[]:
        if not show_detailed_evo:
            #sys.stdout.write('\r' + 'Doing simulations...' + str(int(100*(it+1)/float(args['paras']['n_iter_tot']))) + '%')
            sys.stdout.write('\r' + 'Doing simulations...' + str(int(100*(it+1)/float(parass.get('n_iter_tot', 1.)))) + '%')
            sys.stdout.flush() 
            it += 1
        return it, thing_to_do(verbose=show_detailed_evo, **args)
    else:
        assert level[0] in a.keys()
        for i in a[level[0]]:
            n_dashes = max(0, tot_lvl - len(level)+1)
            if show_detailed_evo:
                print n_dashes*'-', level[0], '=', i
            parass.update(level[0],i)
            it, results[i] = loop(a, level[1:], parass, results={}, thing_to_do=thing_to_do, tot_lvl=tot_lvl, it=it,\
                                             show_detailed_evo=show_detailed_evo, **args)
        return it, results
    
def iter_sim(paras, save=1, do=do_standard, build_pat=build_path_average, rep=result_dir):#, make_plots=True):#la variabile test_airports è stata inserita al solo scopo di testare le rejections
    """
    Used to loop and average the simulation. G can be passed in paras if fixnetwork is True.
    save can be 0 (no save), 1 (save agregated values) or 2 (save all queues).

    Notes
    -----
    Changed in 3.0.0: taken from Model 2 (unchanged).

    (From Model 2)
    Changed in 2.9.2: added do and build_pat kwargs.
    
    """

    # Used for debugging.
    # if 0:
    #     with open('state.pic','w') as f:
    #         pickle.dump(getstate(),f)
    # else:
    #     with open('state.pic','r') as f:
    #         setstate(pickle.load(f))
    
    print header(paras)

    # Compute number of iterations
    n_iter_tot = np.prod([len(paras[p + '_iter']) for p in paras['paras_to_loop']])
    paras['n_iter_tot'] = n_iter_tot
    print "Total number of iterations over the parameters:", n_iter_tot
    
    if paras['fixnetwork']:
        G = paras['G']        
    else:
        G = None
        
    loop({p:paras[p + '_iter'] for p in paras['paras_to_loop']}, paras['paras_to_loop'], \
        paras, tot_lvl=len(paras['paras_to_loop']), thing_to_do=average_sim, paras=paras, \
        G=G, do=do, build_pat=build_pat, save=save, rep=rep, show_detailed_evo=True)

def change_airports((G, paras_G), change_name_G=True):
    """
    Used to generate networks with different soft infrastructure but 
    the same hard infrastructure.
    """

    save_name = G.name_generic + '_nairports' + str(paras_G['nairports_sec']) + '_' + str(paras_G['I_iter'])
    path_save = jn(G.rep, save_name) + '.pic'

    if paras_G['force'] or not os.path.exists(path_save):  
        soft_infrastructure(G, paras_G)
        
        if change_name_G:
            G.name = save_name

        # Save 
        with open(path_save,'w') as f:
            pickle.dump(G, f)
    else:
        print 'Skipped this value because the file already exists and parameter force is deactivated.'

    return path_save

def iter_airport_change(paras, G, do=change_airports):
    """

    Notes
    -----
    New in 3.0.0
    
    """        
    G.name_generic = G.name

    it, files = loop({p:paras[p + '_iter'] for p in paras['paras_to_loop']}, paras['paras_to_loop'], \
        paras, thing_to_do=produce_several_airports, paras=paras, do=do, G=G, show_detailed_evo=True)

    with open(jn(G.rep, 'list_of_files.pic'), 'w') as f:
        pickle.dump(list(np.array(files.values()).flatten()), f)

    print "Lisf of files of network saved as", jn(G.rep, 'list_of_files.pic')

def produce_several_airports(paras, do=change_airports, G=None, verbose=True):
    """
    Used to produce several versions of a network (draw the airports at random at each iteration).
    paras is fixed here.

    Notes
    -----
    New in 3.0.0

    """

    inputs = []
    print 'G.name_generic', G.name_generic
    for i in range(paras['n_iter']):
        paras['I_iter'] = i
        inputs.append((G, paras.copy()))

    start_time = time()
    files = []
    if paras['parallel']:
        parmap(do, inputs)
    else:
        print 'Doing', len(inputs), 'iterations...'
        for i, a in enumerate(inputs):
            #sys.stdout.write('\r' + 'Doing simulations...' + str(int(100*(i+1)/float(paras['n_iter']))) + '%')
            #sys.stdout.flush() 
            fil = do(a)
            files.append(fil)
        
    print '... done in', time()-start_time, 's'
    return files

if __name__=='__main__':
    """
    Manual entry
    """
    paras_file = None if len(sys.argv)==1 else sys.argv[1]
    paras = read_paras_iter(paras_file=paras_file)

    if yes('Ready?'):
        results = iter_sim(paras, save=1)
    
    print 'Done.'
    
