import json
data = open('sample-data.json').read()
print(
    "Interface Status" "\n"
    "================================================================================" "\n"
    "DN                                                 Description           Speed    MTU" "\n"  
    "-------------------------------------------------- --------------------  ------  ------")

js_obj = json.loads(data)
imdata = js_obj['imdata']
for x in imdata:
    dn = x["l1PhysIf"]["attributes"]["dn"]
    Description = x["l1PhysIf"]["attributes"]["descr"]
    Speed = x["l1PhysIf"]["attributes"]["speed"]
    mtu = x["l1PhysIf"]["attributes"]["mtu"]
    print("{0:51} {1:20} {2:7} {3:4}".format(dn, Description, Speed, mtu))