import sys
from typing import final
from arithmetic import *
from data_transfer import *
from branch_transfer import *
from registers import *
from memory import *
from pc import *

# __________________Dictionary where key is the op code and the value is the function for that instruction__________

ins = {'10000': my_add,
       '10001': my_sub,
       '10110': my_mul,
       '11010': my_xor,
       '11011': my_or,
       '11100': my_and,
       '10010': my_mov_B,
       '11001': my_ls,
       '11000': my_rs,
       '10011': my_mov_C,
       '11101': my_not,
       '11110': my_cmp,
       '10111': my_div,
       '10100': my_ld,
       '10101': my_st,
       '11111': my_jmp,
       '01100': my_jlt,
       '01101': my_jgt,
       '01111': my_je,
       '01010': my_hlt}

A = ['10000', '00001', '10110', '11010', '11011', '11100']
B = ['10010', '11001', '11000']
C = ['10011', '10111', '11101', '11110']
D = ['10100','10101']
E = ['11111','01100','01101','01111']
F = ['01010']

def my_print():
    list = []
    list.append(pc_convert_bin(pc))
    list.append(convert_bin(final_reg[0]))
    list.append(convert_bin(final_reg[1]))
    list.append(convert_bin(final_reg[2]))
    list.append(convert_bin(final_reg[3]))
    list.append(convert_bin(final_reg[4]))
    list.append(convert_bin(final_reg[5]))
    list.append(convert_bin(final_reg[6]))
    list.append(convert_bin(final_reg[7]))
    print(*list)

source_code = sys.stdin.read().rstrip()
lines = source_code.split("\n")
pc = 0

for i, line in enumerate(lines):
    mem[i] = line

halted = False
while not halted:
#    print('hello',pc)
    line = mem[pc]
    op_ins = line[0:5]
    if op_ins == '01010':
        halted = True
        break
    ck=0
    
    if op_ins in A:
        ins[op_ins](bd(line[7:10]), bd(line[10:13]), bd(line[13:16]))

    elif op_ins in B:
        ins[op_ins](bd(line[5:8]),bd(line[8:16]))

    elif op_ins in C:
        ins[op_ins](bd(line[10:13]),bd(line[13:16]))

    elif op_ins in D:
        ins[op_ins](bd(line[5:8]),line[8:16])

    elif op_ins in E:
        ck=1
        pc_1= ins[op_ins](line[8:16])
        if pc_1==+1:
            my_print()
            pass
        else :
            my_print()
            pc = pc_1-1

    if ck==0:
        my_print()
    pc+=1


my_print()

for i in mem:
    print(i)
