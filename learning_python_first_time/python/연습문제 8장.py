print("E8-1")
def numbered(n):
    if n%2==0:
        print("%d은(는) 짝수이다."%(n))
    else:
        print("%d은(는) 홀수이다."%(n))
N=int(input("수를 입력하세요: "))
numbered(N)
del N
del numbered
print("E8-2") #1에서 1000까지
def multiple_sum(n):
    sm=0
    for x in range(1,1001):
        if x%n==0:
            sm=sm+x
    return sm
c=int(input("N값을 입력하세요 : "))
total=multiple_sum(c)
print("1에서 1000까지의 수중 %d의 배수 합계 : %d"%(c,total))
del total
del c
del multiple_sum
print("E8-3")
sentence="강아지/사슴/거북/고릴라/청개구리"
def get_word(s):
    temp=s.split("/")
    return temp
words=get_word(sentence)
for word in words:
    length=len(word)
    print("%s : %d"%(word,length))
del word,words,get_word,sentence
print("E8-4")
num1=[2,6,3,8,7]
print("num1 = ",num1)
def get_mult(list1):
    list2=[]
    for x in list1:
        if x%2==0:
            list2.append(x*10)
        else:
            list2.append(x*100)
    return list2
print("num2 = ",get_mult(num1))
print("S8-1")
