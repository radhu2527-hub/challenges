#  this program checks if a given number is amstrong or not

num=int(input('enter a number::'))          
num_1=num
sum=0
temp=0
while num>0:
    temp=num%10
    sum=sum+temp**3
    num//=10

if num_1==sum:
    print('number entered is amstrong')
        
else:
    print('not amstrong')


#this pgm prints the list of amstrong numbers in an upper and lower limit

lower=int(input('enter the lower limit::'))
upper=int(input('enter upper limit::'))
amstrong=['amstrong numbers in range',lower,upper,'are']
print(amstrong)
for num in range(lower,upper+1):
    sum=0
    temp=num
    while(temp>0):
        digit=temp%10
        sum=sum+digit**3
        temp//=10
    if num==sum:
        print(num)
        print()


    



