wordInfo={'세탁기':50,'선풍기':30,'청소기':40,'냉장고':60}
myxticks=sorted(wordInfo,key=wordInfo.get,reverse=True)
print(myxticks)
reverse_key=sorted(wordInfo.keys(),reverse=True)
print(reverse_key)
chartdata=sorted(wordInfo.values(),reverse=True)
print(chartdata)
def nolambda(x,y):
    return 3*x+2*y
x,y=3,5
result=nolambda(x,y)
print('일반 함수 방식 : %d'%result)
yeslambda=lambda x,y:3*x+2*y
result=yeslambda(x,y)
print("람다 방식 01 : %d"%(result))
result=yeslambda(5,7)
print('람다 방식 02 : %d'%(result))

def function(x,y):
    return 3*x+2*y

lambda x,y: 3*x + 2*y