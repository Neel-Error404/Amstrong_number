lo= int(input('Input the lower ranger'))
hi= int(input('Input the hi ranger'))
po= int(input('Input the power'))
for n in range(lo,hi+1):
    num=n
    see=0
    while n>0:
        re= n%10
        see=see+ pow(re,po)
        n=n//10
    if num==see:
        print(num,'is an amstrong number')
