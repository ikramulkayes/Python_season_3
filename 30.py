class AirConditioner:
  name = "Air Conditioner"
  all_instances = []
  instances = []
  def __init__(self, brand, inverter=False, heat_mode=False):
    self.__brand = brand
    self.__inverter = inverter
    self.__heat = heat_mode
    code = ""
    for word in self.name.split():
      code += word[0]
    self.__id = f"{code}{len(self.instances)}"
    self.instances.append(self)
    AirConditioner.all_instances.append(self)

  def turn_on(self):
    print("AC ON")
    print("Compressor ON")
  
  def getAttrs(self):
    return self.__id, self.__brand, self.__inverter, self.__heat

  def __str__(self):
    format = "ID: %s, Brand: %s, Inverter: %s, Heat-mode: %s"
    return format % self.getAttrs()

  @classmethod
  def printInfo(cls):
    print(f"Total {cls.name} Instances: {len(cls.instances)}")
    for instance in cls.instances:
      print(instance)

  @classmethod
  def getDeepInfo(cls):
    print("Total AC Instances:", len(cls.all_instances))
    return "Incomplete"



AirConditioner.printInfo()
print("------------------------")
print(AirConditioner.getDeepInfo())
print("========================")
general_inverter = GeneralInverterAC(False)
general_inverter_heat = GeneralInverterAC(True)
basic_ac = AirConditioner("Local")
lg_inverter = LGInverterAC(True)
general_inverter.turn_on()
print("++++++++++++++++++++++++")
lg_inverter.turn_on()
print("**********************")
AirConditioner.printInfo()
print("------------------------")
print(AirConditioner.getDeepInfo())
print("========================")
GeneralInverterAC.printInfo()
print("========================")
LGInverterAC.printInfo()
print("========================")
print(LGInverterAC.getDeepInfo())
print("========================")