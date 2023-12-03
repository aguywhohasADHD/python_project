coffee=3
price=2000
print("판매 가능한 커피 잔량 : %d" %coffee)
print("단가 : %d원"%price)
while True:
    money=int(input('돈을 넣어주세요: '))
    if money==price:
        print("커피를 팝니다.")
        coffee-=1
    elif money>price:
        print("거스름돈 {}를 주고, 커피를 팝니다.".format(money-price))
        coffee-=1
    else:
        print('돈을 다시 돌려주고, 커피를 팔지 않습니다.')
    print("남은 커피의 양은 {}개입니다.".format(coffee))
    if coffee==0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break