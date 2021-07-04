files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
result = {}
for file,owner in files.items():
    result[owner]=result.get(owner,[]) + [file]
    #print(result.get(owner,[])+[file])
print(result)