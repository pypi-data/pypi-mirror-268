#!/usr/bin/env python3
"""
 These modules should contain one function each...
ls for the objects...

"""

from fire import Fire
from console import fg,bg
from codeframe import config


def main(*args,**kwargs):
    print(f"{fg.dimgray}D... main() @fn_lo: args/kwargs.../{args}/{kwargs}/{fg.default}")
    print(config.object_list)

if __name__=="__main__":
    Fire(main)
