#!/usr/bin/env python3
import os

from perfTabs import *
#from perfTabs import PerformanceTableau, PartialPerformanceTableau
from outrankingDigraphs import BipolarOutrankingDigraph

make_path = lambda x: os.path.join('..', 'report', x)
printline = lambda : print(80 * '-')

def fwrite(string, file):
  with open(file, 'w') as f:
    f.write(string)

def main():

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

  html_heatmap = pt.htmlPerformanceHeatmap()
  fwrite(html_heatmap, make_path("full_heatmap.html"))

  #Create diGraph for the whole data
  full_digraph = BipolarOutrankingDigraph(pt)

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

  partial_digraphs = {}

  for ct in ['Eco', 'Soc', 'Env']:

    printline()
    print('RUBIS Best Choice Recommendation from {} point of view'.format(ct))
    printline()

    #Split to partial performance tableau containing only chosen criteria 
    criterias = [c for c, val in pt.criteria.items() if ct in val['name']]
    ppt = PartialPerformanceTableau(pt,criteriaSubset=criterias)
    
    html_heatmap = ppt.htmlPerformanceHeatmap(colorLevels=5)

    fwrite(html_heatmap, make_path(ct+"_heatmap.html"))
    partial_digraph = BipolarOutrankingDigraph(ppt)

    condorcet_winners = partial_digraph.condorcetWinners()
    printline()
    print("Condorcet winners for {} -> {}".format(ct, condorcet_winners))
    printline()

    partial_digraph.showRubisBestChoiceRecommendation()

    print('')

if __name__ == '__main__':
    main()