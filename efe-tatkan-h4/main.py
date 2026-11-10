from dataclasses import dataclass, asdict
import jlist 

class CapacityFullError(Exception): pass
class AlreadyRegisteredError(Exception): pass

@dataclass
class Member:
    id: str
    name: str
    major: str

@dataclass
class Event:
    id: str
    title: str
    date: str
    
    _quota: int

    @property
    def quota(self):
        return self._quota

    @quota.setter
    def quota(self, val):
        self._quota = val

    guestlist: jlist.JList

    def register(self, member : Member):

        if(self.quota <= 0):
            raise CapacityFullError(f"the event '{self.title}' doesnt accept any more members.")
        try: self.guestlist.addItem(asdict(member))
        except jlist.ItemExistsError as e:
            raise AlreadyRegisteredError(f"the member with the id '{member.id}' has been registered to this event already.") 
        self.quota -= 1
        
@dataclass
class Announcement:
    id: str
    title: str
    desc: str
    date: str