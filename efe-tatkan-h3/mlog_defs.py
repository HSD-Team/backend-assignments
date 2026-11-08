import json

class InvalidCommandError(Exception): pass
class MemberNotFoundError(Exception): pass
class MemberExistsError(Exception): pass

class Memlist:
    
    """list containing members."""

    def __init__(self, i : list | None):
        self.members= []
        if i != None:
            self.members = i
        Memlist.init = True
        Memlist.glob = self

    @classmethod
    def classinit(cls):

        """initializes static class variables."""

        Memlist.init = False

    @classmethod
    def getglob(cls):

        """returns the global instance of the member list. creates one from file if it doesnt exist."""
        
        if Memlist.init:
            return Memlist.glob
        
        r = None
        try:
            try:
                with open("members.json", "r", encoding="utf-8") as f:
                    t = json.load(f)
                    if type(t) != list: raise TypeError("memlistjsondec")
                    for i in t:
                        if type(i) != str: raise TypeError("memlistjsondec")
                    r = t
            except (FileNotFoundError, json.JSONDecodeError):
                print("warning: no valid .json file was found. loading empty list.")
            except TypeError as e:
                if e.args[0] == "memlistjsondec":
                    print("warning: a valid .json file was found, but it's not compatible with this program. loading empty list.")
                else: raise
        except Exception as e:
            print(f"warning: opening the json file failed with {e=}, {type(e)=}. loading empty list.")

        return Memlist(r)

    def mempos(self, name : str, cr : bool = False) -> int | None:

        """get the index of a member within the list. insert entry if 'cr' is True and the member doesn't exist."""

        if not cr and len(self.members) == 0: raise MemberNotFoundError

        for i in range(len(self.members)):
            if name.lower() == self.members[i].lower(): 
                return i  
            if name.lower() < self.members[i].lower():
                if cr: 
                    self.members.insert(i, name)
                    return i
                else: raise MemberNotFoundError
        if cr: 
            self.members.append(name)
            return len(self.members) - 1
        else: raise MemberNotFoundError

