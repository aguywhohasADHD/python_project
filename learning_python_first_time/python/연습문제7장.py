print("E7-4")
def killometer_to_mile(killo):
    mile=killo*0.621371
    print("%d킬로미터는 %.2f 마일이다."%(killo,mile))
a=int(input("킬로미터를 입력하세요 : "))
killometer_to_mile(a)
print("E7-5")
def math(a,b,c):
    if a==1:
        print("%d + %d = %d"%(b,c,b+c))
    elif a==2:
        print("%d - %d = %d"%(b,c,b-c))
    elif a==3:
        print("%d x %d = %d"%(b,c,b*c))
    elif a==4:
        print("%d / %d = %d"%(b,c,b/c))
    else:
        raise ValueError("오류 : a가 1,2,3,4, 중 하나의 값이어야 함.")
print("- 선택 옵션")
print("1. 더하기")
print("2. 빼기")
print("3. 곱하기")
print("4. 나누기")
a=int(input("원하는 연산을 선택하세요(1/2/3/4) : "))
b=int(input("첫 번째 숫자를 입력하세요"))
c=int(input("두 번째 숫자를 입력하세요"))
math(a,b,c)
print("E7-6")
def count_char(string,x):
    count=0
    for i in string:
        if i==x:
            count=count+1
    return count
test_str=input("영어 문장을 입력하세요 : ")
character=input("알파벳 하나를 입력하세요 : ")
num_char = count_char(test_str,character)
print("%s 에 포함된 %s의 개수는 %d 개이다."%(test_str,character,num_char))
print("E7-7")
tup1=(10,20,30,40,50)
def sum_tup(numbers):
    total=0
    for number in numbers:
        total=total+number
    return total
total=sum_tup(tup1)
print("튜플의 합계 :",total)
print("E7-8")
def str_reverse(string):
    result=""
    index=len(string)
    while index>0:
        result=result+string[index-1]
        index=index-1
    return result
string=input("문자열을 입력하세요 : ")
print(str_reverse(string))
print("E7-9")
def space_hyper(string):
    result=""
    i=0
    while i<len(string):
        if string[i]==" ":
            result=result+"-"
        else:
            result=result+string[i]
        i=i+1
    return result
string=input("문자열을 입력하세요 : ")
print(space_hyper(string))
print("E7-10")
#인치=센티미터x0.393701
#파운드=킬로그램x2.204623
def convert(a,b):
    if a==1:
        print("%d 센티미터 --> %.2f 인치"%(b,b*0.393701))
    elif a==2:
        print("%d 킬로그램 --> %.2f 파운드"%(b,b*2.204623))
    else:
        raise ValueError("오류. a의 값이 1 혹은 2중 하나여야 합니다.")
c=int(input("원하는 환산 단위를 선택하세요.(1/2) : "))
if c==1:
    d=int(input("센티미터 단위의 길이를 입력하세요 : "))
    convert(c,d)
elif c==2:
    d=int(input("킬로그램 단위의 무게를 입력하세요 : "))
    convert(c,d)
print("S7-1")
def isPrimeNumber(num):
    prime_yes=True
    for i in range(2,num):
        if num%i==0:
            prime_yes=False
            break
    return prime_yes
n=int(input("n값을 입력해 주세요 : "))
print("2 ~ %d까지의 정수 중 소수 : "% n, end=" ")
for a in range(2,n+1):
    is_prime=isPrimeNumber(a)
    if is_prime:
        print(a,end=" ")
print("S7-2")
def match_word(word,answer):
    if word==answer:
        result="참 잘했어요!"
    else:
        result="틀렸어요!"
    return result
eng_dict={"house":"집","piano":"피아노","christmas":"크리스마스","friend":"친구","bread":"빵"}
for i in eng_dict:
    string=input(eng_dict[i]+"에 맞는 영어 단어는?")
    msg=match_word(string,i)
    print(msg)
print("S7-3")
def make_square(num):
    list_new=[]
    for i in range(1,num+1):
        list_new.append(i**2)
    return list_new
n=int(input("n값을 입력하세요 : "))
list1=make_square(n)
print(list1)
del make_square,list1,n,a,b,c,d,i,eng_dict,string,msg,match_word,isPrimeNumber,math,is_prime,convert,space_hyper,str_reverse,count_char,total,sum_tup,tup1,num_char,killometer_to_mile,test_str,character,