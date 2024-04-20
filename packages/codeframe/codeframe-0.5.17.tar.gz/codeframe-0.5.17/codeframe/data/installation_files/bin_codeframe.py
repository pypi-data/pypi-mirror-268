#!/usr/bin/env python3

# to override print <= can be a big problem with exceptions
#
# colors in df_table _fg _bg columns:
# see
# https://github.com/mixmastamyk/console/blob/master/console/color_tables_x11.py#L112
#
# from __future__ import print_function  # must be 1st
# import builtins
import sys
from fire import Fire
from codeframe.version import __version__
# from codeframe import unitname
from codeframe import config
from codeframe import topbar
from codeframe import key_enter
from codeframe import installation
# from codeframe  import df_table
from codeframe.df_table import create_dummy_df, show_table, \
    inc_dummy_df
from codeframe.config import move_cursor
from codeframe import mmapwr
from codeframe import interpreter

import time
import datetime as dt
from console import fg, bg, fx
from blessings import Terminal
import os
from pyfiglet import Figlet
import signal

# ====================== for separate terminal keyboard using mmap

from prompt_toolkit import PromptSession, prompt
from prompt_toolkit.history import FileHistory

from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.completion import NestedCompleter

from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

# ========================
SHOW_LOGO_TABLE = False
SHOW_TIME = False
SHOW_COMMAND_LINE = True
RUN_MMAP_INPUT = True  #  INTERACTIVE MMAP-INTERACTIVE
RUN_SELECT_FROM_TABLE = False

termsize = os.get_terminal_size().columns

# import pandas as pd
# import numpy as np
# from terminaltables import SingleTable

# ------- this defended the project from winch error
# from simple_term_menu import TerminalMenu


def handle_sigwinch(signum: signal.Signals, qqq):
    # pylint: disable=unused-argument
    #print("WINCH SIGNAL:",type(qqq), qqq)
    #os.system("reset")
    return None


# ----this DOES IT
#  for FONTS in `pyfiglet -l`; do echo $FONTS; pyfiglet $FONTS -f $FONTS; done | less
figlet = Figlet(font="slant")
# figle2 = Figlet(font="roman")
# figle2 = Figlet(font="standard")
figle2 = Figlet(font="ansi_regular")


def print_logo():
    """
    print fromt page + time
    """
    global termsize
    # global figlet, filg

    word = " codeframe"
    # os.system('reset')
    print("")
    print(figlet.renderText(word))
    print(figle2.renderText(dt.datetime.now().strftime("%H:%M:%S ")))
    print(
        f"DO YOU WANT TO INSTALL ME ?... Run me with your  \
{fg.green}'projectname'{fg.default} as a parameter"
    )
    print("do you want to quit ?  type '.q'  ")
    #print(f"    terminal width = {termsize} {os.get_terminal_size().columns}")

def autoreset_terminal():
    global termsize
    termsize2 = os.get_terminal_size().columns
    #print("TS???", termsize, termsize2)
    if termsize != termsize2:
        print("i... RESET TERMINAL")
        os.system("reset")
        #terminal.clear()
        termsize = termsize2
        move_cursor(3, 1)
        #print("X")

