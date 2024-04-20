#!/usr/bin/env python3
"""
 Purpose is to have defined objects - LOCAL commands would work on these objects.
https://realpython.com/python-classes/#special-methods-and-protocols
#
https://stackoverflow.com/questions/12101958/how-to-keep-track-of-class-instances
#
each class keeps its own instances
"""
from fire import Fire
from weakref import WeakSet  # --------- weakset doeasnt survive  creation in other MOD and forgetting!!!!
from console import fg, bg
import itertools
import os
import pandas

class O_object(object):
    #instances = None
    #name = None
    #typ = None
    #@classmethod
    #def add_to_instance(cls, name, obj):
    #    O_object.instances[name] = obj

    def __new__(cls,name):
        """
        Keep list of instances (breaks with O_dataframes)
        Do not create existing name - return None
        """
        instance = object.__new__(cls)
        if "instances" not in cls.__dict__:
            #cls.instances = WeakSet()  # LIST SURVIVES MORE across  MODULES
            cls.instances = [] # WeakSet()
        names = [obj.get_name() for obj in cls.instances]
        if name in names:
            print(f"X... {fg.red}object /{name}/ already exists ... NOT CREATED{fg.default}")
            return None
        #cls.instances.add(instance)  # LIST SURVIVES MORE
        cls.instances.append(instance)
        return instance

    @classmethod
    def get_instances(cls):
        """
        works same as  .instances
        """
        return list(cls.instances) #Returns list of all current instances


    def __init__(self, name):
        self.name = name
        self.typ = "o" # useful when reading files o_  h_
        self.df_data = None


    def __str__(self): #dunder methods
        ln = 16-len(self.name)
        ss = " "*ln
        return f"s... Object name is  /{fg.green}{self.name}{fg.default}/ {ss} of type /{self.typ}/"

    #--------- I like to see the address.....
#    def __repr__(self): # for debugging.... they say
#        return f"{type(self).__name__}(\"{self.name}\")"

    def get_name(self):
        return self.name

    def get_type(self):
        return self.typ

    def read_from_file(self,filename):
        """
        fill pandas dataframe - for spectrum and for asc
        """
        base = os.path.splitext(filename)[0]
        self.name = f"{self.typ}_{base}"
        print(f"i... opening file /{fg.yellow}{filename}{fg.default}/ and naming /{fg.green}{self.name}{fg.default}/")
        self.df_data = pandas.read_csv(filename)
        print(f"i... ... ... ... ... ... ... data loaded. LEN={len(self.df_data)}")
        return


    @classmethod
    def from_file(cls, filename):
        """
         # create new object from something =O_object.create_from()
        """
        a = cls("tmp")
        a.read_from_file(filename)
        return a

    @staticmethod
    def abouts():
        print(f"h... About: this is a static method of either O_object or its daugters..." )

    @classmethod
    def about(cls):
        """
        # access to class name
        """
        print(f"h... About: this is a class {cls.__name__}...")

# ================================================ ******************************************************************************
# ================================================ ******************************************************************************
# ================================================ ******************************************************************************


class O_histogram(O_object):
    def __init__(self, name):
        super().__init__(name)
        self.typ = "h"

#    def __repr__(self):
#        return f"O_histogram({self.name})"

# ================================================ ******************************************************************************
# ================================================ ******************************************************************************
# ================================================ ******************************************************************************

class O_dataframe(O_object):
    def __init__(self, name):
        super().__init__(name)
        self.typ = "d"

# ================================================ ******************************************************************************
# ================================================ ******************************************************************************
# ================================================ ******************************************************************************

def list_objects():
    """
    LIST
    """
    for i in get_objects_list():# WeakSet(itertools.chain(   O_dataframe.instances,O_histogram.instances   )):
        print(i)

def get_objects_list_names():
    SS = get_objects_list()
    names = [obj.get_name() for obj in SS]
    return names

def get_objects_list():
    """
    LIST OF histograms and dataframes together
    """
    A = "instances" in O_dataframe.__dict__
    B = "instances" in O_histogram.__dict__

    #print("A x B ... ", A,B )

    # LISTS --------
    if A and (type(O_dataframe.instances) != WeakSet) and B:
        return O_dataframe.instances + O_histogram.instances
    if A and (type(O_dataframe.instances) != WeakSet) :
        return O_dataframe.instances
    if B and (type(O_histogram.instances) != WeakSet) :
        return O_histogram.instances
    # --------- WeakSet
    if A and B :
        #LI = list( WeakSet(itertools.chain(   O_dataframe.instances,O_histogram.instances   )) )
        LI = list( itertools.chain(   O_dataframe.instances,O_histogram.instances   ))
        #print(LI)
        return LI
    if A  :
        return list( WeakSet(itertools.chain(   O_dataframe.instances   )) )
    if B  :
        return list( WeakSet(itertools.chain(   O_histogram.instances   )) )
    return []


def object_exists( name ):
    """
    check LIST OF histograms and dataframes together
    """
    SS = get_objects_list()
    names = [obj.get_name() for obj in SS]
    if name in names: return True
    return False

# ================================================ ******************************************************************************
# ================================================ ******************************************************************************
# ================================================ ******************************************************************************

def main():
    print( get_objects_list() )
    print()
    o1 = O_object("o1")
    o2 = O_object("o1")

    h1 = O_histogram("h1")
    h2 = O_histogram.from_file("hpge_b0c00.asc")

    d1 = O_dataframe("d1")
    d2 = O_dataframe("d2")

    print("-"*50, 'all defined')

    #print(o1)
    print(h1)
    print(h2)
    print(d1)

    print("repr..h1",repr(h1))
    print("c... call:", h1.get_name() ,"X", h1.get_type() )
    print("c... call:", getattr(h1,"name") ,"X", getattr(h1,"typ") )
    print("c... call:", h1.name ,"X", h1.typ )
    print("c... call:", d1.name ,"X", d1.typ )
    print( "d1repr... ",repr(d1) )

    print("-"*50," print some d1 ")
    h1.about()
    h2.about()
    h2.abouts()
    d1.about()


    print("-"*50," LISTING INSTANCES -  every class has its own list")
    # for i in  O_histogram.instances:
    #     print("#Histo#  printed name: ",i.get_name(), i.get_type() )
    #     i.about()
    # print()

    # for i in  O_object.get_instances():
    #     print("~Object~  printed name: ",i.get_name(), i.get_type() )
    #     i.about()
    # print()

    # for i in O_dataframe.get_instances():
    #     print("`Datafr`  printed name: ",i.get_name(), i.get_type() )
    #     print( repr(i))
    #     i.about()

    # print(  "i...  instances are of type :",  type(O_dataframe.instances)  )
    # # if type(O_dataframe.instances) == "<class '_weakrefset.WeakSet'>":
    # if type(O_dataframe.instances) != WeakSet:
    #     print("-"*50," LISTING SUM OF INSTANCES")
    #     for i in O_dataframe.instances+O_histogram.instances:
    #         print(i)

    list_objects()



    #print(O_histogram.instances) # CRASHES, only classmethod can be called

if __name__ == "__main__":
    Fire(main)
