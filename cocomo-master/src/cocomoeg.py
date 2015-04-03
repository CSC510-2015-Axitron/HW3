from __future__ import division,print_function
import sys,random
sys.dont_write_bytecode = True

"""

# Test Cases for COCOMO

"""
from cocomo import *


@go
def _complete():
  rseed(1)
  for _ in range(4):
    print(complete(flight))
  print("")
  for _ in range(4):
    print(complete(flight), reduceFunctionality())
    
#@go
#def _sample1():
  #sample(projects=[flight,anything]) 

#Original values for Projects
#flight,ground,osp,osp2,anything 


PROJECTS  = [osp]
TREATMENTS= [doNothing, improvePersonnel, improveToolsTechniquesPlatform,
             improvePrecendentnessDevelopmentFlexibility, 
             increaseArchitecturalAnalysisRiskResolution, relaxSchedule,
             improveProcessMaturity, reduceFunctionality, reduceQuality, improveTeam]

@go
def _efforts():
  sample(projects=PROJECTS)

@go
def _effortsTreated():
  for project in PROJECTS:
    print("\n#### ",project.__name__," ","#"*50,"\n")
    sample(projects=[project],treatments=TREATMENTS)
 
