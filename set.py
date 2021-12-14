import json

set_old = set()
set_new = set()

f = open('lol.json')
data = json.load(f)
for x in data:
    set_old.add(x["name"])
f.close()

j = open('lol_new.json')
data = json.load(j)
for x in data:
    set_new.add(x["name"])
j.close

print(set_old.intersection(set_new))

set_added = set_new
for x in set_old:
    if x in set_added:
        set_added.remove(x)

print(set_added)
print(len(set_new))
