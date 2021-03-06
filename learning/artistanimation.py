#coding:utf-8
import glob
import numpy as np
#from numpy.random import multinomial
from scipy.stats import rv_discrete
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
from __init__ import *

trialname = "/home/akira/Dropbox/SpCoSLAM/rosbag/albert-b-laser-vision/albert-B-laser-vision-dataset/"
filelist = glob.glob(trialname+"CNN_Place365/*.csv")
filelist.sort()
Data = len(filelist)
print Data
x = np.arange(DimImg)

s = raw_input("start number?>")
e = raw_input("end number?>")

fig = plt.figure()
#ax = fig.add_subplot(111)

#data = pd.DataFrame(data=0., index=np.arange(0, 30, 1), columns=np.arange(0,1, 0.01))
#for exp in data.index.values:
#   data.ix[exp] = np.arange(0,1, 0.01)**(.1*exp)

def animate(nframe):
   plt.cla()
   nframe_s = nframe + int(s)
   #nframe_e = nframe + int(e)
   #print nframe,s
   #print filelist
   #if (int(s) <= pp < int(e)):
   filename = filelist[nframe_s]
   print nframe_s, filename
   for line in open( filename, 'r'):
       itemList = line[:].split(',')
   FT = [float(itemList[i]) for i in xrange(DimImg)]
   custm = rv_discrete(name='custm', values=(x, FT))
   plt.bar(x, custm.pmf(x) , color='blue')
   #plt.plot(x, custm.pmf(x)) #data.ix[nframe])
   plt.ylim(0.0,1.0)
   plt.xlim(0,DimImg)
   #plt.xticks([0,1,2,3,4,5],['aaaaaa','bbbbb','c','d','eeeee','f'], fontsize=5, rotation=90)
   filename = filelist[nframe_s]
   timename = filename[len(trialname+"CNN_Places365/"):-4]
   plt.title("%d, %s" % (nframe_s,timename)) #, fontsize=10, fontname='serif') # タイトル



ims = []
pp =0
"""
for filename in filelist:
        #rand = np.random.randn(100)     # 100個の乱数を生成
        #im = plt.plot(rand)             # 乱数をグラフにする
        #im = plt.bar(x, poisson.pmf(x, lamda))
        FT = []
        #
        if (int(s) <= pp < int(e)):
          print filename
          for line in open( filename, 'r'):
            itemList = line[:].split(',')
            #for i in xrange(len(itemList)):
            #  if itemList[i] != "":
            #FT.append( [float(itemList[i]) for i in xrange(DimImg)] )
            #print itemList[204]
            FT = [float(itemList[i]) for i in xrange(DimImg)]
            
          #if sum(FT) != 1.0:
          #  print "not sum 1.0",sum(FT) #,FT
          custm = rv_discrete(name='custm', values=(x, FT))
          timename = filename[len(trialname):-4]
          #plt.cla()
          #plt.title("%s" % timename) #, fontsize=10, fontname='serif') # タイトル
          #ims.append(im)
          #t = ax.annotate(timename,(50,50),color='w')
          plt.ylim(0.0,1.0)
          im = plt.bar(x, custm.pmf(x) , color='blue')
        
          ims.append(im)                  # グラフを配列 ims に追加
          #plt.title("%s" % timename) #, fontsize=10, fontname='serif') # タイトル
        pp += 1
"""

# 動画保存の準備
#Writer = animation.writers['ffmpeg']
#writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)


# 10枚のプロットを 100ms ごとに表示
#ani = animation.ArtistAnimation(fig, ims, interval=100, repeat_delay = 100)
#mywriter = animation.FFMpegWriter()
#ani.save('./mymovie.mp4',writer=mywriter)
ani = animation.FuncAnimation(fig, animate, frames=int(e)-int(s))

ani.save(trialname+'CNNanime2/hoge'+s+'-'+e+'.gif', writer='imagemagick')

plt.show()

