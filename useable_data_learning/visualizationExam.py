import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
from math import sqrt
font_location='c:/windows/fonts/malgun.ttf'
font_name=font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font',family=font_name)
theaterfile='theater.csv'
colnames=['id','theater','region','bindo']
dftheater=pd.read_csv(theaterfile,names=colnames,header=None)
dftheater=dftheater.rename(index=dftheater.id)
dftheater=dftheater.reindex(columns=['theater','region','bindo'])
dftheater.index.name='id'
print('전제 조회')
print(dftheater)
print('극장별 상영 횟수 집계')
mygrouping=dftheater.groupby('theater')['bindo']
sumSeries=mygrouping.sum()
meanSeries=mygrouping.mean()
sizeSeries=mygrouping.size()
print('Series 3개를 이용하여 DataFrame을 만들어 낸다.')
df=pd.concat([sumSeries,meanSeries,sizeSeries],axis=1)
df.columns=['합계','평균','개수']
print(df)
df.plot(kind='barh',rot=0)
#df.plot(kind='barh',rot=0,alpha=0.7,legend=True,stacked=True)
plt.title(str(mysize)+'개 매장 집계 데이터')
#plt.show()
filename='visuallizationExam_01.png'
plt.savefig(filename)
print('집계 메소드를 사전에 담아 전달하기')
