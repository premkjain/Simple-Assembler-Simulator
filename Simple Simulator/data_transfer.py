import imp
from registers import *
from memory import *
from pc import *
from arithmetic import *

def my_cmp(reg1,reg2) :
    if final_reg[reg1]==final_reg[reg2] :
        final_reg[7]=1
    elif final_reg[reg1]>final_reg[reg2] :
        final_reg[7]=2
    elif final_reg[reg1]<final_reg[reg2] :
        final_reg[7]=4

def bd(x):
    global final_reg
    s=0
    for i in range(len(x)):
        # s+=int((x[len(x)-i-1])*(2**i))
        s+=int(x[len(x)-i-1])*(2**i)
    return int(s)

def my_ld(reg1,mem_add):
    final_reg[reg1] = bd(mem[bd(mem_add)])

def my_st(reg1,mem_add):
    mem[bd(mem_add)] = convert_bin(final_reg[reg1])

def my_jmp(mem_add):
    return bd(mem_add)

def my_jlt(mem_add):
    ans=0
    if final_reg[7]==4:
        ans=bd(mem_add)
    else :
        ans=+1
    final_reg[7]=0
    return ans

def my_jgt(mem_add):
    ans1=0
    if final_reg[7]==2:
        ans1=bd(mem_add)
    else :
        ans1=+1
    final_reg[7]=0
    return ans1

def my_je(mem_add):
    ans2=0
    if final_reg[7]==1:
        ans2=bd(mem_add)
    else :
        ans2=+1
    final_reg[7]=0
    return ans2

def my_hlt():
    return 1
