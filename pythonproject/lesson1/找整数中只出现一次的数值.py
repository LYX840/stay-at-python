nums=list(map(int,input("请输入数值用空格隔开").split()))
count={}
z=0
for n in nums:
    if n in count:
        count[n]+=1
    else:
        count[n]=1
for key,value in count.items():
    if value==1:
        print(f"{key}出现了1次")
        z+=1
if z==0:
    print("没有出现1次的数值")