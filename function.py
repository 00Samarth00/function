

def most_frequent(x):
    alp='abcdefghijklmnopqrstuvwxyz'
    result=[]
    for i in range(0,26):
        if(x.count(alp[i])>0):
            result.append(str(str(x.count(alp[i]))+'='+alp[i]))
            result.sort(reverse=True)
            
        else:
            None
    
    
    return result

        


in_=input('ENTER A STRING HERE:')

in_=in_.casefold()

final=most_frequent(in_)
print(final)





 
    
































    







