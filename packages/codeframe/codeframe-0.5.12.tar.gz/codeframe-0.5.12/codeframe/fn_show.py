#!/usr/bin/env python3
"""
 These modules should contain one function each...


"""

from fire import Fire
from console import fg,bg
from codeframe import config


def main(*args,**kwargs):
    print(f"{fg.dimgray}D... main() @fn_lo: args/kwargs.../{args}/{kwargs}/{fg.default}")
    #print(f"D... main() @fn_show: args/kwargs.../{args}/{kwargs}/")
    if len(args)==0:
        print("D...  give me an object: allowed objects:",config.object_list)
    elif args[0] in config.object_list:
        print(f"{fg.green}i... showing {args[0]}{fg.default}")

if __name__=="__main__":
    Fire(main)
