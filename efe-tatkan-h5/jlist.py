import json
from urllib.parse import unquote

class ItemNotFoundError(Exception): pass
class ItemExistsError(Exception): pass
class InvalidJSONFormatError(Exception): pass
class EmptyIDError(ValueError): pass

class JList:
    
    """generalized json list with automatic alphabetical ordering, 
    designed to be used with multiple instances."""

    def __init__(self, name : str, _init : list | None = None):
        self.list= []
        if _init != None:
            self.list = _init
        self.name = name.lower()

    def loadFromFile(self, _filename : str) -> None:

        """initialize the list from a formatted json file."""

        try: 
            with open(_filename, "r", encoding="utf-8") as f:
                j = json.load(f)
                try:
                    e = j[self.name]
                    if(type(e) == list):                            #the entry associated with the item must be a list
                        for o in e:
                            try: o["id"]                            #entries in the list must be dictionaries with the key "id"
                            except (KeyError, TypeError): raise InvalidJSONFormatError 
                        self.list = j[self.name]
                        return
                    else:
                        raise InvalidJSONFormatError
                except KeyError:                                    #if the json file doesnt have an entry for this item, create it
                    j[self.name] = []
                    self.list = []
                    return
                except (InvalidJSONFormatError, TypeError) as e:
                    e.add_note("the entry in the given file corresponding to this JList object was not a proper list.")
                    raise
        except (FileNotFoundError, json.JSONDecodeError) as e:      #if the file couldnt be found
            e.add_note("json file not found, or is invalid.")
            raise

    def itemPos(self, id : str) -> int | None:

        """get the index of an item within the list. throw an exception if its not listed."""

        if id == "": raise EmptyIDError("'id' can't be an empty string. this error is most likely caused by an invalid value given to a model.")

        c_ind = 0
        l_ind = 0

        #iteratively compare each character in input and the list item, return where the input is (or should be inserted)
        while True:

            if l_ind == len(self.list):
                #this automatically breaks the execution if the list index is at the end of the list. 
                break
            elif c_ind >= len(self.list[l_ind]["id"]):
                l_ind+=1
                c_ind = 0                           #reset the character index to prevent leaks after size mismatch
                continue
            else:
                c = unquote(id)[c_ind]
                ic = self.list[l_ind]["id"].lower()[c_ind]

            if c > ic:
                l_ind+=1                            #no match, check the next item in the list
            elif c == ic:
                c_ind+=1                            #the characters match. we can move on to the next character
                if c_ind == len(unquote(id)):
                    if c_ind == len(self.list[l_ind]["id"]):
                        #if there are no more characters left to match, and the input and item strings are the same length; the input has been found.
                        return l_ind                #return the current list index.
                    break
            elif c < ic: 
                #this item and the others after it come after the input alphabetically. if we reached here, the input is not in the list.
                break
                
        #report the failed index number for insertion operations
        raise ItemNotFoundError(f"the given item with the id '{id}' ({unquote(id)}) was not found. itemPos() stopped checking at index {l_ind}.", l_ind)

            
    def addItem(self, item : dict) -> None:

        """add a new item to the list, throw ItemExistsError if an item with the same id is already listed."""

        try: 
            i = self.itemPos(item["id"])
            #item's id string is already in the list. adding fails.
            raise ItemExistsError(f"the given item with id '{item["id"]}' conflicts with another item in this list at index {i}.", i)
        except ItemNotFoundError as e:
            self.list.insert(e.args[1], item)          #item doesnt exist, insert in the list

    def modifyItem(self, item : dict) -> None:

        """modify an already existing item in the list. itemPos throws ItemNotFoundError if it isn't listed."""

        i = self.itemPos(item["id"])
        self.list[i if i != None else 0] = item

    def removeItem(self, id : str) -> None:

        """modify an already existing item in the list. itemPos throws ItemNotFoundError if it isn't listed."""

        i = self.itemPos(id)
        self.list.remove(i if i != None else 0) 

    def save(self, _filename : str) -> None:

        """save the list into a json file."""

        with open(_filename, 'w+', encoding="utf-8") as f:
            try: j = json.load(f)
            except json.decoder.JSONDecodeError as e:
                j = {}
            j[self.name] = self.list
            json.dump(j, f, ensure_ascii=False, indent=2)    #dump into the same file  