# encoding: shift_jis
#!/usr/bin/env python

#多項分布の確率を読み込んでカラーマップで表示するプログラム

#読み込むデータを指定
#場所の名前の音節列を読み込む→音素列に変換（単語辞書登録プログラムを一部流用）
#Wを読み込む→カラーマップで描画（縦軸が名前、横軸がindexCt）
#Φを読み込む→カラーマップで描画（縦軸がindexIt、横軸がindexCt）

###場所概念Ctはデータが語った番号だけにする
#Ctの結果を読み込み

#from pylab import *
import matplotlib.pyplot as plt
import numpy as np
import sys
from matplotlib.colors import LogNorm
import collections
from __init__ import *


#itとCtのデータを読み込む（教示した時刻のみ）
def ReaditCtData(trialname, cstep, particle):
  CT,IT = [0 for i in xrange(step)],[0 for i in xrange(step)]
  i = 0
  if (step != 0):  #最初のステップ以外
    for line in open( datafolder + trialname + "/" + str(cstep) + "/particle" + str(particle) + ".csv" , 'r' ):
      itemList = line[:-1].split(',')
      CT[i] = int(itemList[7]) 
      IT[i] = int(itemList[8]) 
      i += 1
  return CT, IT

# Reading particle data (ID,x,y,theta,weight,previousID)
def ReadParticleData2(step, particle, trialname):
  p = []
  for line in open ( datafolder + trialname + "/"+ str(step) + "/particle" + str(particle) + ".csv" ):
    itemList = line[:-1].split(',')
    p.append( [float(itemList[2]), float(itemList[3])] )
    #p.append( Particle( int(itemList[0]), float(itemList[1]), float(itemList[2]), float(itemList[3]), float(itemList[4]), int(itemList[5])) )
  return p


##学習データファイルから単語の読み込み

#ファイル名を要求
trialname = raw_input("dataname?>")
step = 50
iteration = step #int(raw_input("iteration_num?[1~10]>"))
#sample = int(raw_input("saple_num?[0~5]>"))
filename = datafolder + trialname + "/" + str(step)  ##FullPath of learning trial folder

iteration = iteration - 1
#w_indexの2行目を読み込む
W_index= []
W_index_p = []

i = 0
#重みファイルを読み込み
for line in open(datafolder + trialname + '/'+ str(step) + '/weights.csv', 'r'):   ##読み込む
        #itemList = line[:-1].split(',')
        if (i == 0):
          MAX_Samp = int(line)
        i += 1

#最大尤度のパーティクル番号を保存
particle = MAX_Samp

i = 0
#テキストファイルを読み込み
for line in open(datafolder + trialname + '/'+ str(step) + '/W_list' + str(particle) + '.csv', 'r'):   ##*_samp.100を順番に読み込む
        itemList = line[:-1].split(',')
        
        if(i == 0):
            for j in range(len(itemList)):
              if (itemList[j] != ""):
                W_index = W_index + [itemList[j]]
        i = i + 1
print W_index


LIST = []
hatsuon = [ "" for i in xrange(len(W_index)) ]
TANGO = []
##単語辞書の読み込み
for line in open("./lang_m/web.000.htkdic", 'r'):
      itemList = line[:-1].split('	')
      LIST = LIST + [line]
      for j in xrange(len(itemList)):
          itemList[j] = itemList[j].replace("[", "")
          itemList[j] = itemList[j].replace("]", "")
      
      TANGO = TANGO + [[itemList[1],itemList[2]]]
      



