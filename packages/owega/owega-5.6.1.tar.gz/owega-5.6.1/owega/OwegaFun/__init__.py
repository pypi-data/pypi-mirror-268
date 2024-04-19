"""Owega Functions init."""
from .utility import Utility
from . import longTermSouvenirs as lts
# from .longTermSouvenirs import LTS, setAdd, setDel, setEdit
from .functions import Functions

existingFunctions = Functions().append(
    Utility, 'utility').append(lts.LTS, 'lts')
existingFunctions.disableGroup('lts')


def connectLTS(addfun, delfun, editfun):
    """Connect Long-Term-Souvenir functions."""
    lts.setAdd(addfun)
    lts.setDel(delfun)
    lts.setEdit(editfun)
    existingFunctions.enableGroup('lts')


def function_to_tool(fun):
    """Convert an old function to a tool."""
    dct = {}
    dct["type"] = "function"
    dct["function"] = fun
    return dct


def functionlist_to_toollist(fun_lst):
    """Convert a old functions as a tools."""
    tool_lst = []
    for fun in fun_lst:
        tool_lst.append(function_to_tool(fun))
    return tool_lst
