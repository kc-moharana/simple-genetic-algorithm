'''
 Implementing Genetic Algorithm 
 -problem:
  Find the individuals with all 1
'''
import sys,os,re
import Operon_OOP
import numpy as np
import matplotlib.pyplot as plt

def main():
 print("#### Genetic Algorithm ####")
 NGEN,NPOP,CHROM_SIZE, MUT_PROB, CROSS_PROB = 10,10,5,0.01,0.5
 pop = Operon_OOP.population(n=NPOP, k= CHROM_SIZE)
 pop.random_populate()
 pop.evaluate()
 pop.view(sort=True)
 top_score_per_gen = np.array([])
 top_score_per_gen = np.append(top_score_per_gen,max(pop.indv_scores))
 plt.figure()
 plt.title('Genetic Algorithm top score per generation')
 plt.xlabel('Generations')
 plt.ylabel('Best Score')
 plt.xlim(0,NGEN)
 
 for gen in range(1,NGEN):
  plt.plot(range(1,len(top_score_per_gen)+1), top_score_per_gen, color='blue', marker='.')
  plt.xlim(1,NGEN)
  plt.pause(0.05)
  new_pop = Operon_OOP.population(n=NPOP, k= CHROM_SIZE)
  for _ in range(NPOP):
   c = pop.select(tournsize=4,k=2)
   offspring = Operon_OOP.cross_over(c[0],c[1],CROSS_PROB)
   c = Operon_OOP.mutate_chromosome(offspring,MUT_PROB)
   new_pop.add_chromosome(c)
  new_pop.evaluate()
  #new_pop.view(sort=True)
  pop = new_pop
  top_score_per_gen = np.append(top_score_per_gen,max(pop.indv_scores))
 print('Best population')
 pop.view(sort=True)
 #pop.view(sort=True,k=1)
 plt.plot(range(1,len(top_score_per_gen)+1), top_score_per_gen, color='blue', marker='.')
 plt.xlim(1,NGEN)
 plt.show()
 #plt.savefig('GA_run_top_score.pdf', figsize=(12,10))

if __name__ == "__main__":
 main()
