"""Function handlers."""
import json


def disabledFunction(*args, **kwargs):
    """Blank function template to replace disabled functions."""
    rdict = {}
    rdict["function_status"] = "Function disabled!"
    rdict["return_code"] = -1
    return json.dumps(rdict)


class Functions:
    """Functions handler."""

    def __init__(self):
        """Initialize the Functions object."""
        self.fstatuses = {}
        self.functions = {}
        self.descriptions = {}
        self.groups = {}

    def funExists(self, fname):
        """Return True if the function exists."""
        if fname in self.fstatuses.keys():
            return True
        return False

    def addFunction(self, function, description):
        """Add a function to the object."""
        fname = description.get("name", "")
        if (not fname) or (self.funExists(fname)):
            return False
        self.fstatuses[fname] = True
        self.functions[fname] = function
        self.descriptions[fname] = description
        return True

    def connectFunction(self, fname, function):
        """Connect a function."""
        if not self.funExists(fname):
            return False
        self.fstatuses[fname] = True
        self.functions[fname] = function
        return True

    def removeFunction(self, fname):
        """Remove a function from the object."""
        if not self.funExists(fname):
            return False
        self.fstatuses.pop(fname)
        self.functions.pop(fname)
        self.descriptions.pop(fname)
        return True

    def disableFunction(self, fname):
        """Disable a function."""
        if not self.funExists(fname):
            return False
        self.fstatuses[fname] = False
        return True

    def enableFunction(self, fname):
        """Enable a function."""
        if not self.funExists(fname):
            return False
        self.fstatuses[fname] = True
        return True

    def addGroup(self, gname, fnames):
        """Add a function group."""
        self.groups[gname] = fnames
        return True

    def removeGroup(self, gname):
        """Remove a function group."""
        if gname not in self.groups.keys():
            return False
        self.groups.pop(gname)
        return True

    def enableGroup(self, gname):
        """Enable a function group."""
        for fname in self.groups.get(gname, []):
            self.enableFunction(fname)

    def disableGroup(self, gname):
        """Disable a function group."""
        for fname in self.groups.get(gname, []):
            self.disableFunction(fname)

    def getFunction(self, fname):
        """Get a function."""
        if self.fstatuses.get(fname, False):
            return self.functions.get(fname, disabledFunction)
        return disabledFunction

    def getEnabled(self):
        """Get enabled functions."""
        descs = []
        for fname, desc in self.descriptions.items():
            if self.fstatuses.get(fname, False):
                descs.append(desc)
        return descs

    def append(self, other, gname=""):
        """Append other Function handlers as group?."""
        for other_gname, other_group in other.groups.items():
            self.addGroup(other_gname, other_group)
        group = []
        for fname, status in other.fstatuses.items():
            group.append(fname)
            self.addFunction(
                other.functions.get(fname, disabledFunction),
                other.descriptions.get(fname, {
                    "name": fname,
                    "description": "a disabled function",
                    "parameters": {
                        "type": "object",
                    },
                })
            )
            if not status:
                self.disableFunction(fname)
        if gname:
            self.addGroup(gname, group)
        return self
