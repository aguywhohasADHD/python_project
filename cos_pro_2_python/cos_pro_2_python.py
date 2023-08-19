print("문제 01-1")
def solution(n):
    answer=1
    for i in range(1,n+1):
        answer*=i
    return answer
n=5
ret=solution(n)
print("solution 함수의 반환 값은",ret,"입니다.")