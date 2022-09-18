class BetterCallSaul:
  number = 0
  def __init__(self,first_name, last_name,age,location):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.location = location
    self.extrafee = 0
    BetterCallSaul.number += 1
    self.id = BetterCallSaul.number
  
  @staticmethod
  def amIGuilty():
    print("Constitution says you are innocent until proven guilty")
  
  @classmethod
  def createClient(cls,first_name, last_name,age,location):
    temp_client = cls(first_name, last_name,age,location)
    if(location != "Albuquerque"):
      temp_client.extrafee = 100
    return temp_client
 
 
  def __str__(self):
    return f"ID:{self.id}\nFirst name:{self.first_name}\nLast name:{self.last_name}\nAge:{self.age}\nLocation:{self.location}"
 
 
#write your code here
client1 = BetterCallSaul("Walter","White",49,"Albuquerque")
client2 = BetterCallSaul("Jesse","Pinkman",21,"Albuquerque")
client3 = BetterCallSaul.createClient("Mike","Ehrementraut",56,"Florida")
client4 = Oakley.createClient("Gus","Fring",37,"Chile")
client5 = Oakley("Skinny","Pete",27,"Albuquerque")
print(client1)
print("#################################")
client1.amIGuilty()
print("#################################")
print(client2)
print("#################################")
print(client3)
print("#################################")
print(f"Client Name:{client3.first_name}\nExtra Fee:{client3.extrafee}")
print("#################################")
print(client4)
print("#################################")
print(f"Client Name:{client4.first_name}\nExtra Fee:{client4.extrafee}")
print("#################################")
print(client5)
print("#################################")
client4.amIGuilty()