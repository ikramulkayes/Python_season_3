dct = {}
for key,val in dct.items():
    for k,v in val:
        dct[key][k] = tuple(v)

