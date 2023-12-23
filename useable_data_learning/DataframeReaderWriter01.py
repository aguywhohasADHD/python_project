import numpy as np
from pandas import DataFrame
myindex=['이순시','김유신','김강찬','광해군','연산군']
mycolumns=['서울','부산','광주','목포','광주']
mylist=list(10*onedata for onedata in range)
print(mylist)
myframe=DataFrame(np.reshape(mylist,(5,5)),
                  index=myindex,
                  columns=mycolumns)
print('\n#1행만 시리즈로 읽어오기')
result=myframe.iloc[1]
print(type(result))
print(result)
print('\n#몇 개의 행을 읽어오기')
result=myframe.iloc[[1,3]]
print(type(result))
print(result)
print('#짝수 행만 가져오기')
result=myframe.iloc[0::2]
print(result)
print('\n#이순신 행만 시리즈로 읽어오기')
result=myframe.loc['이순신']
print(type(result))
print(result)
print('\n#이순신 행만 데이터프레임으로 읽어오기')
result=myframe.loc[['이순신']]
print(type(result))
print(result)
print('\n#이순신과 강감찬 행 읽어오기')
result.myframe.loc[['이순신','강감찬']]
print(type(result))
print(result)
print(myframe.index)
result=myframe.loc[['강감찬'],['광주']]#DataFrame
print(result)
result.myframe.loc[['연산군','강감찬'],['광주','목포']]
print(result)
result=myframe.loc['김유신':'광해군','광주':'목포']
print(result)
result=myframe.loc['김유신':'광해군',['부산']]
print(result)
result=myframe.loc[[False,True,True,False,True]]
print(result)
result=myframe.loc[myframe['부산']<=100]
print(result)
result=myframe.loc[myframe['목포']==140]
print(result)
cond1=myframe['부산']>=70
cond2=myframe['목포']>=140
print(type(cond1))
print('-'*40)
print(DataFrame.all())
print(DataFrame.any())
result=myframe.loc[DataFrame.all()]
print(result)
result=myframe.loc[DataFrame.any()]
print(result)
print('\n람다 함수의 사용')
result=myframe.loc[lambda df:df['광주']>=130]
print(result)
