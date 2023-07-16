print("E6-8")
person = {"name":"홍길동", "age":30, "family":5, "children":["선미", "성진", "소영"], "pets":["강아지", "고양이", "이구아나"]}
for key in person:
    if key == "children":
        num_child = len(person[key])
        print("자녀 수 : %d명"%(num_child))
print("S6-1")
temp = {"월":15.5, "화":17.0, "수":16.2, "목":12.9, "금":11.0, "토":10.5, "일":13.3}
print("-"*25)
print(" 월 화 수 목 금 토 일 ")
print("-"*25)
for key in temp:
    print("%6.1f"%(temp[key]),end="")
print()
print("-"*25)
print("S6-2")
temp = {"월":15.5, "화":17.0, "수":16.2, "목":12.9, "금":11.0, "토":10.5, "일":13.3}
smallest = temp["월"]
for key in temp:
    if temp[key]< smallest:
        day = key
        smallest = temp[key]
print("요일:%s, 최저 기온:%.1fº"%(day,smallest))
print("S6-3")
temp = {"월":15.5, "화":17.0, "수":16.2, "목":12.9, "금":11.0, "토":10.5, "일":13.3}
sum = 0
for key in temp:
    sum += temp[key]
avg = sum/len(temp)
print("일주인간 기온 평균 : %.1fº"%(avg))