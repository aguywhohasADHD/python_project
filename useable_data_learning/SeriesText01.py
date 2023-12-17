from pandas import Series
mylist=[10,40,30,20]
myseries=Series(data=mylist,index=['강감찬','이순신','김유신','광해군'])
print('\n#자료형 확인')
print(type(myseries))
myseries.index=name='점수'
print('\n#시리즈의 색인 이름')
print(myseries.index.name)
myseries.name='학생들 시험'
print('\n#시리즈의 이름')
print(myseries.name)
print('\n#색인 확인하기')
print(myseries.index)
print('\n#시리즈의 값 확인')
print(myseries.values)
print('\n#시리즈 정보 출력')
print(myseries)
print('\n#반복하여 출력하기')
for idx in myseries.index:
    print('색인 : '+idx+', 값 : '+str(myseries[idx]))
print('\n여러 개의 색인 이름으로 데이터 읽기')
print(myseries[['서대문구','서초구']])
print('\n점수를 이용한 데이터 읽기')
print(myseries[[2]])
print('\n0, 2, 4번째 데이터 읽기')
print(myseries[0:5:2])
print('\n1, 3, 5번째 데이터 읽기')
print(myseries[[1,3,5]])
print('\n슬라이싱 사용하기')
print(myseries[3:6])#from <= 결과 < to 1, 3, 5번째 데이터 읽기
print('\n2번째 항목의 값 변경')
myseries[2]=90
print('\n2번째부터 4번째까지 항목의 값 변경')
myseries[2:5]=33
print('\m용산구와 서대문구만 55로 변경')
myseries[['용산구','서대문구']]==55
print('\n짝수 행만 80으로 변경')
myseries[0::2]=80
print('\n시리즈 내용 확인')
print(myseries)