#!/usr/bin/env python3
#
#  I want to use cmd_parser and call the functions with parameters BY "string cmdline parame"" like Fire()
#
#
from fire import Fire
import sys
from codeframe.version import __version__
from codeframe import config
from codeframe import cmd_parser
import os
from codeframe.config import  move_cursor
import subprocess as sp
from console import fg,bg
import glob
import shlex


# ===================================  all commands are in 2 main groups ===========
#                     shell (just pass to shell)
#                     local - each one needs to have its own module defined
# SHELL COMMANDS with files as parameters (ll is extended here)
KNOWN_COMMANDS_SHELL_FS = ['ls','ll','fdfind','head','tail','cat']
# other shell commands
KNOWN_COMMANDS_SHELL_OTHER = ['ag']
# call functions@fn_modules -  objects as parameters -  must be defined
KNOWN_COMMANDS_LOCAL = ['lo','show','zoom','unzoom','connect','reset']
# call functions@fn_modules - files as parameters
KNOWN_COMMANDS_LOCAL_FS = ['load']
#
# ============================================================================= summary
KNOWN_COMMANDS = KNOWN_COMMANDS_SHELL_FS + KNOWN_COMMANDS_LOCAL + KNOWN_COMMANDS_SHELL_OTHER + KNOWN_COMMANDS_LOCAL_FS


#============================================= prepare for completions =======================
# now create nested completion dict
KNOWN_COMMANDS_DICT = {}
for i in KNOWN_COMMANDS:
    KNOWN_COMMANDS_DICT[i]=None
# now create special completion for filemanagement
allfiles = glob.glob("*")
for i in KNOWN_COMMANDS_SHELL_FS+KNOWN_COMMANDS_LOCAL_FS:
    KNOWN_COMMANDS_DICT[i] = {}
    for j in allfiles:
        KNOWN_COMMANDS_DICT[i][j] = None
#========================================================== completions created...............
#print(KNOWN_COMMANDS_DICT)

def respond(inp):
    done = False
    while not done:
        res = mmapwr.mmread_n_clear( mmapwr.MMAPRESP ) # read response
        print(f".../{inp}/==/{res}/..")
        if res==inp:
            break
        time.sleep(1)


def exclude(cmd=""):
    """
    certain protection from malicious shell string...
    """
    bad = False
    if cmd.find("&")>=0:  bad = True
    if cmd.find("|")>=0:  bad = True
    if cmd.find("'")>=0:  bad = True
    if cmd.find('$')>=0:  bad = True
    if cmd.find('%')>=0:  bad = True
    if cmd.find('#')>=0:  bad = True
    if cmd.find('!')>=0:  bad = True
    if cmd.find('(')>=0:  bad = True
    if cmd.find(')')>=0:  bad = True
    if cmd.find(';')>=0:  bad = True
    #if cmd.find('"')>=0:  die() # for sed

    if bad:
        print( f"{fg.white}{bg.red}X... not allowed char in {cmd}", fg.default,bg.default)
    return bad


#==========================================================
# this does classically expansion - more files.....
#==========================================================
def interpolate_star( parlis ):
    """
    Full cmd.split() ... only files, not directories; NOT USED
    """
    cmd2 = []
    newcmd = []
    newcmd.append(parlis[0])
    for i in parlis:
        cmd2.append(i)
    for i in range(1,len(cmd2)):
        print(">>>",cmd2[i] )
        if '*' in cmd2[i]:
            for j in glob.glob( cmd2[i] ):
                if not os.path.isdir(j):
                    newcmd.append(j)
        else:
            newcmd.append(cmd2[i])
    return newcmd
#==========================================================
# this does creates iteratoin through *  - more files.....
#==========================================================
def iterate_star( parstring ):
    """
    kw2.... only files, not directories; USED FOR LOCAL_FSl NOTUSED TOOO
    """
    #def replace_wildcard_with_files(string_A):
    parts = shlex.split(parstring)
    expanded_parts = []
    for part in parts:
        if '*' in part:
            expanded_parts.extend(glob.glob(part))
        else:
            expanded_parts.append(part)
    return [' '.join(expanded_parts)]

    # cmd2 = parstring.split()
    # newcmd = []
    # for i in cmd2:
    #     newcmd.append(i)
    #     if '*' in i:
    #         for j in glob.glob( cmd2[i] ):
    #             if not os.path.isdir(j):
    #                 newcmd.append(j)
    #     else:
    #         newcmd.append(cmd2[i])
    # return newcmd

