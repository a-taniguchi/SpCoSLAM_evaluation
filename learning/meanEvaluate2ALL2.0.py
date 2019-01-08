#c-od-i-n-:-ut-f---8
#!/usr/bin/env python
#PAR_w_MI ga PARs tosite hozon sareteita mono wo syuusei.->2.0
#Akira Taniguchi 
#-2018/01/25-2018/02/22
import sys
import string
#from sklearn.metrics.cluster import adjusted_rand_score
#import matplotlib.pyplot as plt
import numpy as np
#import math
from __init__ import *

trialname = raw_input("data_name?(**NUM) > ")
data_num1 = raw_input("data_start_num?(DATA***) > ")
data_num2 = raw_input("data_end_num?(DATA***) > ")
N = int(data_num2) - int(data_num1) +1
#filename = raw_input("Read_Ct_filename?(.csv) >")"001"#"010"#
S = int(data_num1)

step = 50
#N = step

ARIc_M = [[] for c in xrange(N)]
ARIi_M = [[] for c in xrange(N)]
NMIc_M = [[] for c in xrange(N)]
NMIi_M = [[] for c in xrange(N)]
PARs_M = [[] for c in xrange(N)]
PARw_M = [[] for c in xrange(N)]
L_M = [[] for c in xrange(N)]
K_M = [[] for c in xrange(N)]
ESEG_M = [[] for c in xrange(N)]
PARss_M = [[] for c in xrange(N)]
#K_M = [[] for c in xrange(N)]
#MM = [ np.array([[] for m in xrange(10) ]) for n in xrange(N)]
#MM_M = 

fp = open(datafolder + '/Evaluation/' + trialname + '_' + data_num1 + '_' + data_num2 + '_Evaluation2ALL2.0.csv', 'w')
fp.write('ARIc,ARIi,NMIc,NMIi,PARwMI,PARw,L,K,ESEG,PARs\n')

i = 0

for s in range(N):
  i = 0
  for line in open(datafolder + trialname + str(s+1).zfill(3) + '/' + trialname + str(s+1).zfill(3) +'_meanEvaluation2ALL.csv', 'r'): #ALL
    itemList = line[:-1].split(',')
    if (i != 0) and (itemList[0] != '') and (i <= step):
      #print i,itemList
      ARIc_M[s] = ARIc_M[s] + [float(itemList[0])]
      ARIi_M[s] = ARIi_M[s] + [float(itemList[1])]
      NMIc_M[s] = NMIc_M[s] + [float(itemList[2])]
      NMIi_M[s] = NMIi_M[s] + [float(itemList[3])]
      PARs_M[s] = PARs_M[s] + [float(itemList[4])]
      PARw_M[s] = PARw_M[s] + [float(itemList[5])]
      L_M[s] = L_M[s] + [float(itemList[6])]
      K_M[s] = K_M[s] + [float(itemList[7])]
      ESEG_M[s] = ESEG_M[s] + [float(itemList[9])]
      PARss_M[s] = PARss_M[s] + [float(itemList[10])]
      #if (float(itemList[0]) > NMIc_MAX[0][1]):
      #    NMIc_MAX = [[s+1,float(itemList[0])]] + NMIc_MAX
      #if (float(itemList[1]) > NMIi_MAX[0][1]):
      #    NMIi_MAX = [[s+1,float(itemList[1])]] + NMIi_MAX
      #if (float(itemList[3]) > PARw_MAX[0][1]):
      #    PARw_MAX = [[s+1,float(itemList[3])]] + PARw_MAX
    i = i + 1
    
  ARIc_M[s] = np.array(ARIc_M[s])
  ARIi_M[s] = np.array(ARIi_M[s])
  NMIc_M[s] = np.array(NMIc_M[s])
  NMIi_M[s] = np.array(NMIi_M[s])
  PARs_M[s] = np.array(PARs_M[s])
  PARw_M[s] = np.array(PARw_M[s])
  L_M[s] = np.array(L_M[s])
  K_M[s] = np.array(K_M[s])
  ESEG_M[s] = np.array(ESEG_M[s])
  PARss_M[s] = np.array(PARss_M[s])
  print PARw_M[s],N,len(PARw_M),len(PARw_M[s])

ARIc_MM = sum(ARIc_M)/float(N)
ARIi_MM = sum(ARIi_M)/float(N)
NMIc_MM = sum(NMIc_M)/float(N)
NMIi_MM = sum(NMIi_M)/float(N)
PARw_MM = sum(PARw_M)/float(N)
PARs_MM = sum(PARs_M)/float(N)
L_MM = sum(L_M)/float(N)
K_MM = sum(K_M)/float(N)
ESEG_MM = sum(ESEG_M)/float(N)
PARss_MM = sum(PARss_M)/float(N)
#print NMIc_MM
#MI,NMIi,PARs,PARw,

for iteration in xrange(len(NMIc_MM)):
  fp.write( str(ARIc_MM[iteration])+','+ str(ARIi_MM[iteration])+','+ str(NMIc_MM[iteration])+','+ str(NMIi_MM[iteration])+','+ str(PARs_MM[iteration])+','+str(PARw_MM[iteration])+ ','+str(L_MM[iteration])+','+ str(K_MM[iteration])+','+str(ESEG_MM[iteration])+','+ str(PARss_MM[iteration]) )
  fp.write('\n')
fp.write('\n')


for iteration in xrange(len(NMIc_MM)):
  ARIc_MS = np.array([ARIc_M[s][iteration] for s in xrange(N)])
  ARIi_MS = np.array([ARIi_M[s][iteration] for s in xrange(N)])
  NMIc_MS = np.array([NMIc_M[s][iteration] for s in xrange(N)])
  NMIi_MS = np.array([NMIi_M[s][iteration] for s in xrange(N)])
  PARs_MS = np.array([PARs_M[s][iteration] for s in xrange(N)])
  PARw_MS = np.array([PARw_M[s][iteration] for s in xrange(N)])
  L_MS = np.array([L_M[s][iteration] for s in xrange(N)])
  K_MS = np.array([K_M[s][iteration] for s in xrange(N)])
  ESEG_MS = np.array([ESEG_M[s][iteration] for s in xrange(N)])
  PARss_MS = np.array([PARss_M[s][iteration] for s in xrange(N)])
  #print iteration,np.std(NMIc_MS, ddof=1)
  fp.write( str(np.std(ARIc_MS, ddof=1))+','+ str(np.std(ARIi_MS, ddof=1))+','+ str(np.std(NMIc_MS, ddof=1))+','+ str(np.std(NMIi_MS, ddof=1))+','+ str(np.std(PARs_MS, ddof=1))+','+str(np.std(PARw_MS, ddof=1)) +','+str(np.std(L_MS, ddof=1)) +','+str(np.std(K_MS, ddof=1)) +','+str(np.std(ESEG_MS, ddof=1))+','+ str(np.std(PARss_MS, ddof=1)) )
  fp.write('\n')
print "close."
fp.close()
