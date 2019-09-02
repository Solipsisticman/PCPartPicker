from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps
import sqlite3
import os

if os.path.isfile('pcparts.db'):
        os.remove('pcparts.db')
        
conn = sqlite3.connect('pcparts.db')
db = conn.cursor()

db.execute("""CREATE TABLE CPUS
              (Model INTEGER PRIMARY KEY,
               Name TEXT,
               CoreCount TEXT,
               CoreClock TEXT,
               BoostClock TEXT,
               TDP TEXT,
               Price TEXT,
               Socket TEXT)""")

Model="1" 
Name="AMD Ryzen 5 2600" 
CoreCount="6"
CoreClock="3.4 GHz"
BoostClock="3.9 GHz"
TDP="65 W"
Price="£119.00"
Socket="AM4"
db.execute("INSERT INTO CPUS(Model,Name,CoreCount,CoreClock,BoostClock,TDP,Price,Socket)\
VALUES (?,?,?,?,?,?,?,?)",(Model,Name,CoreCount,CoreClock,BoostClock,TDP,Price,Socket));

Model="2" 
Name="Intel Core i9-9900K" 
CoreCount="8"
CoreClock="3.6 GHz"
BoostClock="5 GHz"
TDP="95 W"
Price="£459.99"
Socket="LGA1151"
db.execute("INSERT INTO CPUS(Model,Name,CoreCount,CoreClock,BoostClock,TDP,Price,Socket)\
VALUES (?,?,?,?,?,?,?,?)",(Model,Name,CoreCount,CoreClock,BoostClock,TDP,Price,Socket));

db.execute("""CREATE TABLE CPUCooler
              (Model INTEGER PRIMARY KEY,
               Name TEXT,
               FanRPM TEXT,
               NoiseLevel TEXT,
               Colour TEXT,
               RadiatorSize TEXT,
               Price TEXT,
               Socket TEXT)""")
Model="1" 
Name="Corsair H100i RGB PLATINUM" 
FanRPM="2400 RPM"
NoiseLevel="37 dB"
Colour="Black / Silver"
RadiatorSize="240 mm"
Price="£116.48"
Socket="LGA1151"
db.execute("INSERT INTO CPUCooler(Model,Name,FanRPM,NoiseLevel,Colour,RadiatorSize,Price,Socket)\
VALUES (?,?,?,?,?,?,?,?)",(Model,Name,FanRPM,NoiseLevel,Colour,RadiatorSize,Price,Socket));

Model="2" 
Name="NZXT Kraken X62 Rev 2" 
FanRPM="500 - 1800 RPM"
NoiseLevel="21 - 38 dB"
Colour="Black"
RadiatorSize="280 mm"
Price="£127.54"
Socket="AM4"
db.execute("INSERT INTO CPUCooler(Model,Name,FanRPM,NoiseLevel,Colour,RadiatorSize,Price,Socket)\
VALUES (?,?,?,?,?,?,?,?)",(Model,Name,FanRPM,NoiseLevel,Colour,RadiatorSize,Price,Socket));

db.execute("""CREATE TABLE Motherboard
              (Model INTEGER PRIMARY KEY,
               Name TEXT,
               Socket TEXT,
               FormFactor TEXT,
               RAMSlots TEXT,
               MaxRAM TEXT,
               Price TEXT,
               Socket2 TEXT)""")

Model="1" 
Name="Asus ROG STRIX Z390-E GAMING" 
Socket="LGA1151"
FormFactor="ATX"
RAMSlots="4"
MaxRAM="64 GB"
Price="£259.00"
Socket2="LGA1151"
db.execute("INSERT INTO Motherboard(Model,Name,Socket,FormFactor,RAMSlots,MaxRAM,Price,Socket2)\
VALUES (?,?,?,?,?,?,?,?)",(Model,Name,Socket,FormFactor,RAMSlots,MaxRAM,Price,Socket2));

Model="2" 
Name="Asus ROG STRIX B450-F GAMING" 
Socket="AM4"
FormFactor="ATX"
RAMSlots="4"
MaxRAM="64 GB"
Price="£119.99"
Socket2="AM4"
db.execute("INSERT INTO Motherboard(Model,Name,Socket,FormFactor,RAMSlots,MaxRAM,Price,Socket2)\
VALUES (?,?,?,?,?,?,?,?)",(Model,Name,Socket,FormFactor,RAMSlots,MaxRAM,Price,Socket2));

db.execute("""CREATE TABLE Memory
              (Model INTEGER PRIMARY KEY,
               Name TEXT,
               Speed TEXT,
               Type TEXT,
               Modules TEXT,
               Colour TEXT,
               Price TEXT,
               Socket TEXT)""")

Model="1" 
Name="G.Skill Trident Z RGB 16 GB" 
Speed="DDR4-3200"
Type="288-pin DIMM"
Modules="2 x 8GB"
Colour="Black"
Price="£115.17"
Socket="LGA1151,AM4"
db.execute("INSERT INTO Memory(Model,Name,Speed,Type,Modules,Colour,Price,Socket)\
VALUES (?,?,?,?,?,?,?,?)",(Model,Name,Speed,Type,Modules,Colour,Price,Socket));

Model="2"
Name="Corsair Vengeance LPX 16 GB" 
Speed="DDR4-3200"
Type="288-pin DIMM"
Modules="2 x 8GB"
Colour="Black / Yellow"
Price="£88.91"
Socket="LGA1151,AM4"
db.execute("INSERT INTO Memory(Model,Name,Speed,Type,Modules,Colour,Price,Socket)\
VALUES (?,?,?,?,?,?,?,?)",(Model,Name,Speed,Type,Modules,Colour,Price,Socket));

