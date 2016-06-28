#!/usr/bin/env python3

__author__  = "Maciej Zurad"
__email__   = "maciej.zurad@gmail.com"
__license__ = "GPL"

import os
from perfTabs import *
from outrankingDigraphs import BipolarOutrankingDigraph

make_path = lambda x: os.path.join('..', 'report', 'figures', x.lower())
printline = lambda : print(80 * '-')

pt = XMCDA2PerformanceTableau('project_2')
full_digraph = BipolarOutrankingDigraph(pt)

printline()
print('Ranking')
printline()
print('Transitivity degree {}'.format(full_digraph.computeTransitivityDegree()))
printline()
print('Chorless circuits')
full_digraph.computeChordlessCircuits()
full_digraph.showChordlessCircuits()
printline()
print('')

from linearOrders import CopelandOrder
cop = CopelandOrder(full_digraph)
print('The Copeland ranking')
cop.showRanking()
printline()
cop_corr = full_digraph.computeOrdinalCorrelation(cop)
print("Fitness of Copeland's ranking: %.3f" % cop_corr['correlation'])
printline()
print('')

from linearOrders import NetFlowsOrder
nf = NetFlowsOrder(full_digraph)
print('The Net-Flows ranking')
printline()
print('Net flow values for each alternative')
for n,va in enumerate(nf.netFlows):
  print("{0} {2} -> {1:.2f}".format(n+1, *va))
printline()
nf.showRanking()
nf_corr = full_digraph.computeOrdinalCorrelation(nf)
print("Fitness of Net-flows ranking: %.3f" % nf_corr['correlation'])
printline()
print('')

from linearOrders import KohlerOrder
ko = KohlerOrder(full_digraph)
print('The Kohler ranking')
printline()
ko.showRanking()
ko_corr = full_digraph.computeOrdinalCorrelation(ko)
print("Fitness of Kohler's ranking: %.3f" % ko_corr['correlation'])
printline()
print('')

from linearOrders import RankedPairsOrder
rp = RankedPairsOrder(full_digraph)
print('The Tideman\'s Ranked-Pairs rule ranking')
printline()
rp.showRanking()
rp_corr = full_digraph.computeOrdinalCorrelation(rp)
print("Fitness of Tideman's Ranked-Pairs rule ranking: %.3f" % rp_corr['correlation'])
printline()
print('')

#Sorting 
from sortingDigraphs import QuantilesSortingDigraph
qs = QuantilesSortingDigraph(pt,limitingQuantiles=10)
qs.showSorting()
qs.showQuantileOrdering()
qs.exportGraphViz(make_path("sorted_deciles_graph"))
