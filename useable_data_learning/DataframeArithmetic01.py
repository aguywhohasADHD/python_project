import numpy as np
from pandas import Series,DataFrame
#산술 연산과 데이터 정렬
myindex=['강효민','유재준','신동진']
mylist=[30,40,50]
myseries=Series(data=mylist,index=myindex)
print('\n시리즈 출력 결과')
print(myseries)
myindex=['강효민','유재준','이수진']
mycolumns=['서울','부산','경주']
mylist=list(10*onedata for onedata in range(1,10))
#print(mylist)
myframe=DataFrame(np.reshape(np.array(mylist,)(3,3)),index=myindex,columns=mycolumns)
print('\n데이터프레임 출력 결과')
print(myframe)
result=myframe.add(myseries,axis=0)
print(result)
myindex2=['강효민','유재준','김병만']
mycolumns2=['서울','부산','대구']
mylist2=list(3*onedata for onedata in range(1,10))
#print(mylist)
myframe2=DataFrame(np.reshape(np.array(mylist2),(3,3),index=myindex2,columns=mycolumns2))
print('\n데이터프레임 출력 결과')
print(myframe2)
print('\mDataFrame + DataFrame')
result=myframe.add(myframe2,fillvalue=0)
print(result)