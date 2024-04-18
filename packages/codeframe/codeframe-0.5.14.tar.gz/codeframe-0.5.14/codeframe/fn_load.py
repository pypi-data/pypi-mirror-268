#!/usr/bin/env python3
"""
 These modules should contain one function each...

MODIFIY THE original codeframe adding these functions only + editing CONFIG

... they need some common connect point to have common objects:
 1. config ?
  -  yes, but is there possible to do without?
     - ? for the sake of codeframe initial paradigm? or is that ok?

"""

from fire import Fire
from console import fg,bg
from codeframe import config
# I NEED TO UPDATE  -   config.object_list


def main(*args,**kwargs):
    print(f"{fg.dimgray}D... main() @fn_lo: args/kwargs.../{args}/{kwargs}/{fg.default}")
    #print(f"D... main() @fn_load: args/kwargs.../{args}/{kwargs}/")
    if len(args)==0:
        print("X... give me a file as a parameter...")
        return None
    # ===== loading
    print(f"{fg.green}i... loading {args[0]}{fg.default}")
    config.object_list.append( args[0] )


if __name__=="__main__":
    Fire(main)
