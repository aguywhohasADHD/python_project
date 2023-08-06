def solution(n):
    answer=0
    for i in range(1,n+1):
        answer*=i
    return answer
n=int(input("int"))
ret=solution(n)
print("solution 함수의 반환 값은",ret,"입니다.")
def solution(n):
    answer=0
    for i in range(1,n+1):
        answer*=i
    answer+=n
    return answer
n=int(input("int"))
ret=solution(n)
print("solution 함수의 반환 값은",ret,"입니다.")
del solution,ret,n