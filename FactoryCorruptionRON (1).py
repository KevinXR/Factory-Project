print("\n┏┳┓┓     ┏┓     ┏┓┏  ┏┳┓┓     ┏┓          ")
print(" ┃ ┣┓┏┓  ┣┫┏┓╋  ┃┃╋   ┃ ┣┓┏┓  ┣ ┏┓┏╋┏┓┏┓┓┏")
print(" ┻ ┛┗┗   ┛┗┛ ┗  ┗┛┛   ┻ ┛┗┗   ┻ ┗┻┗┗┗┛┛ ┗┫")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ")       
print("                                             ")                                      
                                        
# Things to do:
#  * make inputs better
#  * Clean up code
#  * How much of ____ do you want?
#  * Resource policies
#  * Custom/Leader modifiers
#  * Colored and Noncolored version
#  * Convert everything to java
#  * Organize all data
#  * Make into program


# If you want nice colors, do "pip install colorama"
# you can use this website: https://www.programiz.com/python-programming/online-compiler/ or another of your choosing as long as its a python complier 

import math
# from colorama import Fore
#009c75
#ideology = str(input("Ideology? \n"))
#factory = int(input("Factory output? (0-5) \n"))
#decide = str(input ("What policy? (forced labor, public service, both or none)\n"))
#corrupt = str(input ("Do you have "Ignore Safety Regulations?" (Yes/No)\n")) 
#extra = float(input("Enter any custom factory modifiers in a percentage. Put 0 if there are none. (%25 = 25)"))
#city = float(input("Civilian factory count? \n"))

ideology = "none"
factory = 2
decide = "none"
corrupt = "yes"
city = 20
extra = 0.0


#shit ton of variables
steel = 3
elect = 16
fert = 12
motor = 6
civ = 40
x = city*2.5
y = city*3
m = int(math.ceil(x/motor))
e = int(math.ceil(y/elect))
f = int(math.ceil(x/fert))
s = int(math.ceil(motor/steel))
factory1 = .2
factory2 = .45
factory3 = .7
factory4 = 1.2
factory5 = 1.7
communist = 2.25
socialist = 1.5
forced = .4
public = .2
sinola = .35
modifier=1.00

#algorithm
if (ideology == "communism"):
  steel=steel*communist
  elect=elect*communist
  motor=motor*communist
  fert=fert*communist
  civ=civ*communist
elif (ideology == "socialism"): 
  steel=steel*socialist
  elect=elect*socialist
  motor=motor*socialist
  fert=fert*socialist
  civ=civ*socialist
print("")
if (factory == 1):
  modifier=modifier+factory1
elif (factory == 2):
  modifier=modifier+factory2
elif (factory == 3):
  modifier=modifier+factory3
elif (factory == 4):
  modifier=modifier+factory4
elif (factory == 5):
  modifier=modifier+factory5
else: 
  modifier=modifier+0
if (corrupt == "yes"):
  modifier=modifier+sinola
else: 
  modifier=modifier+0
print("-----------------------------------------------------------------")
if (decide == "forced labor"):
  modifier=modifier+forced
elif (decide == "public service"):
  modifier=modifier+public
elif (decide == "both"):
  modifier=modifier+public+forced
else: 
  modifier=modifier+0
print("")
#setter/mutator variables
modifier=modifier+(extra/100)
m2 = x/(motor*modifier)
f2 = x/(fert*modifier)
e2 = y/(elect*modifier)
s2 = m2/(steel*modifier)
m3 = int(math.ceil(m2))
f3 = int(math.ceil(f2))
e3 = int(math.ceil(e2))
s3 = int(math.ceil(s2))
mr = (m3*2)+.1
fr = (f3*3.5)+.1
er = (e3*2)+.1
sr = (s3*4)+.1
sr2 = (s3*0.2)+.1
income = (m3 + e3 + f3 + s3 + city)*250000
dif = (mr*96000+er*96000+fr*41500+sr*38000+sr2*102000)


#output
print("Motor factory makes about: " + str(round((motor*modifier), 2)) + " motor parts")
print("Electronics factory makes about: " + str(round((elect*modifier), 2)) + " electronics")
print("Fertilizer factory makes about: " + str(round((fert*modifier), 2)) + " fertilizers")
print("Steel factory makes about: " + str(round((steel*modifier), 2)) + " steel")
print("Civilian factory makes about: " + str(round((civ*modifier), 2)) + " consumer goods")
print(f"Cost to build everything: {(25000000*((m3+f3+e3+s3) + (city))):,}")

print("\nYou need: \n" + str (m3) + " motor factories \n" + str (e3) + " electronic factories \n" + str (f3) + " fertilizer factories \n" + str(s3) + " steel factories \n")
print("Resources you need: \n" + str (mr) + " Tungsten \n" + str (er) + " Copper and Gold \n" + str (fr) + " Phosphate \n" + str(sr) + " Iron \n" + str(round(sr2, 2)) + " Titanium \n")
print("Good luck LMAO")
print(f"Your resource income is: {(income):,}")
print(f"Your actual income is: {(income-dif):,}")







