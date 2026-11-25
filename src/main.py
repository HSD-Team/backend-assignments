from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from datetime import datetime

import mem_classes as mem
import jlist

dummy_event = mem.Event(title="members", date="", quota=-1, guestlist=jlist.JList(name="members"), id_str="members")
_headers = {"Date" : datetime.now().strftime("%d/%m/%Y, %H:%M:%S"), 
            "Content-Type" : "application/json; charset=utf-8"} # default headers for this context

app = FastAPI()

@app.get("/health", name="status")          # return a static response, to confirm that the server is alive
async def status():
    r = {"status": "ok"}
    return JSONResponse(content=r, headers=_headers)


@app.get("/members", name="mem_list")              # return a list of all members
async def listMembersRequest(department: str | None = None):

    r = {"members" : dummy_event.guestlist.content}

    if department != None:
        r["members"] = [i for i in dummy_event.guestlist.content if i["major"]==department]

    return JSONResponse(content=r, headers=_headers)


@app.get("/members/{id}", name="mem_get")         # return a specific user with a given id
async def getMemberRequest(id : str):

    if id == "": raise HTTPException(status_code=422, detail="the input string was empty.")

    try:
        i = dummy_event.guestlist.itemPos(id)
        r = dummy_event.guestlist.content[i if i != None else 0]
        return JSONResponse(content=r, headers=_headers)

    except jlist.ItemNotFoundError as e:
        raise HTTPException(status_code=404, detail=f"a member with the given id '{id}' could not be found.")


@app.post("/members", name="mem_add")             # try to register a new member
async def addMemberRequest(memb: mem.MemberBase, request: Request):
    
    try:
        r = dummy_event.register(memb)
        loc = str(request.url_for("mem_get", id=r.id_str))
        headers = _headers
        headers["Location"] = loc
        return JSONResponse(status_code=201, content=r.model_dump(), headers=headers)

    except mem.AlreadyRegisteredError as e:
        raise HTTPException(status_code=409, detail=e.args[0])
    
    except mem.MemberValueError as e:
        raise HTTPException(status_code=422, detail=e.args[0])

    ###except AssertionError as e:
    ###   raise HTTPException(status_code=471, detail=f"DEBUG!!! dump '{r.model_dump()}' og '{memb.model_dump()}'")

    ###except Exception as e:
    ###    raise HTTPException(status_code=472, detail=e.args[0])


@app.put("/members", name="mem_up")              # try to update a registered member
async def modifyMemberRequest(memb: mem.MemberBase, request: Request):
    
    try:
        r = dummy_event.modify(memb)
        loc = str(request.url_for("mem_get", id=r.id_str))
        headers = _headers
        headers["Location"] = loc
        return JSONResponse(content=r.model_dump(), headers=headers)       

    except mem.MemberNotFoundError as e:
        raise HTTPException(status_code=404, detail=e.args[0])
    except mem.MemberValueError as e:
        raise HTTPException(status_code=422, detail=e.args[0])


@app.delete("/members", name="mem_remove")          # try to delete a registered member
async def deleteMemberRequest(memname: str):
    
    try:
        dummy_event.remove(memname)
        return JSONResponse(status_code=204, content=None, headers={"Date" : datetime.now().strftime("%d/%m/%Y, %H:%M:%S")})
    
    except mem.MemberNotFoundError as e:
        raise HTTPException(status_code=404, detail=e.args[0])
    except mem.MemberValueError as e:
        raise HTTPException(status_code=422, detail=e.args[0])