#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import sys

def format_domains(text): # converts "    6 - A   44 -  A   61 - A  106 -  A  332 - A  460 "  format to  6:44,61:106,332:460
    # Find all numbers in the text
    numbers = re.findall(r'\d+', text)

    # Pair every two numbers with '-', and join these pairs with '+'
    formatted_output = ','.join([':'.join(numbers[i:i+2]) for i in range(0, len(numbers), 2)])

    return formatted_output

#the input file is 'two_domains_cath'
input_file=sys.argv[1]
#input_file="two_domains_cath"
file=open(input_file,'r')
lines=file.readlines()

#UNCOMMENT the os.system for real function

for line in lines:
    print(line[0:4])
    n_dom=int(line[7:9])
    #print(n_dom)
    a=line[15:]
    hypens=[match.start() for match in re.finditer('-',a)]
    #print(hypens)
    b=0
    c=(int(a[0])*2)-1
    #print(b,c)
    for i in range(n_dom):
        if i==0 and a[hypens[0]+1].isnumeric():#for the first domain of -ve initials
            x=re.findall(r'\d+',format_domains(a[hypens[b]+1:hypens[c+1]]))
            x[0]='1'
            x=' '.join(y for y in x)
            print('dom_%s:'%(i+1),format_domains(x))
            #os.system('pdb_selres -'+format_domains(x)+' '+line[0:4]+'.pdb | pdb_chain -A > '+line[0:4]+'_'+'dom_%s'%(i+1)+'.pdb')
            continue
        elif i==0 and a[hypens[0]+1].isspace():
            print('dom_%s:'%(i+1),format_domains(a[hypens[b]-6:hypens[c]]))
            #os.system('pdb_selres -'+format_domains(a[hypens[b]-6:hypens[c]])+' '+line[0:4]+'.pdb | pdb_chain -A > '+line[0:4]+'_'+'dom_%s'%(i+1)+'.pdb')
            continue
        elif a[hypens[0]+1].isspace() and a[hypens[c]+3].isnumeric():
            factor=(int(a[hypens[c]+3])*2)
            b1=c
            c=c+factor
            #b=(int(a[hypens[b]+2])*2)-1
            print('dom_%s:'%(i+1), format_domains(a[hypens[b1]+7:hypens[c]]))
            #os.system('pdb_selres -'+format_domains(a[hypens[b1]+7:hypens[c]])+' '+line[0:4]+'.pdb | pdb_chain -B > '+line[0:4]+'_'+'dom_%s'%(i+1)+'.pdb')
            continue
        elif a[hypens[0]+1].isnumeric() and a[hypens[c+1]+3].isnumeric():#for the following domains of -ve initials
            factor=(int(a[hypens[c+1]+3])*2)
            b1=c+1
            c=c+factor
            #b=(int(a[hypens[b]+2])*2)-1
            print('dom_%s:'%(i+1), format_domains(a[hypens[b1]+7:hypens[c+1]]))
            #os.system('pdb_selres -'+format_domains(a[hypens[b1]+7:hypens[c+1]])+' '+line[0:4]+'.pdb | pdb_chain -B > '+line[0:4]+'_'+'dom_%s'%(i+1)+'.pdb')
            continue
        else:
            continue
"""        
elif a[hypens[c]+3].isnumeric():
    factor=(int(a[hypens[c]+3])*2)
    b1=c
    c=c+factor
    #b=(int(a[hypens[b]+2])*2)-1
    print('dom_%s:'%(i+1), format_domains(a[hypens[b1]+7:hypens[c]]))
    #os.system('pdb_selres -'+format_domains(a[hypens[b1]+7:hypens[c]])+' '+line[0:4]+'.pdb | pdb_chain -B > '+line[0:4]+'_'+'dom_%s'%(i+1)+'.pdb')
"""
