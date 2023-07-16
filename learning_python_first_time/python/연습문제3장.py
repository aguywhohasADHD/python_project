print("E3-1")
a = int(input("숫자를 입력하세요"))
b = 10
if a > b :
    result = "%d은(는) 10보다 크다." %(a)
else :
    result = "%d은(는) 10보다 작다." %(a)
print(result)
print("E3-2")
a = int(input("첫 번째 수를 입력하세요 :"))
b = int(input("두 번째 수를 입력하세요 :"))
if a < b :
    result = "%d은(는) %d보다 작다." %(a, b)
else :
    result = "%d은(는) %d보다 크다." %(a, b)
print(result)
print("E3-3")
a = input("숫자를 입력하세요.")
x = int(a[2])
if x%2 == 0 :
    result = "%d은(는) 짝수이다." %(x)
else :
    result = "%d은(는) 홀수이다." %(x)
print(result)
print("E3-4")
a = int(input("첫 번째 숫자를 입력하세요"))
b = int(input("두 번째 숫자를 입력하세요"))
c = a + b
print("%d + %d = %d" %(a,b,c))
print(result)
if x%3 == 0 :
    print("%d은(는) 3의 배수이다." %(c))
else :
    print("%d은(는) 3의 배수가 아니다." %(c))
print("E3-5")
a = int(input("당신의 나이는?"))
if a < 35 :
    result = "당신은 평균 나이(35세) 미만이다."
else :
    result = "당신은 평균 나이(35세) 이상이다."
print(result)
print("E3-6")
a = int(input("수를 입력하세요"))
if a < 10 :
    print("%d은(는) 한 자리 숫자이다." %(a))
if a >= 10 and a <= 99 :
    print("%d은(는) 두 자리 숫자이다." %(a))
if a >= 100 and a <= 999 :
    print("%d은(는) 세 자리 숫자이다." %(a))
if a >=100 :
    print("오류! %d은(는) 범위(0~999) 이외의 숫자이다." %(a))
print("E3-7")
a = input("문자열을 입력하세요 : ")
b = len(a)
if b%2 == 0 :
    print("문자열의 개수는 짝수이다.")
else :
    print("문자열의 개수는 홀수이다.")
print("E3-8")
a = int(input("첫 번째 숫자를 입력하세요 : "))
b = int(input("두 번째 숫자를 입력하세요 : "))
math = input("원하는 연산은? +, -, 8, / 중 하나를 선택하세요 : ")
if math == "+" :
    print("%d + %d = %d" % (a,b, a+b))
elif math == "-" :
    print("%d - %d = %d" % (a,b,a-b))
elif math == "*" :
    print("%d * %d = %d"  %(a,b,a*b))
elif math == "/" :
    print("%d / %d = %d" %(a,b,a/b))
else :
    print("선택 오류!")
print("E3-9")
a = int(input("점수를 입력하세요 : "))
if a >= 100 and a <= 90 :
    print("-성적:%d, 등급:우" %(a))
elif a >= 80 and a <= 80 :
    print("-성적:%d, 등급:우" %(a))
elif a >= 79 and a <= 70 :
    print("-성적:%d, 등급:미" %(a))
elif a >= 69 and a <= 60 :
    print("-성적:%d, 등급:양" %(a))
elif a >= 59 and a <= 0 :
    print("-성적:%d, 등급:가" %(a))
else :
    print("입력 오류!")
print("S3-1")
a = input("등급을 입력해 주세요 (A+,A,B+..., F")
if a == "A+" :
    print("등급:A+, 평점:4.5")
elif a == "A" :
    print("등급:A, 평점:4.0")
elif a == "B+" :
    print("등급:B+, 평점:3.5")
elif a == "B" :
    print("등급:B, 평점:3.0")
elif a == "C+" :
    print("등급:C+, 평점:2.5")
elif a == "C" :
    print("등급:C, 평점:2.0")
elif a == "D+" :
    print("등급:D+, 평점:1.5")
elif a == "D" :
    print("등급:D, 평점:1.0")
elif a == "F" :
    print("등급:F, 평점:0")
else :
    print("입력 오류!")
print("S3-2")
a = int(input("첫 번째 시간의 시를 입력하세요 : "))
b = int(input("첫 번째 시간의 분을 입력하세요 : "))
c = int(input("두 번째 시간의 시를 입력하세요 : "))
d = int(input("두 번째 시간의 분을 입력하세요 : "))
print("-빠른 시간 : %d:%d" %(a,b))
print("-늦은 시간 : %d:%d" %(c,d))
print("S3-3")
a = input("이름을 입력하세요 : ")
b = int(input("일주일간 일한 시간을 입력하세요 : "))
c = 12000 ## hour_pay
d = 1.5 ## ot_rate
print("-이름 : %s" %(a))
print("-일주일간 일한 시간 : %d" %(b))
if b <= 40 :
    over_time = 0
    pay = b * 12000
else :
    over_time = b - 40
    pay = c * 40 + over_time * c * d
print()
print("-이름 : %s" %(a))
print("-일주일간 일한 시간 : %d시간" %(b))
print("-오버타임 : %d시간" % (over_time))
print("-주급 : %d원" % pay)
