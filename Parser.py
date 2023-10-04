def obradi(ulazniNiz):
    ret = ['',ulazniNiz, 1]
    if(len(ulazniNiz)==0):
        ret = ['S', ulazniNiz, 0]
    else:
        ret = S(ret[0], ret[1], ret[2])
    return ret

def S(ispis,ulazniNiz, valjano):
    ret = [ispis,ulazniNiz, valjano]
    ret[0] +="S"
    if(len(ulazniNiz)==0):
        ret[2] = 0
        return ret
    if(ret[1][0] == 'a'):
        ret[1]= ret[1][1::]
        ret = A(ret[0], ret[1], ret[2])
        if(ret[2]==0):
            return ret
        ret = B(ret[0], ret[1], ret[2])
        return ret
    elif(ret[1][0] == 'b'):
        ret[1]= ret[1][1::]
        ret = B(ret[0], ret[1], ret[2])
        if(ret[2] ==0):
            return ret
        ret=A(ret[0], ret[1], ret[2])
        return ret
    ret[2] = 0
    return ret


def A(ispis,ulazniNiz, valjano):
    ret = [ispis,ulazniNiz, valjano]
    ret[0] +="A"
    if(len(ret[1])!=0 and ret[1][0]=='a'):
        ret[1]= ret[1][1::]
        return ret
    elif(len(ret[1])!=0  and ret[1][0] =='b'):
        ret[1]= ret[1][1::]
        return C(ret[0], ret[1], ret[2])
    ret[2] = 0
    return ret
    
def B(ispis,ulazniNiz, valjano):
    ret = [ispis,ulazniNiz, valjano]
    ret[0] +="B"
    if(len(ret[1])==0):
        return ret
    if(ret[1][0:2]=='cc'):
        ret[1]=ret[1][2::]
        ret = S(ret[0], ret[1], ret[2])
        if(ret[1][0:2]!='bc'):
            ret[2] = 0
            return ret
        ret[1]=ret[1][2::]
        return ret
    return ret

def C(ispis,ulazniNiz, valjano):
    ret = [ispis,ulazniNiz, valjano]
    ret[0] +="C"
    ret = A(ret[0], ret[1], ret[2])
    if (ret[2]!=0):
        return A(ret[0], ret[1], ret[2])
    ret[2] = 0
    return ret

ulazniNiz = input()
retVal = obradi(ulazniNiz)
ispis = retVal[0]
ulazniNiz = retVal[1]
rez = retVal[2]
print(ispis)
if(len(ulazniNiz)!= 0):
    print("NE")
elif(rez==0):
    print("NE")
else:
    print("DA")
