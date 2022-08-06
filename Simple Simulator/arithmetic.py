from re import X
from registers import *
    
def my_add(reg1,reg2,reg3):
    final_reg[reg3] = final_reg[reg1]+final_reg[reg2]

    if final_reg[reg3]>65535 :
        final_reg[7]=1
    # print("received", reg1, reg2, reg3, final_reg)
    final_reg[reg3] = final_reg[reg3]&65535
    # print("aa", final_reg)

def my_sub(reg1,reg2,reg3) :
    final_reg[reg3] = final_reg[reg1]-final_reg[reg2]

def my_mul(reg1,reg2,reg3) :
    final_reg[reg3] = final_reg[reg1]*final_reg[reg2]
    final_reg[reg3] = final_reg[reg3]&65535

def my_or(reg1,reg2,reg3) :
    final_reg[reg3] = final_reg[reg1]|final_reg[reg2]
#    final_reg[reg3] = final_reg[reg3]&65535

def my_and(reg1,reg2,reg3) :
    final_reg[reg3] = final_reg[reg1]&final_reg[reg2]

def my_xor(reg1,reg2,reg3) :
    final_reg[reg3] = final_reg[reg1]^final_reg[reg2]

def my_not(reg1,reg2) :
    final_reg[reg2] = (~final_reg[reg1]) & 65535

def my_div(reg1,reg2) :
    a = final_reg[reg1]/final_reg[reg2]
    b = final_reg[reg1]%final_reg[reg2]
    final_reg[0] = a
    final_reg[1] = b
    return (a,b)

def convert_bin(num) :
    # print("ok", num)
    num1 = num & 65535
    a =('0'*(16-len(bin(num1)[2:]))+ bin(num1)[2:] )
    return a

def pc_convert_bin(num):
    num1 = num & 255
    a =('0'*(8-len(bin(num1)[2:]))+ bin(num1)[2:] )
    return a


def bd(x):
    s=0
    for i in range(len(x)):
        s+=int(x[len(x)-i-1])*(2**i)
    return int(s)
