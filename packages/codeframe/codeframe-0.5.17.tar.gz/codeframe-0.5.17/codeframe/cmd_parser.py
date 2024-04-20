#!/usr/bin/env python3
#
# ----------  calling functions with parameters usin strings - way like Fire()
# done using GPT4
#
#
import shlex
import inspect
import fnmatch
from codeframe.version import __version__
from codeframe import config
from codeframe import objects
#from codeframe.config import object_list
from console import fg,bg
import glob
#
#import importlib_resources
import importlib
import sys
import os
#from importlib import import_module
#
# Assuming dflist is a global variable

#config.object_list = ['df1', 'df2', 'df3', 'd11', 'd21','h11']

#############################################################
#
#############################################################





# ---------------------------------------------------------------
def listpy( pretext="fn_", also_local = False, DEBUG = True):
    """
    return all pr_*.py files (in the current directory) (in repo dir)
    """
    files = []
    filescur = []
    dirnow = os.getcwd()
    # GO TO repo
    tgt2 = os.path.dirname(os.path.abspath(__file__))
    if DEBUG: print(f"{fg.dimgray}D... looking at {tgt2} {fg.default}")
    os.chdir( tgt2 )
    files = glob.glob(f"{pretext}*.py")
    if len(files)==0:
        print(f"{fg.red}X... NO python FILES available (@listpy() ){fg.default}")
        return None
    # files = [x for x in files if x.find("pr_model_")!=0] # models- I exclude?
    #print("REPO:",tgt2) # I forgot to link inside the repo
    #print("REPO",files)
    corenames = [ os.path.splitext(x)[0].split( pretext )[1] for x in files]
    #print(f"i... modules available in REPO:\n          {corenames}")
    files = [ tgt2+"/"+x for x in files ]
    #- GO back from repo
    os.chdir( dirnow )

    #print("D... looking current dir")
    if also_local:
        filescur = glob.glob(f"{pretext}*.py")
    # print(f"i... curdir: {filescur}")
    if len(filescur)==0:
        #pass #asdqwe541 = 1
        if DEBUG: print(f"{fg.dimgray}D... NO python FILES available in current directory (listpy){fg.default}")
        # return None
        #files = filescur
    else:
        corenames = [ os.path.splitext(x)[0].split(pretext)[1] for x in filescur]
        if DEBUG: print(f"{fg.dimgray}D... modules available in CURR: {fg.default} {corenames}")
        # files = [x for x in files if x.find("pr_model_")!=0] # models- I exclude?
        files =  files + filescur
        if DEBUG: print(f"{fg.dimgray}D... modules available:{fg.default} {files}")
    return files





#############################################################
#
#############################################################




# ---------------------------------------------------------------
def my_import_module(intit, pretext="fn_", also_local_files = False, DEBUG = True):
    """
    taken from prun.py - load (unload first) a module from the package (even local file)
    """

    files = listpy( also_local = also_local_files) # get all modules available
    if files is None:
        print(f"{fg.red}X... no loadable modules found....(@my_import_module){fg.default}")
        return None

    # print(files) # all present files
    # print(intit) # module
    module = None
    for ffile in files:
        # ffile may be with a path....
        construct = ffile
        if len(ffile.split("/"))>1:
            construct = construct.split("/")[-1]
        construct =  construct.lstrip(pretext)
        # print(construct)
        construct =  construct.rstrip("py")[:-1] # prioblem w .py
        # print(construct)
        ##print(f" ... searching /{intit}/ in /{ffile}/ <={construct}")
        # this was the last searching
        #print(f" ... searching /{intit}/ in {ffile} ")

        if (intit == construct):
            #print(f"P... got {ffile}")
            #print("i... trying to importlib:", item.GetTitle() )
            # UNimport module first - case there was an error there previously
            unloadname = f"{pretext}{intit}"
            if DEBUG: print(f"{fg.dimgray}D... module /{unloadname}/ ... {fg.default}", end="")
            try:
                sys.modules.pop( unloadname ) # ffile[:-3]     f"pr_{construct}")
                if DEBUG: print(f"{fg.dimggray}... unloaded successfully, loading now...{fg.default}")
            except:
                if DEBUG: print(f"{fg.dimgray}... not unloaded, loading now...{fg.default}")

            # IMPORT
            #print("D... importing module")
            #module = importlib.import_module( ffile[:-3] ) # older

            spec = importlib.util.spec_from_file_location( pretext+intit, ffile )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if DEBUG: print(f"{fg.dimgray}D... importing module DONE{fg.default}")
            #break

    return module
# ---------------------------------------------------------------




#############################################################
#
#############################################################





#############################################################
#
#############################################################

def str_func_to_func(sfunc = ""):
    """
    """
    # current_module1 = sys.modules[__name__]
    # print(current_module1)
    # current_module2 = __import__(__name__)
    # print(current_module2)

    #this_pkg = sys.modules[__package__]
    #print(this_pkg)

    if len(sfunc)=="":
        print(f"{fg.red}X... no function name given for search... {fg.default}")
        return None

    # mod2search = f"fn_{sfunc}"
    current_module3 = my_import_module(sfunc,  pretext="fn_", also_local_files=False)
    # print(current_module3)
    #if current_module3 is not None:
    #    current_module3.main()
    return current_module3.main


