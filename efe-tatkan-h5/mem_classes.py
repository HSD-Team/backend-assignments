from pydantic import BaseModel, field_validator
from urllib.parse import quote
from enum import StrEnum
import re

import jlist 

class CapacityFullError(Exception): pass
class AlreadyRegisteredError(Exception): pass
class MemberNotFoundError(Exception): pass
class MemberValueError(ValueError): pass

class MemRank(StrEnum):
    MEMBER = "member"
    ADMIN = "admin"

class MemberBase(BaseModel):

    """base class for members; with a name, major, and rank (member or admin)."""

    name: str = ""
    major: str = ""
    rank: MemRank = MemRank.MEMBER

    @field_validator("major")
    @classmethod
    def major_val(cls, s: str) -> str:
        ss = re.sub(r"^[\W|_]*([\S ]*\w)[\W|_]*$", r"\g<1>", s)
        return re.sub(r"\W+", "_", ss).lower()

class Member(MemberBase):
    id_str: str = ""

class EventBase(BaseModel):

    """base class for events with a title, data, quota and guestlist."""

    title: str = ""
    date: str = ""
    quota: int = -1
    guestlist: jlist.JList

    def formatMemName(self, name: str) -> str:

        """formats a given member name into a member id. returns an empty string if the given name is invalid."""

        if name == "" or re.search(r"[^\w ]+|_+", name): 
            return ""
        else: return name.lower()

    def register(self, member : MemberBase) -> Member:

        """try to add a member into the guestlist. throw AlreadyRegisteredError if the member is already listed."""

        quota_step = 1
        if self.quota < 0:
            quota_step = 0
        elif self.quota == 0:
            raise CapacityFullError(f"the event '{self.title}' doesnt accept any more members.")
        try: 
            mem_d = member.model_dump()
            mem_d["id_str"] = self.formatMemName(member.name)
            self.guestlist.addItem(mem_d)
            self.quota -= quota_step
            ###raise Exception(f"DEBUG FROM register!! memd: '{mem_d}', memd dump: '{Member(**mem_d)}'")
            return Member(**mem_d)
        except jlist.ItemExistsError:
            raise AlreadyRegisteredError(f"the member with the id '{mem_d["id_str"]}' has been registered to this event already.")
        except jlist.EmptyIDError:
            raise MemberValueError(f"invalid value for member.name: '{member.name}'. member names can only contain letters, numbers and spaces.")

    def modify(self, member : MemberBase) -> Member:

        """try to modify a registered member. throw MemberNotFoundError if the member doesn't exist."""
        
        try:
            mem_d = member.model_dump()
            mem_d["id_str"] = self.formatMemName(member.name)
            self.guestlist.modifyItem(mem_d)
            return Member(**mem_d)
        except jlist.ItemNotFoundError:
            raise MemberNotFoundError(f"a member with id '{mem_d["id_str"]}' could not be found and thus can't be modified.")
        except jlist.EmptyIDError:
            raise MemberValueError(f"invalid value for member.name: '{member.name}'. member names can only contain letters, numbers and spaces.")
    
    def remove(self, memname: str) -> None:

        """try to remove a registered member from the list. throw MemberNotFoundError if the member doesn't exist."""

        try:
            id_ = self.formatMemName(memname)
            self.guestlist.removeItem(id_)
        except jlist.ItemNotFoundError:
            raise MemberNotFoundError(f"a member with id '{id_}' could not be found and thus can't be removed.")
        except jlist.EmptyIDError:
            raise MemberValueError(f"invalid value for member.name: '{memname}'. member names can only contain letters, numbers and spaces.")
        
    def save(self) -> None:

        """save the guestlist of this event into a json."""

        self.guestlist.save(f"{self.title}.json")

class Event(EventBase):
    id_str: str = ""
        
class Announcement(BaseModel):

    """stub class for announcements."""

    id_str: str = ""
    title: str = ""
    desc: str = ""
    date: str = ""