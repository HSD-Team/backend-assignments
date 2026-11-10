import json

class ItemNotFoundError(Exception): pass
class ItemExistsError(Exception): pass
class InvalidJSONFormatError(Exception): pass

class JList:
    
    """generalized json list with automatic alphabetical ordering, 
    designed to be used with multiple instances."""

    def __init__(self, name : str, _init : list | None):
        self.list= []
        if _init != None:
            self.list = _init
            self.name = name

    def loadFromFile(self, _filename : str) -> None:

        """initialize the list from a formatted json file."""

        try: 
            with open(_filename, "r") as f:
                j = json.load(f)
                try:
                    e = j[self.name]
                    if(type(e) == list): #the entry associated with the item must be a list
                        for o in e:
                            try: o["id"] #entries in the list must be dictionaries with the key "id"
                            except (KeyError, TypeError): raise InvalidJSONFormatError 
                        self.list = j[self.name]
                        return
                    else:
                        raise InvalidJSONFormatError
                except KeyError:          #if the json file doesnt have an entry for this item, create it
                    j[self.name] = []
                    self.list = []
                    return
                except (InvalidJSONFormatError, TypeError) as e:
                    e.add_note("the entry in the given file corresponding to this JList object was not a proper list.")
                    raise
        except (FileNotFoundError, json.JSONDecodeError) as e:  #if the file couldnt be found
            e.add_note("json file not found, or is invalid.")
            raise

    def itemPos(self, id : str) -> int | None:

        """get the index of an item within the list. throw an exception if its not listed."""

        if len(self.list) == 0: raise ItemNotFoundError(0)

        for i in range(len(self.list)):
            k = self.list[i]
            if id.lower() == k["id"].lower(): 
                return i
            if id.lower() < k["id"].lower():
                raise ItemNotFoundError(i)   #report the failed index number for insertion operations

    def addItem(self, item : dict) -> None:

        """add a new item to the list, throw ItemExistsError if that exact item is already listed, 
        or replace the old item if the new version has been modified."""

        try: 
            i = self.itemPos(item["id"])
            if i == None: i = 0
            if item == self.list[i]:
                raise ItemExistsError(i)       #items are the same, throw exception
            else: self.list[i] = item          #replace item
        except ItemNotFoundError as e:
            self.list.insert(e.args[0], item)  #item doesnt exist, insert in the list