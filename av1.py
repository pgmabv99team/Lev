import json 
  
# Opening JSON file 
f = open('file2.json',) 
data = json.load(f)
print (data["states"])
print (data["states"][1]["population"])

x=[
    ["a","b","c"],
    ["x","y","z"]
]

print(x)
print(x[1][0:2])