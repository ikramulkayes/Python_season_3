import re
message3 = "Here is my email dog ggkayes@gmail.com"
message1 = "Here is my phone number: (191)-820-9505"
message2 = "Yo pops, this is the number you wanted 01677183342"
pattern = "\d{10}|\(\d{3}\)-\d{3}-\d{4}"
patternemail = "[a-z0-9A-Z]*@[a-z0-9A-Z]*\.[a-z0-9A-Z]*"
patternorder = "order[^\d]*(\d*)"
matched = re.findall(pattern,message1)
print(matched)
matched = re.findall(pattern,message2)
print(matched)
matched = re.findall(patternemail,message3)
print(matched)


message4 = "My order #541546"
matched = re.findall(patternorder,message4)
print(matched)
