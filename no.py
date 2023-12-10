l1=[]
l2=[]
power=False
def stun():
    print(l1)
    for i in range(len(l1)):
        x=l1[i]**2
        print("Working on the {} number that is {}.\nBecame {}!".format(i+1,l1[i],x))
        l2.append(x)
    print("the list is:"+str(l2))
    return

rangeval=eval(input("enter how many times: "))+1
for i in range(1,rangeval):
    num1=eval(input("Enter the value of the {} value: ".format(i)))
    l1.append(num1)
reg=input("Enter Y to use the power system.").upper()
power=reg=="Y"
if power:
    stun()