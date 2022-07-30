def phonebook(lst):
  nlst =[]
  dct = {}
  for i in range(len(lst)//2):
    nlst.append([lst[0+2*i], lst[1+2*i]])
    if nlst[0][0][0] not in dct.keys():
      dct[nlst[0][0][0]] = {nlst[0][0]: [nlst[-1]]}
    else:
      if nlst[0][0] not in dct[nlst[0][0[0]].keys():
         dct[nlst[0][0][0]][nlst[0][0]] = [nlst[-1]]
      else:
         var = dct[nlst[0][0][0]][nlst[0][0]]
         var.append(nlst[-1])
         dct[nlst[0][0[0]][nlst[0][0]] = var
  return dct

PB = ['Bob', '01932342392', 'Alice', '01546734123', 'Britney', '01303544535', 'Aeron', '01723454642', 'Smith', '01923457890', 'Tarek', '01934663922', 'Carol', '01823456785']
print(phonebook(PB))