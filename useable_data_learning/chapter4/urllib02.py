import urllib.request
#url과 저장 경로 지정하기
url="https://www.example.com"
savename='urldownload02.png'
#urlopen()함수를 이용하여 다운로드한다.
result=urllib.request.urlopen(url)
#read() 함수를 이용하여 바이너리 형식으로 변경해준다,
data=result.read()
print('#type(data) :',type(data))
#파일로 저장하기
with open(savename,mode="wb") as f:
    f.write(data)
    print(savename + " 파일로 저장되었습니다.")