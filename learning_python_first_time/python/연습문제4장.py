print("E4-1")
for a in range(1,10):
    if a%2==1:
        print(a)
print("E4-2")
sum=0
for a in range (1,101):
    if a%3==0:
        sum+=a
print("1~100 까지의 3의 배수 합계 :",sum)
print("E4-3")
sum=0
for a in range (1,101):
    if a%5==0:
        print(a,end=" ")
print("E4-4")
count=0
for a in range (1,101):
    if a%5==0:
        print(a,end=" ")
        count+=1
        if count%5==0:
            print()
print("E4-5")
sum=0
for a in range (1,101):
    if a%4==0:
        sum+=a
        print(a,"-->",sum)
print("E4-6")
sum=1
for a in range (1,10):
    sum=sum*a
print("10! =",sum)
print("E4-7")
sum=1
a=1
while a<11:
    sum=sum*a
    a+=1
print("10! =",sum)
print("E4-8")
print("-"*20)
print("cm","mm","m","inch",end=" ")
print("-"*20)
sum=0
count=0
for cm in range(1,51):
    mm = cm * 10.0
    inch = cm * 0.3937
    m = cm * 0.01
    print("%8d %8.0f %8.2f %8.2f" %(cm, mm, m, inch))
print ("-" * 20)
print ("E4-9")
print("-" * 20)
cm=1
while cm<50:
    mm=cm*10.0
    inch=cm*0.3937
    m=cm*0.01
    print("%8d %8.0f %8.2f %8.2f" %(cm, mm, m, inch))
    cm+=1
print("-"*20)
print("S4-1")
a=1
count=0
while a<1001:
    if a%3!=0:
        print("%d" %(a), end=" ")
        count=count+1
        if count%10==0:
            print()
a+=1
print("S4-2")
a=int(input("성적을 입력하세요 : "))
while a!="q":
    if a>=90:
        print("등급 : 수")
    elif a>=80:
        print("등급 : 우")
    elif a>=70:
        print("등급 : 미")
    elif a>=60:
        print("등급 : 양")
    elif a<60:
        print("등급 : 가")
    b=input("계속하시겠습니까?(중단:q, 계속:y")
    if b=="q":
        print("exit")
        break
    a=int(input("성적을 입력하세요: "))
print("S4-3")
start=int(input("시작 수를 입력하세요 :"))
stop=int(input("끝 수를 입력하세요 :"))
a=start
while a<=stop+1:
    prime_yes=True
    for i in range (2,a):
        if a%i==0:
            prime_yes = False
            break
    if (prime_yes):
        print(a, end=" ")
    a+=1
del start,stop,prime_yes,b,count,cm,mm,inch,sum