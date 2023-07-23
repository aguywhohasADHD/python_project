#E2-1
a=10
b=20
print(a+b)
#E2-2
a=10
b=20
sum=a+b
print("%d + %d = %d"%(a,b,sum))
#E2-3
a=10
b=20
sum=a+b
print(str(a)+"+"+str(b)+"="+str(sum))
#E2-4
fruit1=input("첫 번째 과일을 입력하세요 :")
fruit2=input("두 번째 과일을 입력하세요 :")
print(fruit1+"와(과)"+fruit2+"은(는)"+"내가 좋아하는 과일이다.")
#E2-5
fruit1=input("첫 번째 과일을 입력하세요 :")
fruit2=input("두 번째 과일을 입력하세요 :")
print(fruit1,"와(과)",fruit2,"은(는) 내가 좋아하는 과일이다.",sep="")
#E2-6
fruit1=input("첫 번째 과일을 입력하세요 :")
fruit2=input("두 번째 과일을 입력하세요 :")
print("%s와(과) %s은(는) 내가 좋아하는 과일이다."%(fruit1,fruit2))
#E2-7
a=int(input("첫 번째 숫자를 입력하세요 :"))
b=int(input("두 번째 숫자를 입력하세요 :"))
c=a/b
print("%d / %d = %f"%(a,b,c))
#E2-8
a=int(input("첫 번째 숫자를 입력하세요 :"))
b=int(input("두 번째 숫자를 입력하세요 :"))
c=a/b
print("%d / %d = %.2f"%(a,b,c))
#E2-9
a=input("이메일 주소 앞 부분은?")
b=input("이메일 도메인 이름은?")
email=a+'@'+b
print("-이메일 주소 :",email)
#E2-10
name=input("이름을 입력하세요")
location=input("주소를 입력하세요")
number=input("전화번호를 입력하세요")
print("-이름 : %s" %(name))
print("-주소 : %s" %(location))
print("-전화번호 : %s"%(number))
#E2-11
## 사다리꼴 면적 : [(윗변 길이) + (밑변길이)] x 높이 /2
a=int(input("윗변의 길이는?"))
b=int(input("밑변의 길이는?"))
c=int(input("높이는?"))
d=(a+b)*c/2
print("-사다리꼴의 면적 : %.1f"%(d))
#E2-12
a="가는 말이 고와야 오는 말이 곱다."
print(a)
print("- 추출문자 : ",a[10:14])
#E2-13
a=input("열 자리의 숫자를 입력하세요 : ")
print(" - 추출된 두 숫자 :",a[-2:])
#S2-1
## 파운드 = 킬로그램 x 2.204623, 온스 = 킬로그램 x 35.273962
kg=int(input("변환할 킬로그램(kg)은?"))
print("-" * 50)
print("킬로그램 파운드 온스")
print("-" * 60)
pound=kg*2.204623 ## 파운드
ounce=kg*35.273962 ## 온스
print("%f %.2f %.2f" %(kg,pound,ounce))
print("-"*50)
#S2-2
phone1=input("하이픈(-)이 포함된 11자리의 휴대폰 번호는?")
print(" -입력된 휴대폰 번호 : "+phone1)
phone2=phone1[0:3]+phone1[4:8]+phone1[9:]
print(" - 하이픈이 삭제된 휴대폰 번호 : "+phone2)
del a,b,phone1,phone2,ounce,pound,kg,d,c,number,name,location,email,fruit1,fruit2,