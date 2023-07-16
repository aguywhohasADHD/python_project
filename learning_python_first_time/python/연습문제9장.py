print("S9-1")
x=["가위","바위","보"]
import random
print("="*20)
print("가위바위보 게임")
print("="*20)
def who_win(x,y):
    if x=="가위":
        if y=="가위":
            message="무승부입니다!"
        elif y=="바위":
            message="당신의 승리입니다!"
        else:
            message="나의 승리입니다!"
    elif x=="바위":
        if y=="가위":
            message="나의 승리입니다!"
        elif y=="바위":
            message="무승부입니다!"
        else:
            message="당신의 승리입니다!"
    else:
        if y=="가위":
            message="당신의 승리입니다!"
        elif y=="바위":
            message="나의 승리입니다!"
        else:
            message="무승부입니다!"
    return message
again="y"
while again=="y":
    me=random.choice(x)
    you=random.choice(x)
    result=who_win(me,you)
    print("나 : %s"% me)
    print("당신 : %s"% you)
    print(result)
    print("-"*20)
    again=input("계속하려면 y를 입력하세요.")
print("게임이 종료되었습니다.")
del result,me,you,who_win,x,again,random