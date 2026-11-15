from dataclasses import dataclass, asdict
import jlist 
from enum import Enum

class CapacityFullError(Exception): pass
class AlreadyRegisteredError(Exception): pass

@dataclass
class Member:
    id: str
    name: str
    major: str

    class MemRank(Enum):
        MEMBER = 0
        ADMIN = 1

    rank: MemRank | str

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
        try: 
            _member = member
            _member.rank = str(member.rank)
            self.guestlist.addItem(asdict(member))
        except jlist.ItemExistsError as e:
            raise AlreadyRegisteredError(f"the member with the id '{member.id}' has been registered to this event already.") 
        self.quota -= 1

    def save(self):
        self.guestlist.save(f"{self.title}.json")
        
@dataclass
class Announcement:
    id: str
    title: str
    desc: str
    date: str