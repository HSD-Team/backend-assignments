from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

import mem_classes as mem
import jlist

dummy_event = mem.Event(title="members", date="", _quota=-1, guestlist=jlist.JList("members"), id="members")

app = FastAPI()

### TODO: -implement the JSONResponse returns.
###       -annotate main.py and mem_classes.py


@app.get("/health", status_code=200, response_model= JSONResponse)
async def status():
    return {"status": "ok"}

@app.get("/members", status_code=200, response_model= JSONResponse)
async def listMembersRequest(department: str | None = None):
    if department != None:
        return {"members" : [i for i in dummy_event.guestlist.list if i["major"]==department]}
    else: return {"members" : dummy_event.guestlist.list}

@app.get("/members/{id}", status_code=200, response_model= JSONResponse)
async def getMemberRequest(id : str):
    if id == "": raise HTTPException(status_code=422, detail="the input string was empty.")
    try:
        i = dummy_event.guestlist.itemPos(id)
        return dummy_event.guestlist.list[i if i != None else 0]
    except jlist.ItemNotFoundError as e:
        raise HTTPException(status_code=404, detail=f"a member with the given id '{id}' could not be found.")

@app.post("/members", status_code=201, response_model=JSONResponse)
async def addMemberRequest(memb: mem.MemberBase):
    try:
        return dummy_event.register(memb)
    except mem.AlreadyRegisteredError as e:
        raise HTTPException(status_code=409, detail=e.args[0])
    except mem.MemberValueError as e:
        raise HTTPException(status_code=422, detail=e.args[0])

@app.put("/members", status_code=200, response_model=JSONResponse)
async def modifyMemberRequest(memb: mem.MemberBase):
    try:
        dummy_event.modify(memb)
    except mem.MemberNotFoundError as e:
        raise HTTPException(status_code=404, detail=e.args[0])
    except mem.MemberValueError as e:
        raise HTTPException(status_code=422, detail=e.args[0])

@app.delete("/members", status_code=204, response_model=JSONResponse)
async def deleteMemberRequest(memname: str):
    try:
        dummy_event.remove(memname)
    except mem.MemberNotFoundError as e:
        raise HTTPException(status_code=404, detail=e.args[0])
    except mem.MemberValueError as e:
        raise HTTPException(status_code=422, detail=e.args[0])