import classes as cl
import jlist
import random

mems = []
chars = "abcdefghijklmnopqrstuvwxyz_" 
nums = "0123456789" 

for i in range(8):
    name = ''.join(random.choices(chars,k=10))
    name2 = ''.join(random.choices(nums,k=10))
    name3 = random.choice([cl.Member.MemRank.ADMIN, cl.Member.MemRank.MEMBER])
    mems.append(cl.Member(name, name, name2, name3))

testlist = jlist.JList("testevent")
try: testlist.loadFromFile("test event.json")
except FileNotFoundError: pass
testevent = cl.Event("test event", "test event", "01.01.2027", 5, testlist)

mems[3] = mems[2] #test double registration

for i in range(8):
    try: 
        print(f"\n## register attempt {i+1} ##")
        testevent.register(mems[i])
        print(f"""registered '{mems[i].name}' to testevent
quota of testevent: {testevent.quota}""")
    except cl.AlreadyRegisteredError:
        print(f"couldn't register '{mems[i].name}' because they were already registered.")
    except cl.CapacityFullError:
        print(f"couldn't register '{mems[i].name}' because testevent has no capacity left.")

testevent.save()
print("\nsaved list to 'test event.json', exiting...")