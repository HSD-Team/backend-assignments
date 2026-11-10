import json
import re
import mlog_defs as util

print(""" 
    --- memberlogger.py: CLI for managing a user database ---
    
    to perform an action, please enter your desired command.

        - add <name>: add a new member or directory to the database.
        
        - search <name>: search for a term in the list.
        
        - remove <name>: remove the provided name from the database.
        
        - list: dump the entire list in alphabetical order.

    ** you may enter 'exit' to quit the application and save the changes made in this session.

    """)

while True: 

    i = input(">>> ")

    m = re.search(r"^\s*((\S*) *(\S*))\s*$", i)
    if not m:
        try:
            raise util.InvalidCommandError(f"unknown command: '{i}'")
        except Exception:
            print(f"error: unknown command '{i}' - no operation performed.")
            continue
        
    com = m.group(2).lower()

    match com:
        case "add":
            name = m.group(3)
            list = util.Memlist.getglob()
            try: 
                list.mempos(name)
                print("error: member with the given name already exists - no operation performed.")
            except util.MemberNotFoundError:
                list.mempos(name, True)

        case "list":
            list = util.Memlist.getglob()
            for i in list.members:
                print(i)
            print(f"\n{len(list.members)} members in total.")

        case "search":
            list = util.Memlist.getglob()
            name = m.group(3)
            try:
                p = list.mempos(name)
                print(f"found member named '{name}' at index {p}.")
            except util.MemberNotFoundError: 
                print("error: a member with the given name could not be found.") 

        case "remove":
            list = util.Memlist.getglob()
            name = m.group(3)
            try:
                p = list.mempos(name)
                if p == None: p = -1
                list.members.pop(p)
                print(f"removed member named '{name}'.")
            except util.MemberNotFoundError: 
                print("error: a member with the given name could not be found - no operation performed.")

        case "exit":
            list = util.Memlist.getglob()
            try:
                with open("members.json", "w") as f:
                    json.dump(list.members, f)
                print("successfully saved the changes. exiting program...")
                break
            except Exception:
                print("error: couldn't save successfully - shutdown cancelled.")
