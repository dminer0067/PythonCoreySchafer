import json

with open("states.json","r") as f:
    data = json.load(f)
    
for state in data["states"]:
    del state["area_codes"]

with open("newstates.json","w") as w:
    json.dump(data,w,indent=2)
