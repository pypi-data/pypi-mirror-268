#!/usr/bin/env python3
"""
 These modules should contain one function each...


"""

from fire import Fire
from console import fg,bg
from codeframe import config
from codeframe import objects


def main(*args,**kwargs):
    print(f"{fg.dimgray}D... main() @fn_lo: args/kwargs.../{args}/{kwargs}/{fg.default}")
    #print(f"D... main() @fn_show: args/kwargs.../{args}/{kwargs}/")
    if len(args)==0:
        print("D...  give me an object: allowed objects:",objects.get_objects_list() )
    oname = args[0]
    if objects.object_exists(oname):
        print(f"{fg.green}i... showing {oname}{fg.default}")
    else:
        print(f"i... {fg.red} NOT showing {oname}{fg.default}")


if __name__=="__main__":
    Fire(main)
