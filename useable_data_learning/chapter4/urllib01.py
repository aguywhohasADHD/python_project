import urllib.request#라이브러리 읽어 들이기
#URL과 저장 경로 지정하기
url='https://image-comic.pstatic.net/webtoon/626907/thumbnail/thumbnail_IMAG21_7077799770473063780.jpg'
savename='urldownload01.png'
#다운로드
urllib.request.urlretrieve(url,savename)
print('웹에 있는 이미지'+url+'를 ',end='')
print(savename+'파일로 저장하였습니다.')