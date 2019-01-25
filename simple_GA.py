'''
 Object oriented approach
 '''
import sys,os,re
import numpy as np
import operator

class individual:
 '''
  A single individual chromosome
 '''
 
 def __init__(self,genes):
  self.genes = genes
 def evaluate(self):
  self.score = sum(self.genes)

class population:
 '''
  A GA population
 ''' 
 def __init__(self,n,k):
  '''Create a GA population
   n: number chromosomes in population
   k: length of each chromosome
  '''
  self.size = n
  self.indv_len = k
  self.chromosomes = np.array([])
  self.indv_scores = np.zeros(n)
 def isPopulated(self):
  ''' logical check '''
  if  len(self.chromosomes):
   return True
  else:
   return False

 def random_populate(self):
  ''' Populate with random 0,1 bits '''
  if self.isPopulated():
   print("Already populated!!!",file=sys.stderr)
   return(False)
  for i in range(self.size):
   genes = np.random.choice([0,1],size=self.indv_len)
   indv = individual(genes=genes)
   self.chromosomes=np.append(self.chromosomes,indv)
  return(True)
 def add_chromosome(self,c):
  ''' add a chromosome to the population '''
  try:
   assert isinstance(c,individual)
  except AssertionError:
   print('Object passed is not an individual object instance!!')
   return(False)
  if len(self.chromosomes)<= self.size:
   self.chromosomes=np.append(self.chromosomes,c)
   return(True)
  else:
   print('Population is already full!!')
   return(False)

 def evaluate(self):
  ''' evaluate all chromosomes '''
  if self.isPopulated():
   for i in range(self.size):
    self.chromosomes[i].evaluate()
    self.indv_scores[i] = self.chromosomes[i].score

 def select(self,tournsize,k):
  ''' Select high scoring chromosome 
   tournament selection method
   @tournsize: tournament size
   @k: no of chromosome
  '''
  choosen =[]
  s_indv = self.chromosomes[np.argsort(self.indv_scores,axis=None)]  
  for _ in range(k):
   aspirants  = np.random.choice(s_indv,size=tournsize)
   s = np.argsort(np.array([a.score for a in aspirants]))
   choosen.append(aspirants[s][-1])
  return(choosen)
  
 def view(self, sort=False,k=None, file_handle=sys.stderr):
  if not self.isPopulated():
   print("Population is empty!!",file=sys.stderr)
   return(False)
  if k == None:
   k = self.size
  print("#ID\tCHRM\tSCORE\n--\t----\t------",file=file_handle)
  if sort:
   s_idx = np.argsort(self.indv_scores,axis=None)
   s_indv = self.chromosomes[s_idx]
   for i in range(k):
    print("%d\t"%s_idx[i]+"|".join([str(k) for k in s_indv[i].genes])+"\t%0.2f"%s_indv[i].score,file=file_handle)
  else:
   for i in range(k):
    print("%d\t"%i,end="",file=file_handle)
    print("|".join([str(k) for k in self.chromosomes[i].genes]),end="\t",file=file_handle)
    print("%0.2f"%self.chromosomes[i].score,file=file_handle)

#==============================================================================#
# Operators
#==============================================================================#
def mutate_chromosome(c,p):
 try:
  assert isinstance(c,individual)
 except AssertionError:
  print('Object passed is not an individual object instance!!')
  return(False)
 assert p <=1
 if np.random.random(size=1)[0] > p:
  return(c)
 point = np.random.randint(0,len(c.genes))
 if c.genes[point]:
  c.genes[point] = 0
 else:
  c.genes[point] = 1
 return(c)
 
def cross_over(parent1,parent2,p):
 try:
  assert isinstance(parent1,individual)
  assert isinstance(parent2,individual)
 except AssertionError:
  print('Object passed is not an individual object instance!!')
  return(False)
 assert p <=1
 if np.random.random(size=1)[0] > p:
  return(parent1)
 point = np.random.randint(0,len(parent1.genes))
 offspring = individual(genes=np.empty(len(parent1.genes), dtype=int))
 offspring.genes[:point] = parent1.genes[:point]
 offspring.genes[point:] = parent2.genes[point:] 
 return(offspring)