# =========================================================
#   shell (True or False...check it) run of the commands. with some basic protection
# =========================================================
def run_or_die( cmd , debug = False):
    """
    runs shell command. Iterates over * from filesystem
    """
    res = 0
    if exclude(cmd): return
    res = 0
    #print()
    if debug: print("Exe...", cmd)
    cmd2 = cmd.split()
    for i in range(len(cmd2)):
        #print(i, cmd2[i])
        cmd2[i] = cmd2[i].strip('"')
    newcmd = []
    newcmd.append( cmd2[0] )
    for i in range(1,len(cmd2)):
        # print(">>>",cmd2[i] )
        if '*' in cmd2[i]:
            for j in glob.glob( cmd2[i] ):
                newcmd.append(j)
        else:
            newcmd.append(cmd2[i])
    #print(cmd2)
    if debug: print("Exe...",  newcmd)
    try:
        res = sp.check_call( newcmd )#, shell = True)
        if debug: print("ok",res)
    except:
        res =1
        print(f"X... {fg.red} error running /{bg.white}{cmd}{bg.default}/{fg.default}")
    #print()
    #if res != 0: die("")
# =========================================================

def termline(txt):
    termsize3 = os.get_terminal_size().columns
    cont = f"#... ________ {txt} "
    cont = cont + "_"*(termsize3 - len(cont)-2)
    print(f"{fg.orange}{cont}{fg.default}")


# ==============================================================================================
# ==============================================================================================
# ==============================================================================================
# ==============================================================================================
def load( spectrum = None):
    """
    special case, load
    """
    # Your code here
    print("i... running command load INTERP", spectrum)
    return f"loaded"

def connect(dfname, from_=0, to=999999, display=False, savename=None, quest="meo"):
    # Your code here
    print("i... running command connect  INTERP")
    return f"conected"

def unzoom(dfname, from_=0, to=999999, display=False, savename=None, quest="meo"):
    # Your code here
    print("i... running command unzoom  INTERP")
    return f"unzoomed"

def zoom(dfname, from_=0, to=999999, display=False, savename=None, quest="meo"):
    # Your code here
    print("i... running command zoom  INTERP")
    return f"zoomed"
# ==============================================================================================
# ==============================================================================================
# ==============================================================================================
# ==============================================================================================


def main( cmd ):
    listcmd = cmd.split()
    kw1 = listcmd[0] #.split()[0]
    #
    # ======== I need to interpolate * for filesystem
    # if kw1 in KNOWN_COMMANDS_SHELL_FS or kw1 in KNOWN_COMMANDS_LOCAL_FS:
    #     print("D... FS interpol")
    #     listcmd = interpolate_star( listcmd) # only files, not directories
    kw2 = " ".join( listcmd[1:])
    #cmd = f"{kw1} {kw2}"
    #
    termline(cmd)
    match kw1:
        case 'reset':
            #print("RESET:",cmd,"    ")
            os.system("reset")
            move_cursor(3,1)
            return 1
        # case 'load':
        #     #print("LOAD:",cmd,"    ")
        #     return 2
        # case 'zoom':
        #     #print("ZOOM:",cmd,"    ")
        #     return 2
        # case 'unzoom':
        #     #print("UNZOOM:",cmd,"    ")
        #     return 2
        # case 'connect':
        #     #print("CONNECT:",cmd,"    ")
        #     return 2
        case _:
            # ====== SHELL COMMANDS (itteration of * from FS?)

            #if kw1 in KNOWN_COMMANDS_SHELL_OTHER:
            if kw1 in KNOWN_COMMANDS_SHELL_FS or kw1 in KNOWN_COMMANDS_SHELL_OTHER:
                # replace some commands
                if kw1=="ll": cmd = "ls -l "+kw2
                run_or_die(cmd)

            elif kw1 in KNOWN_COMMANDS_LOCAL: # zoom, show
                ### full control of cmd_parser ------- object list ----------
                ### func = getattr( cmd_parser, kw1) # WHEN ELSEWHERE
                ### --------- get the function from globals --------------------
                #func =  globals()[kw1] # WHEN HERE
                ### --------- HA! import a module fn_yrname
                func =  cmd_parser.str_func_to_func( kw1 )
                #func = func.main
                res = cmd_parser.call_function_with_command( func , kw2)
                for i in res: print("RES:",i) # print results

            elif kw1 in KNOWN_COMMANDS_LOCAL_FS:  # load
                ### ----- I need to do glob myself and call repetitively -------
                ### I try to import a module =======
                ###
                ### func = getattr( cmd_parser, kw1) # WHEN ELSEWHERE
                ### --------- get the function from globals --------------------
                #func =  globals()[kw1]
                ### --------- HA! import a module fn_yrname
                func =  cmd_parser.str_func_to_func( kw1 )
                # func = func.main

                # kw2_bis = iterate_star( kw2 )
                #for i in kw2_bis:
                res = cmd_parser.call_function_with_command( func , kw2, use_files=True)
                #for i in res: print("RES:",i) # print results

            else:
                print(f"{fg.red}X... unknown command /{cmd}/    {fg.default}")
            return 0   # 0 is the default case if x is not found
    pass
    #print()

if __name__=="__main__":
    Fire(main)
