#!/usr/bin/env python3

from perfTabs import *
#from perfTabs import PerformanceTableau, PartialPerformanceTableau
from outrankingDigraphs import BipolarOutrankingDigraph

def fwrite(string, file):
  with open(file, 'w') as f:
    f.write(string)

def main():

  pt = XMCDA2PerformanceTableau('project_2')
  
  print('----------------------------------------------------------------------------------------')
  print('Performance Tableau')
  print('----------------------------------------------------------------------------------------')
  pt.showPerformanceTableau()
  print('')

  print('----------------------------------------------------------------------------------------')
  print('Criteria')
  print('----------------------------------------------------------------------------------------')
  pt.showCriteria()
  print('')


  print('----------------------------------------------------------------------------------------')
  print('Actions')
  print('----------------------------------------------------------------------------------------')
  pt.showActions()
  print('')

  print('----------------------------------------------------------------------------------------')
  print('Statistics')
  print('----------------------------------------------------------------------------------------')
  pt.showStatistics()
  print('')

  html_heatmap = pt.htmlPerformanceHeatmap()
  fwrite(html_heatmap, "full_heatmap.html")

  print('----------------------------------------------------------------------------------------')
  print('RUBIS Best Choice Recommendation from a global multi-objectives compromise point of view')
  print('----------------------------------------------------------------------------------------')
  full_digraph = BipolarOutrankingDigraph(pt)
  full_digraph.showRubisBestChoiceRecommendation()
  print('')

  print('----------------------------------------------------------------------------------------')
  print('Strict Best Choice Recommendation from a global multi-objectives compromise point of view')
  print('----------------------------------------------------------------------------------------')
  codual_full_digraph = ~(-full_digraph) 
  codual_full_digraph.showRubisBestChoiceRecommendation()
  print('')

  partial_digraphs = {}

  for ct in ['Eco', 'Soc', 'Env']:

    print('----------------------------------------------------------------------------------------')
    print('RUBIS Best Choice Recommendation from {} point of view'.format(ct))
    print('----------------------------------------------------------------------------------------')

    #Split to partial performance tableau containing only chosen criteria 
    criterias = [c for c, val in pt.criteria.items() if ct in val['name']]
    ppt = PartialPerformanceTableau(pt,criteriaSubset=criterias)
    
    html_heatmap = ppt.htmlPerformanceHeatmap()
    fwrite(html_heatmap, ct+"_heatmap.html")
    partial_digraph = BipolarOutrankingDigraph(ppt)

    condorcet_winners = partial_digraph.condorcetWinners()
    print("Condorcet winners for {} -> {}".format(ct, condorcet_winners))

    partial_digraph.showRubisBestChoiceRecommendation()

    print('')

if __name__ == '__main__':
    main()