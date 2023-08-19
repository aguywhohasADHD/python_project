print("E5-5")
string="I am a genius!"
list1=[]
for x in string:
    list1.append(x)
print(list1)
print("E5-6")
string="I am a genius"
list1=[]
i=0
while i<len(string):
    list1.append(string[i])
    i=i+1
print(list1)
print("E5-7")
numbers=[7,9,15,18,30,-3,7,12,-16,-12]
sum=0
for number in numbers:
    sum=sum+number
print("합계 :",sum)
print("E5-8")
numbers=[7,9,15,18,30,-3,7,12,-16,-12]
sum=0
i=0
while i<len(numbers):
    sum=sum+numbers[i]
    i=i+1
print("합계 :",sum)
print("E5-9")
numbers=[7,9,15,18,30,-3,7,12,-16,-12]
sum=0
a=0
print("짝수 번째 요소 :",end="")
while a < len(numbers):
    if (a+1)%2==0:
        sum=sum+numbers[a]
        print(numbers[a],end=" ")
    a=a+1
print()
print("합계 :",sum)
print("S5-1")
file_names=["file1.py","file2.txt","file3.pptx","file4.doc"]
for file_name in file_names:
    arr=file_name.split(".")
    print("%s => 파일명:%s, 확장자:.%s"%(file_name,arr[0],arr[1]))
del file_name,a,sum,i,numbers,list1,string