#############################################################
#
#############################################################

def call_function_with_command(func, command, use_files=False, DEBUG=True):
    """
    provide "func" as the real function and inspect its parameter set
    """
    tokens = shlex.split(command)
    ok = False
    try:
        sig = inspect.signature(func)
        #print("D... these are the revealed parameters... ",sig)
        ok = True
    except:
        print(f"{fg.red}X... NO FUNCTION seen like {fg.default}",func,"...",command)
        ok = False
    if not ok : return []
    args = []
    kwargs = {}
    results = []

    if len(tokens)==0:
        results.append( func() )
        return results

    it = iter(tokens)
    print(f"{fg.dimgray}D... tokens:{fg.default}", tokens)
    for token in it:
        if token.endswith('*') or '*' in token:
            # Handle the pattern matching by deferring execution until later
            args.append(token)
        elif token.startswith('-'):
            # Remove the '-' prefix
            flag = token.lstrip('-')
            value = next(it, None)
            # Attempt to match the flag to known parameters
            matched_params = [p for p in sig.parameters if p.startswith(flag)]
            if not matched_params:
                print(f"X... ERROR - unknown flag {token}")
                return []
                raise ValueError(f"Unknown flag: {token}")
            if len(matched_params) > 1:
                print(f"X... ERROR - ambiguous flag {token}")
                return []
                raise ValueError(f"Ambiguous flag: {token}")
            param_name = matched_params[0]
            param = sig.parameters[param_name]
            # Convert the value to the correct type based on the default value
            if param.default is not inspect.Parameter.empty and param.default is not None:
                if isinstance(param.default, bool):
                    value = value.lower() in ('true', 'yes', '1')
                else:
                    value = type(param.default)(value)
            elif param.default is None:
                # If the default is None, we keep the value as a string
                pass
            kwargs[param_name] = value
        else:
            if DEBUG: print(f"{fg.dimgray}D... appending {fg.default}", token)
            args.append(token)

    for pattern in args:
        if DEBUG: print(f"{fg.dimgray}D... working on arg:{fg.default}", pattern)
        matching_dfs=[]
        # Run the function for each dataframe in config.object_list that matches the pattern
        if use_files:
            if DEBUG: print(f"{fg.dimgray}D... interpreting pattern as a file:{fg.default}", pattern)
            matching_dfs = glob.glob( pattern )
            if len(matching_dfs)==0:
                print(f"{fg.red}X... no files match /{pattern}/{fg.default}")
        elif objects.object_exists( pattern ): #pattern in objects.get_objects_list():
            if DEBUG: print(f"{fg.dimgray}D... argument /{pattern}/ IS  in the list of allowed objects{fg.default}")
            matching_dfs = fnmatch.filter(objects.get_objects_list_names(), pattern)
            if len(matching_dfs)==0:
                print(f"{fg.red}X... no objects match /{pattern}/{fg.default}")
        else:
            print(f"{fg.red}X... argument /{pattern}/ IS NOT in the list of allowed objects:{fg.default}", objects.get_objects_list() )
        #
        for dfname in matching_dfs:
            # Substitute '$' with the dataframe name for all kwargs
            modified_kwargs = {k: v.replace('$', dfname) if isinstance(v, str) and '$' in v else v
                               for k, v in kwargs.items()}
            try:
                results.append(func(dfname, **modified_kwargs))
            except:
                print(f"X... function {func}({command}) crashed")
    return results




# Example function
def cut(dfname, from_=0, to=999999, display=False, savename=None, quest="meo"):
    # Your code here
    print("i... running command cut")
    return f"cut({dfname}, from_={from_}, to={to}, display={display}, savename='{savename}' quest='{quest}')"


# ==============================================================================================
# ==============================================================================================
# ==============================================================================================
# ==============================================================================================
# def load( spectrum = None ):
#     # Your code here
#     print("i... running command load")
#     return f"loaded"

# def connect(dfname, from_=0, to=999999, display=False, savename=None, quest="meo"):
#     # Your code here
#     print("i... running command connect")
#     return f"conected"

# def unzoom(dfname, from_=0, to=999999, display=False, savename=None, quest="meo"):
#     # Your code here
#     print("i... running command unzoom")
#     return f"unzoomed"

# def zoom(dfname, from_=0, to=999999, display=False, savename=None, quest="meo"):
#     # Your code here
#     print("i... running command zoom")
#     return f"zoomed"




if __name__ == "__main__":
    # Example usage:
    command = "d*1 -f 10 -t 20 -s bis_$.txt"
    command = "d*1 -f 10 -t 20 -q 'Hi! $_bis; ls $_bis' -s $.txt"
    results = call_function_with_command(cut, command)
    for result in results:
        print(result)  # Output will be the string representation of the function call for each matching dataframe
    str_func_to_func("load")
