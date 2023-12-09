import os
myfolder='d:\\'
newpath=os.path.join(myfolder,'hello')
try:
    os.mkdir(path=newpath)
    for idx in range(1,11):
        newfile=os.path.join(newpath,'somefolder'+str(idx).zfill(2))
        os.mkdir(path=newfile)
except fileExistserror:
    print('디렉터리가 이미 존재합니다.')
print('finished')