##W_indexの単語を順番に処理していく
for c in xrange(len(W_index)):   
          W_index_sj = unicode(W_index[c], encoding='shift_jis')
          #if len(W_index_sj) != 1:  ##１文字は除外
          for moji in xrange(len(W_index_sj)):
              #print len(W_index_sj),str(W_index[i]),W_index_sj[moji]#,len(unicode(W_index[i], encoding='shift_jis'))
              for j in xrange(len(TANGO)):
                #print TANGO[j],j
                ##文字が最後でないとき and 次の文字が小文字のとき
                if (len(W_index_sj)-1 != moji) and (W_index_sj[moji+1] == u'ぁ' or W_index_sj[moji+1] == u'ぃ' or W_index_sj[moji+1] == u'ぅ' or W_index_sj[moji+1] == u'ぇ' or W_index_sj[moji+1] == u'ぉ' or W_index_sj[moji+1] == u'ゃ' or W_index_sj[moji+1] == u'ゅ' or W_index_sj[moji+1] == u'ょ'):   ##次の文字をみる
                    #print moji,W_index_sj[moji+1]
                    if (unicode(TANGO[j][0], encoding='shift_jis') == W_index_sj[moji]+W_index_sj[moji+1]):
                      print moji,j,TANGO[j][0]
                      hatsuon[c] = hatsuon[c] + TANGO[j][1]# + " "
                #文字が小文字のとき（そもそも存在しないため実行されない：消してもよい仕様）
                elif(W_index_sj[moji] == u'ぁ' or W_index_sj[moji] == u'ぃ' or W_index_sj[moji] == u'ぅ' or W_index_sj[moji] == u'ぇ' or W_index_sj[moji] == u'ぉ' or W_index_sj[moji] == u'ゃ' or W_index_sj[moji] == u'ゅ' or W_index_sj[moji] == u'ょ'):
                  if (unicode(TANGO[j][0], encoding='shift_jis') == W_index_sj[moji]):
                    print W_index[c][moji] + " (komoji)"
                else:  ##文字が小文字でないとき and (文字が最後のとき or 次の文字が小文字でないとき)
                  #print moji , len(W_index_sj)-1,i
                  if (unicode(TANGO[j][0], encoding='shift_jis') == W_index_sj[moji]):
                      print moji,j,TANGO[j][0]
                      hatsuon[c] = hatsuon[c] + TANGO[j][1]
          print hatsuon[c]
          W_index_p = W_index_p + [hatsuon[c]]
          #else:
          #  print W_index[c] + " (one name)"
        


##各場所の名前の単語ごとに
#meishi = meishi.encode('shift-jis')

#Ct = []
##Ctの読み込み
Ct,It = ReaditCtData(trialname, step, particle)
#for line in open('./data/' + filename +'/' + filename + '_Ct_'+str(iteration+1) + "_" + str(sample) + '.csv', 'r'):
#   itemList = line[:-1].split(',')
#   
#   for i in xrange(len(itemList)):
#      if itemList[i] != '':
#        if Ct.count(int(itemList[i])) == 0:
#          Ct = Ct + [int(itemList[i])]

#######
N = len(W_index_p)
L = len(collections.Counter(Ct))  #max(Ct)


##Wの読み込み
W = np.array([[0.0 for j in range(L)] for i in range(len(W_index_p))])
c = 0
j = 0
#テキストファイルを読み込み
for line in open(datafolder + trialname + '/'+ str(step) + '/W' + str(particle) + '.csv', 'r'):
        #if Ct.count(j) >= 1:
        itemList = line[:-1].split(',')
        #print c
        #W_index = W_index + [itemList]
        for i in xrange(len(itemList)):
            if itemList[i] != '':
              #print c,i,itemList[i]
              W[i][c] = float(itemList[i])
              if (W[i][c] >= 0.2):
                print W[i][c]
              #print itemList
        c = c + 1
        #j = j + 1
    












plt.subplots_adjust(left=0.60, bottom=0.1, right=0.85, top=0.9800, wspace=None, hspace=None)


#print C1550
plt.xlim([0,L]);
plt.ylim([N,0]);

ind = np.arange(L) # the x locations for the groups 
yyy = np.arange(len(W_index_p))
width = 0.50
X_ct = [i for i in range(L)]
Ct.sort()
plt.xticks(ind+width,([i for i in range(L)]), fontsize=8)#
plt.yticks(yyy+width, (W_index_p),fontsize=8)#, fontname='serif'6
MAX = max([max(W[i]) for i in range(len(W))])
c = plt.pcolor(W,cmap=plt.cm.hot,vmin=0.0,vmax=MAX) #0.5) #gray
#title('')
#xlabel('Location Concepts ID', fontsize=24)
####plt.xlabel('$C_t$', fontsize=10)
#plt.ylabel('word', fontsize=20)

cbar=plt.colorbar(pad=0.08,shrink=0.25,aspect=14,ticks=[0.1*i for i in range(int(MAX*10)+1)])
#cbar.set_label('Frequency of estimated index number',fontsize=32)
cbar.ax.tick_params(labelsize=6)

plt.savefig(datafolder + trialname + '/'+'gs_W_'+ str(step) + '.eps', dpi=300, transparent=True)
plt.savefig(datafolder + trialname + '/'+'gs_W_'+ str(step) + '.png', dpi=300, transparent=True)
plt.show()