db.execute("""CREATE TABLE Storage
              (Model INTEGER PRIMARY KEY,
               Name TEXT,
               Capacity TEXT,
               Type TEXT,
               Cache TEXT,
               Interface TEXT,
               Price TEXT,
               Socket TEXT)""")

Model="1" 
Name="Samsung 860 Evo" 
Capacity="500 GB"
Type="SSD"
Cache="512 MB"
Interface="SATA 6 Gb/s"
Price="£74.99"
Socket="LGA1151,AM4"
db.execute("INSERT INTO Storage(Model,Name,Capacity,Type,Cache,Interface,Price,Socket)\
VALUES (?,?,?,?,?,?,?,?)",(Model,Name,Capacity,Type,Cache,Interface,Price,Socket));

Model="2" 
Name="Seagate Barracuda" 
Capacity="2000 GB"
Type="7200 RPM"
Cache="64 MB"
Interface="SATA 6 Gb/s"
Price="£105.31"
Socket="LGA1151,AM4"
db.execute("INSERT INTO Storage(Model,Name,Capacity,Type,Cache,Interface,Price,Socket)\
VALUES (?,?,?,?,?,?,?,?)",(Model,Name,Capacity,Type,Cache,Interface,Price,Socket));

db.execute("""CREATE TABLE VideoCard
              (Model INTEGER PRIMARY KEY,
               Name TEXT,
               Chipset TEXT,
               Memory TEXT,
               CoreClock TEXT,
               BoostClock TEXT,
               Price TEXT,
               Socket TEXT)""")

Model="1" 
Name="Asus ROG Strix Gaming OC" 
Chipset="GeForce RTX 2080"
Memory="8 GB"
CoreClock="1515 MHz"
BoostClock="1890 MHz"
Price="£799.99"
Socket="LGA1151,AM4"
db.execute("INSERT INTO VideoCard(Model,Name,Chipset,Memory,CoreClock,BoostClock,Price,Socket)\
VALUES (?,?,?,?,?,?,?,?)",(Model,Name,Chipset,Memory,CoreClock,BoostClock,Price,Socket));


Model="2" 
Name="Gigabyte WINDFORCE OC" 
Chipset="GeForce RTX 2060 SUPER"
Memory="8 GB"
CoreClock="1470 MHz"
BoostClock="1680 MHz"
Price="£384.98"
Socket="LGA1151,AM4"
db.execute("INSERT INTO VideoCard(Model,Name,Chipset,Memory,CoreClock,BoostClock,Price,Socket)\
VALUES (?,?,?,?,?,?,?,?)",(Model,Name,Chipset,Memory,CoreClock,BoostClock,Price,Socket));

db.execute("""CREATE TABLE PCCase
              (Model INTEGER PRIMARY KEY,
               Name TEXT,
               Type TEXT,
               Colour TEXT,
               SidePanelWindow TEXT,
               InternalBays TEXT,
               Price TEXT,
               Socket TEXT)""")

Model="1" 
Name="Corsair Obsidian 500D RGB SE" 
Type="ATX Mid Tower"
Colour="Black"
SidePanelWindow="Tempered Glass"
InternalBays="2"
Price="£209.99"
Socket="LGA1151,AM4"
db.execute("INSERT INTO PCCase(Model,Name,Type,Colour,SidePanelWindow,InternalBays,Price,Socket)\
VALUES (?,?,?,?,?,?,?,?)",(Model,Name,Type,Colour,SidePanelWindow,InternalBays,Price,Socket));

Model="2" 
Name="NZXT H500i" 
Type="ATX Mid Tower"
Colour="Black"
SidePanelWindow="Tempered Glass"
InternalBays="3"
Price="£99.98"
Socket="LGA1151,AM4"
db.execute("INSERT INTO PCCase(Model,Name,Type,Colour,SidePanelWindow,InternalBays,Price,Socket)\
VALUES (?,?,?,?,?,?,?,?)",(Model,Name,Type,Colour,SidePanelWindow,InternalBays,Price,Socket));

db.execute("""CREATE TABLE PowerSupply
              (Model INTEGER PRIMARY KEY,
               Name TEXT,
               FormFactor TEXT,
               EfficiencyRating TEXT,
               Wattage TEXT,
               Modular TEXT,
               Price TEXT,
               Socket TEXT)""")

Model="1" 
Name="EVGA SuperNOVA G2" 
FormFactor="ATX"
EfficiencyRating="80+ Gold"
Wattage="550 W"
Modular="Full"
Price="£92.99"
Socket="LGA1151,AM4"
db.execute("INSERT INTO PowerSupply(Model,Name,FormFactor,EfficiencyRating,Wattage,Modular,Price,Socket)\
VALUES (?,?,?,?,?,?,?,?)",(Model,Name,FormFactor,EfficiencyRating,Wattage,Modular,Price,Socket));

Model="2" 
Name="Corsair AX860" 
FormFactor="ATX"
EfficiencyRating="80+ Platinum"
Wattage="860 W"
Modular="Full"
Price="£241.40"
Socket="LGA1151,AM4"
db.execute("INSERT INTO PowerSupply(Model,Name,FormFactor,EfficiencyRating,Wattage,Modular,Price,Socket)\
VALUES (?,?,?,?,?,?,?,?)",(Model,Name,FormFactor,EfficiencyRating,Wattage,Modular,Price,Socket));
#CPUCooler="H110i"
#db.execute("UPDATE PCParts SET CPUCooler=? WHERE \
#Memory='Corsair'",(CPUCooler,))

def print_table(sql): 
	db.execute(sql) 
	all_rows = db.fetchall() 
	for row in all_rows: 
		for i in row: 
			print(i, end=' | \t') 
		print() 
	print()

sql="SELECT * FROM PCCase"
print_table(sql)


conn.commit()
conn.close()
