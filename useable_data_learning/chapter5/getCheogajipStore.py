from itertools import count
from ChickenUtil import ChickenStore
brandName='cheogajip'
base_url='http://www.cheogajip.co.kr/bbs/board.php?bo_table=store'
def getData():
    savedData=[]#엑셀로 저장할 리스트
    for page_idx in count():
        url=base_url
        url+='?bo_table=store'
        url+='&page=%s'%str(page_idx+1)
        chknStore=