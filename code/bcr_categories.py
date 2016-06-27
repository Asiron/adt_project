#!/usr/bin/env python3

import os
from perfTabs import *
from outrankingDigraphs import BipolarOutrankingDigraph
from weakOrders import RankingByChoosingDigraph

make_path = lambda x: os.path.join('..', 'report', 'figures', x.lower())
printline = lambda : print(80 * '-')

def fwrite(string, file):
    with open(file, 'w') as f:
        f.write(string)

pt = XMCDA2PerformanceTableau('project_2')

for ct in ['Eco', 'Soc', 'Env']:

    printline()
    print('RUBIS Best Choice Recommendation from {} point of view'.format(ct))
    printline()

    criterias = [c for c, val in pt.criteria.items() if ct in val['name']]
    ppt = PartialPerformanceTableau(pt,criteriaSubset=criterias)

    partial_digraph = BipolarOutrankingDigraph(ppt)

    html_heatmap = ppt.htmlPerformanceHeatmap(colorLevels=5)
    fwrite(html_heatmap, make_path(ct+"_heatmap.html"))

    html_relationtable = partial_digraph.htmlRelationTable(isColored=True)
    fwrite(html_relationtable, make_path(ct+"_bipolar_adj_matrix.html"))

    condorcet_winners = partial_digraph.condorcetWinners()
    printline()
    print("Condorcet winners for {} -> {}".format(ct, condorcet_winners))
    printline()

    weak_condorcet_winners = partial_digraph.weakCondorcetWinners()
    printline()
    print("Weak Condorcet winners for {} -> {}".format(ct, weak_condorcet_winners))
    printline()

    partial_digraph.showRubisBestChoiceRecommendation()

    printline()
    print('Weakly ordering for {} point of view'.format(ct))
    printline()

    codual_partial = ~(-partial_digraph)

    rbc = RankingByChoosingDigraph(codual_partial)
    rbc.showRankingByChoosing()
    rbc.exportGraphViz(make_path(ct+"_weak_ordering"))

    printline()
    print("Strict Best choice recommendation from {} point of view".format(ct))
    codual_partial.showRubisBestChoiceRecommendation()
    printline()

    print('')

