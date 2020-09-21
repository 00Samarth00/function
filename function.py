'''def most_frequent(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

str1=input("Enter a string:")
result=most_frequent(str1)
print(result)'''
#-------------------------------------------------------------


def most_frequent(x):
    alp='abcdefghijklmnopqrstuvwxyz'
    key=[]
    val=[]
    result=[]
    for i in range(0,26):
        if(x.count(alp[i])>0):
            key.append(alp[i])
            val.append(x.count(alp[i]))
            result.append(str(str(x.count(alp[i]))+'='+alp[i]))
            result.sort(reverse=True)
            
        else:
            None
    
    
    return result

        


in_=input('ENTER A STRING HERE:')

in_=in_.casefold()

final=most_frequent(in_)
print(final)





 
    































'''alp='abcdefghijklmnopqrstuvwxyz'
x={}
num=[]
for i in range(0,26):
    if(in_.count(alp[i])>0):
       x[alp[i]]=in_.count(alp[i])
       num.append((in_.count(alp[i]),alp[i]))
       num.sort(reverse=True)
       
       
    else:
        None
print('THE ORDERED PAIR IN FORMAT (NUMBER OF TIMES THAT ALPHABET APPEARS IN THE STRING,ALPHABET):-')
for r in range(0,len(num)-1):
    print(num[r])'''
    







