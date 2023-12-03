tuple01=(10,20,30)
tuple01=tuple01+(40,)
print('print tuple :',tuple01)
tuple02=10,20,30,40
mylist=[10,20,30,40]
tuple03=tuple(mylist)
if tuple02==tuple03:
    print("component equal")
else:
    print("component not equal")
tuple04=(10,20,30)
tuple05=(40,50,60)
print('+ 연산자는 2개의 튜플을 합치는 역할을 합니다.')
tuple06=tuple04+tuple05
print(tuple06)
print('* 연산자는 튜플을 지정한 정수만큼 반복시키는 역할을 합니다.')
tuple07=tuple04*3
print(tuple07)
print("튜플을 사용하면 변수들을 swap 시킬 수 있습니다.")
a,b=11,22
a,b=b,a
print('a=',a,', b=',b)
tuple08=(11,22,33,44,55,66)
print(tuple08[1:3])
print(tuple08[3:])