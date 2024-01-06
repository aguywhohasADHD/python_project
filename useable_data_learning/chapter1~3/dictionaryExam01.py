dictionary={'김유신':50,'윤봉길':40,'김구':60}
print('사전 내역 : ',dictionary)
print('\nkeys*() 메소드는 사전의 key 목록을 보여 줍니다.')
for key in dictionary.keys():
    print(key)
print('\nvalues() 메소드는 사전의 값들의 목록을 보여 줍니다.')
for value in dictionary.values():
    print(value)
print('\nkeys()를 이용한 value 검색하기')
for key in dictionary.keys():
    print('{}의 나이는 {]입니다'.format(key,dictionary[key]))
print('\nitems() 메소드는 key와 value로 이루어진 쌍(pair)을 보여 줍니다.')
for key, value in dictionary.items():
    print('{}의 나이는 {]입니다.'.format(key,value))
print('\nin은 키의 존재 여부를 확인해줍니다.')
findKey='유관순'
if findKey in dictionary:
    print(findKey+'(은)는 존재합니다.')
else:
    print(findKey+'(은)는 존재하지 않습니다.')
print('\npop()를 이용한 데이터 끄집어 내기')
result=dictionary.pop('김구')
print('pop 이후의 사전 내용 : ',dictionary)
print('pop된 내용 : ',result)
print('\nclear() 메소드는 사전의 내용을 모두 비웁니다.')
dictionary.clear()
print('사전 내역 : ',dictionary)