def main(projectname=None, debug=False, keyboard_remote_start = False, servermode = False, logo = False):
    """
    Main function of the project. When 'projectname' given: new project is created

    Parameters:
    projectname: THIS WILL GENERATE NEW PROJECT with these modules
    keyboard_remote_start: just start a standalone prompt
    servermode: wait for commands via mmap... to be used with -k
    """
    global RUN_SELECT_FROM_TABLE, SHOW_LOGO_TABLE, SHOW_TIME, RUN_MMAP_INPUT

    SHOW_LOGO_TABLE = logo
    SHOW_TIME = logo

    if not servermode: RUN_MMAP_INPUT = False
    # GLobal clear terminal
    if debug:
        print(__version__)
    #else:

    signal.signal(signal.SIGWINCH, handle_sigwinch)

    # ======== DEFINE THE CONFIG FILE HERE ========

    config.CONFIG["filename"] = "~/.config/codeframe/cfg.json"
    config.CONFIG["history"] = "~/.config/codeframe/history"
    # solely LOAD will create ....from_memory files
    # config.load_config()
    # solely  SAVE will create cfg.json only
    # config.save_config()

    # ==================================================== #########################
    # ==================================================== ######################### remote
    # ==================================================== #########################
    #               command prompt - separate thread
    # ==============================================================================
    if keyboard_remote_start:
        #prompt_completer = WordCompleter( interpreter.KNOWN_COMMANDS )
        prompt_completer = NestedCompleter.from_nested_dict( interpreter.KNOWN_COMMANDS_DICT )

        multilineinput = False
        config.myPromptSession = PromptSession(
            history=FileHistory( os.path.expanduser(config.CONFIG["history"]) )
        ) #, multiline=Trueinp
        inp = ""
        myname = os.path.splitext(os.path.basename(__file__))[0]

        print(f"i...  input interface to {fg.orange}{myname}{fg.default} application. .q to quit all; .h to help.")
        while (inp!=".q"):
            inp = config.myPromptSession.prompt("> ",
                                                multiline=multilineinput,
                                                completer=prompt_completer,
                                                complete_while_typing=False,
                                                wrap_lines=True, # no noew lines
                                                mouse_support=False,  # i want middlemouse
                                                auto_suggest=AutoSuggestFromHistory()
                                                )
            if inp==".h":
                print("H...  HELP:")
                print("H...  .t   table+logo")
                print("H...  .d   disable logo and time")
                print("H...  .r   reset terminal")
                print("H... known commands: ", "  ".join(interpreter.KNOWN_COMMANDS )  )
            elif inp==".q":
                mmapwr.mmwrite(inp)
            else:
                # print(f" >>>Write {inp} to the")
                mmapwr.mmwrite(inp)
                done = False
                ii = 1
                while not done:
                    # res = mmapwr.mmread(  ) # read response
                    ii+=1
                    res = mmapwr.mmread_n_clear( mmapwr.MMAPRESP  )
                    res = res.strip() # strin newline
                    if ii%2==0:
                        print("w", end="\r", flush=True)
                    else:
                        print("W", end="\r", flush=True)
                    #print(f"... input was /{inp}/==/{res}/..result of read   len(inp):", len(inp), "  ...res:",len(res) )
                    if res.strip()==inp.strip():
                        #print(f" YES::::.../{inp}/==/{res}/.. ?")
                        done = True
                    #else:
                    #    print(f" NONO:::.../{inp}/==/{res}/.. ?")
                    time.sleep(0.25)
                #print("... konec prikazu")


        # print(inp)
        return
    # ==================================================== #########################
    #           command prompt - separate thread
    # ==================================================== #########################
    # ==================================================== #########################


    if projectname is None:
        print()
    elif projectname == "usage":
        print(
            """ ... usage:
            _
        """
        )
        sys.exit(0)
    # ----------------------- installation with this name ----------
    else:
        installation.main(projectname)
        sys.exit(0)

    # ===================== top bar and commads from kdb ==========
    os.system("reset")
    # when I put reset later, it occludes the 1st red inpput command
    top = topbar.Topbar(bgcolor=bg.blue)
    top2 = top.add(bgcolor=bg.black)

    top.print_to(
        10,
        f" {fg.white}{fx.bold}{dt.datetime.now().strftime('%H:%M:%S')}\
{fx.default}{fg.default} ",
    )
    top.place()
    # start after top

    # ========================= INITIAL cmd key setting....
    cmd = ""
    enter = False
    key = None
    a, b = (" ", " ")

    # KEYTHREAD THIS MUST BE HERE.....toi catch 1st letter
    #   only return         key, enter, abc = kthread.get_global_key()
    #                       key:mayreact on q;     enter==hit ; abc=>(a,b) for display.
    kthread = None
    if RUN_MMAP_INPUT:
        # THis goes when mmap active
        #print("i...   MMAP ACTIVE ...........................")
        kthread = key_enter.MmapSimulatedKeyboard(ending=".q")
    else:
        #print("D...    MMAP NOT ACTIVE, using SSHKEYB.............")
        kthread = key_enter.KeyboardThreadSsh(ending=".q")
    # whatabout to have other terminal feeding mmapfile
    #

    df = create_dummy_df()
    terminal = Terminal()
    selection = None
    #terminal.clear()
    move_cursor(3, 1)
#################################################################
    #          L O O P
    #################################################################
    while True:  # ================================= LOOP

        autoreset_terminal()
        if (SHOW_LOGO_TABLE):
            terminal.clear()
            move_cursor(3, 9)
            if SHOW_TIME:
                print_logo()

            # time.sleep(0.05)
            show_table(df, selection)
        #
        # RUN OPERATION ON TABLE
        #
        df = inc_dummy_df(df)

        key, enter, abc = kthread.get_global_key()
        (a, b) = abc  # unpack tuple

        if enter:
            #print()
            #print("--------------------------------------ENTER pressed")
            if len(key.strip()) == 0:
                pass
            elif key.strip() == ".q":
                break
            else:
                cmd = key.strip()
                # ======================================================== INTERPRETER
                if cmd==".t":
                    SHOW_LOGO_TABLE = not SHOW_LOGO_TABLE
                elif cmd==".d":
                    SHOW_TIME = not SHOW_TIME
                elif cmd==".r":
                    os.system("reset")
                    move_cursor(3,1)
                else:
                    print("...calling interpreter")
                    interpreter.main( cmd )
                if RUN_SELECT_FROM_TABLE:
                    # list of row numbers from column 'n' :  assume whole word is list of rows:
                    if selection is not None and selection != "":
                        selection = ""
                    else:
                        selection = cmd
                # ======================================================== INTERPRETER
            #print(f"----------- {cmd}; table_selection:{selection}--------------------- ***")
            #print("...writeback try", key)
            mmapwr.mmwrite( key , mmapwr.MMAPRESP)
            #print("...writeback done",key)
        else:
            cmd = ""

        top.print_to(
            10,
            f" {fg.white}{fx.bold}{dt.datetime.now().strftime('%H:%M:%S')}\
{fx.default}{fg.default}",
        )

        #
        #  commandline at TOP#2, cursor  a_b; option not to show
        #
        if (not SHOW_COMMAND_LINE) or (  (key is not None) and (len(key) == 0) ):
            top2.print_to(0, f"{fg.cyan}{bg.black}{' '*termsize}{bg.black}")
        else:
            top2.print_to(
                0,
                f"{fg.white}{bg.red} > {fx.bold}{a.strip()}{fg.yellow}_{fg.white}{b.strip()}\
{fx.default}{fg.default}{bg.default} ",
            )

        # PLACE THE TOPBAR INPLACE
        top.place()
        time.sleep(0.1)


# ====================================================================


if __name__ == "__main__":
    Fire(main)
