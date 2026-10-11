n=int(input("请输入数值"))
count=0
if n<0:
    n=n&0xFFFFFFFFFFFFFFFF
while n:
    count+=n&1
    n = n>>1
print(count)