#!/usr/bin/env python3

import os
from perfTabs import *
from weakOrders import RankingByChoosingDigraph
from outrankingDigraphs import BipolarOutrankingDigraph

make_path = lambda x: os.path.join('..', 'report', 'figures', x.lower())
printline = lambda : print(80 * '-')

def fwrite(string, file):
  with open(file, 'w') as f:
    f.write(string)

pt = XMCDA2PerformanceTableau('project_2')

printline()
print('Performance Tableau')
printline()
pt.showPerformanceTableau()
print('')

printline()
print('Criteria')
printline()
pt.showCriteria()
print('')

printline()
print('Actions')
printline()
pt.showActions()
print('')

printline()
print('Statistics')
printline()
pt.showStatistics()
print('')

full_digraph = BipolarOutrankingDigraph(pt)

html_heatmap = pt.htmlPerformanceHeatmap()
fwrite(html_heatmap, make_path("full_heatmap.html"))

html_relationtable = full_digraph.htmlRelationTable(isColored=True)
fwrite(html_relationtable, make_path("full_bipolar_adj_matrix.html"))

weak_condorcet_winners = full_digraph.weakCondorcetWinners()
printline()
print("Weak Condorcet winners from a multi-objectives point of view -> {}".format(weak_condorcet_winners))
printline()

condorcet_winners = full_digraph.condorcetWinners()
printline()
print("Condorcet winners from a multi-objectives point of view -> {}".format(condorcet_winners))
printline()

printline()
print('RUBIS Best Choice Recommendation from a global multi-objectives compromise point of view')
printline()
full_digraph.showRubisBestChoiceRecommendation()
print('')

printline()
print('Strict Best Choice Recommendation from a global multi-objectives compromise point of view')
printline()
codual_full_digraph = ~(-full_digraph) 
codual_full_digraph.showRubisBestChoiceRecommendation()
print('')

printline()
print('Weakly ordering from a global multi-objectives compromise point of view')
rbc = RankingByChoosingDigraph(codual_full_digraph)
rbc.showRankingByChoosing()
rbc.exportGraphViz(make_path("weak_ordering"))
