import json

with open("test.json","r") as f:
    data = json.load(f)

print(data["test"])
print(type(data))
with open("test.json","w") as f:
    json.dump(data | {"AHHH":"GAHHHHH"},f,indent=4)