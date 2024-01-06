mystring='life is an egg'
mylist=mystring.split()
for idx in range(len(mylist)):
    if idx%2==0:
        mylist[idx]=mylist[idx].upper()
    else:
        mylist[idx]=mylist[idx].lower()
print('join()함수를 이용하여 문자열 합치기')
result='#'.join(mylist)
print('결과 리스트 :',result)