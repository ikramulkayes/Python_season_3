import re
message1 = "Here is my phone number: (191)-820-9505"
message2 = "Yo pops, this is the number you wanted 01677183342"
pattern = "\d{10}|\(\d{3}\)-\d{3}-\d{4}"
matched = re.findall(pattern,message1)
print(matched)
matched = re.findall(pattern,message2)
print(matched)
