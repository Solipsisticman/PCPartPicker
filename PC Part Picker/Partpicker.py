from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps
import sqlite3
import os
app = Flask(__name__)



conn = sqlite3.connect("pcparts.db") 
cursor = conn.cursor()


conn.commit()
username= "'Barney' OR '0'='0'"
password= "'Barney' OR '0'='0'"
sql = "SELECT * FROM CPUS WHERE Model ='1'"
#print(sql)
cursor.execute(sql)
all_rows = cursor.fetchall()
#print(all_rows)

for cpu in all_rows:
    cpusex='{0} : {1}, {2}, {3}, {4}, {5}, {6}, {7}'.format(cpu[0], cpu[1], cpu[2], cpu[3], cpu[4], cpu[5], cpu[6], cpu[7])
    #print('{0} : {1}, {2}, {3}, {4}, {5}, {6}'.format(cpu[0], cpu[1], cpu[2], cpu[3], cpu[4], cpu[5], cpu[6]))

sql = "SELECT * FROM CPUS WHERE Model ='2'"
#print(sql)
cursor.execute(sql)
all_rows = cursor.fetchall()
#print(all_rows)

for cpu2 in all_rows:
    cpusex='{0} : {1}, {2}, {3}, {4}, {5}, {6}, {7}'.format(cpu2[0], cpu2[1], cpu2[2], cpu2[3], cpu2[4], cpu2[5], cpu2[6], cpu2[7])
    #print('{0} : {1}, {2}, {3}, {4}, {5}, {6}'.format(row2[0], row2[1], row2[2], row2[3], row2[4], row2[5], row2[6]))

sql = "SELECT * FROM CPUCooler WHERE Model ='1'"
cursor.execute(sql)
all_rows = cursor.fetchall()

for cooler in all_rows:
    coolerex='{0} : {1}, {2}, {3}, {4}, {5}, {6}, {7}'.format(cooler[0], cooler[1], cooler[2], cooler[3], cooler[4], cooler[5], cooler[6], cooler[7])
    
sql = "SELECT * FROM CPUCooler WHERE Model ='2'"
cursor.execute(sql)
all_rows = cursor.fetchall()

for cooler2 in all_rows:
    coolerex='{0} : {1}, {2}, {3}, {4}, {5}, {6}, {7}'.format(cooler2[0], cooler2[1], cooler2[2], cooler2[3], cooler2[4], cooler2[5], cooler2[6], cooler2[7])

sql = "SELECT * FROM Motherboard WHERE Model ='1'"
cursor.execute(sql)
all_rows = cursor.fetchall()

for mobo in all_rows:
    moboex='{0} : {1}, {2}, {3}, {4}, {5}, {6}, {7}'.format(mobo[0], mobo[1], mobo[2], mobo[3], mobo[4], mobo[5], mobo[6], mobo[7])
    
sql = "SELECT * FROM Motherboard WHERE Model ='2'"
cursor.execute(sql)
all_rows = cursor.fetchall()

for mobo2 in all_rows:
    moboex='{0} : {1}, {2}, {3}, {4}, {5}, {6}, {7}'.format(mobo2[0], mobo2[1], mobo2[2], mobo2[3], mobo2[4], mobo2[5], mobo2[6], mobo2[7])

sql = "SELECT * FROM Memory WHERE Model ='1'"
cursor.execute(sql)
all_rows = cursor.fetchall()

for mem in all_rows:
    memex='{0} : {1}, {2}, {3}, {4}, {5}, {6}, {7}'.format(mem[0], mem[1], mem[2], mem[3], mem[4], mem[5], mem[6], mem[7])
    
sql = "SELECT * FROM Memory WHERE Model ='2'"
cursor.execute(sql)
all_rows = cursor.fetchall()

for mem2 in all_rows:
    memex='{0} : {1}, {2}, {3}, {4}, {5}, {6}, {7}'.format(mem2[0], mem2[1], mem2[2], mem2[3], mem2[4], mem2[5], mem2[6], mem2[7])

sql = "SELECT * FROM Storage WHERE Model ='1'"
cursor.execute(sql)
all_rows = cursor.fetchall()

for sto in all_rows:
    stoex='{0} : {1}, {2}, {3}, {4}, {5}, {6}, {7}'.format(sto[0], sto[1], sto[2], sto[3], sto[4], sto[5], sto[6], sto[7])

sql = "SELECT * FROM Storage WHERE Model ='2'"
cursor.execute(sql)
all_rows = cursor.fetchall()

for sto2 in all_rows:
    stoex='{0} : {1}, {2}, {3}, {4}, {5}, {6}, {7}'.format(sto2[0], sto2[1], sto2[2], sto2[3], sto2[4], sto2[5], sto2[6], sto2[7])

sql = "SELECT * FROM VideoCard WHERE Model ='1'"
cursor.execute(sql)
all_rows = cursor.fetchall()

for gpu in all_rows:
    gpuex='{0} : {1}, {2}, {3}, {4}, {5}, {6}, {7}'.format(gpu[0], gpu[1], gpu[2], gpu[3], gpu[4], gpu[5], gpu[6], gpu[7])

sql = "SELECT * FROM VideoCard WHERE Model ='2'"
cursor.execute(sql)
all_rows = cursor.fetchall()

for gpu2 in all_rows:
    gpu2ex='{0} : {1}, {2}, {3}, {4}, {5}, {6}, {7}'.format(gpu2[0], gpu2[1], gpu2[2], gpu2[3], gpu2[4], gpu2[5], gpu2[6], gpu2[7])

sql = "SELECT * FROM PCCase WHERE Model ='1'"
cursor.execute(sql)
all_rows = cursor.fetchall()

for case1 in all_rows:
    caseex='{0} : {1}, {2}, {3}, {4}, {5}, {6}, {7}'.format(case1[0], case1[1], case1[2], case1[3], case1[4], case1[5], case1[6], case1[7])

sql = "SELECT * FROM PCCase WHERE Model ='2'"
cursor.execute(sql)
all_rows = cursor.fetchall()

for case2 in all_rows:
    caseex='{0} : {1}, {2}, {3}, {4}, {5}, {6}, {7}'.format(case2[0], case2[1], case2[2], case2[3], case2[4], case2[5], case2[6], case2[7])
    
sql = "SELECT * FROM PowerSupply WHERE Model ='1'"
cursor.execute(sql)
all_rows = cursor.fetchall()

for psu1 in all_rows:
    psuex='{0} : {1}, {2}, {3}, {4}, {5}, {6}, {7}'.format(psu1[0], psu1[1], psu1[2], psu1[3], psu1[4], psu1[5], psu1[6], psu1[7])

sql = "SELECT * FROM PowerSupply WHERE Model ='2'"
cursor.execute(sql)
all_rows = cursor.fetchall()

for psu2 in all_rows:
    psuex='{0} : {1}, {2}, {3}, {4}, {5}, {6}, {7}'.format(psu2[0], psu2[1], psu2[2], psu2[3], psu2[4], psu2[5], psu2[6], psu2[7])

conn.commit()
conn.close()

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html', cpu=cpu, cpu2=cpu2, cooler=cooler, cooler2=cooler2, mobo=mobo, mobo2=mobo2, mem=mem, mem2=mem2, sto=sto, sto2=sto2, gpu=gpu, gpu2=gpu2, case1=case1, case2=case2, psu1=psu1, psu2=psu2)

@app.route('/list', methods=['GET', 'POST'])
def pcpartpicker():
    return render_template('list.html', cpu=cpu, cpu2=cpu2, cooler=cooler, cooler2=cooler2, mobo=mobo, mobo2=mobo2, mem=mem, mem2=mem2, sto=sto, sto2=sto2, gpu=gpu, gpu2=gpu2, case1=case1, case2=case2, psu1=psu1, psu2=psu2)

@app.route('/products/cpu', methods=['GET', 'POST'])
def cpus():
    if request.method == "POST":
        if request.form[" submit_button "] == "1":
            pass
        else:
            pass
    elif request.method == "GET":
        return render_template('cpus.html', cpu=cpu, cpu2=cpu2, cooler=cooler, cooler2=cooler2, mobo=mobo, mobo2=mobo2, mem=mem, mem2=mem2, sto=sto, sto2=sto2, gpu=gpu, gpu2=gpu2, case1=case1, case2=case2, psu1=psu1, psu2=psu2)

@app.route('/products/cpu-cooler', methods=['GET', 'POST'])
def cpucooler():
    return render_template('cpu-cooler.html', cpu=cpu, cpu2=cpu2, cooler=cooler, cooler2=cooler2, mobo=mobo, mobo2=mobo2, mem=mem, mem2=mem2, sto=sto, sto2=sto2, gpu=gpu, gpu2=gpu2, case1=case1, case2=case2, psu1=psu1, psu2=psu2)

@app.route('/products/motherboard', methods=['GET', 'POST'])
def motherboard():
    return render_template('motherboard.html', cpu=cpu, cpu2=cpu2, cooler=cooler, cooler2=cooler2, mobo=mobo, mobo2=mobo2, mem=mem, mem2=mem2, sto=sto, sto2=sto2, gpu=gpu, gpu2=gpu2, case1=case1, case2=case2, psu1=psu1, psu2=psu2)

@app.route('/products/memory', methods=['GET', 'POST'])
def memory():
    return render_template('memory.html', cpu=cpu, cpu2=cpu2, cooler=cooler, cooler2=cooler2, mobo=mobo, mobo2=mobo2, mem=mem, mem2=mem2, sto=sto, sto2=sto2, gpu=gpu, gpu2=gpu2, case1=case1, case2=case2, psu1=psu1, psu2=psu2)

@app.route('/products/storage', methods=['GET', 'POST'])
def storage():
    return render_template('storage.html', cpu=cpu, cpu2=cpu2, cooler=cooler, cooler2=cooler2, mobo=mobo, mobo2=mobo2, mem=mem, mem2=mem2, sto=sto, sto2=sto2, gpu=gpu, gpu2=gpu2, case1=case1, case2=case2, psu1=psu1, psu2=psu2)

@app.route('/products/secondarystorage', methods=['GET', 'POST'])
def secondarystorage():
    return render_template('secondarystorage.html', cpu=cpu, cpu2=cpu2, cooler=cooler, cooler2=cooler2, mobo=mobo, mobo2=mobo2, mem=mem, mem2=mem2, sto=sto, sto2=sto2, gpu=gpu, gpu2=gpu2, case1=case1, case2=case2, psu1=psu1, psu2=psu2)

@app.route('/products/video-card', methods=['GET', 'POST'])
def videocard():
    return render_template('video-card.html', cpu=cpu, cpu2=cpu2, cooler=cooler, cooler2=cooler2, mobo=mobo, mobo2=mobo2, mem=mem, mem2=mem2, sto=sto, sto2=sto2, gpu=gpu, gpu2=gpu2, case1=case1, case2=case2, psu1=psu1, psu2=psu2)

@app.route('/products/case', methods=['GET', 'POST'])
def case():
    return render_template('case.html', cpu=cpu, cpu2=cpu2, cooler=cooler, cooler2=cooler2, mobo=mobo, mobo2=mobo2, mem=mem, mem2=mem2, sto=sto, sto2=sto2, gpu=gpu, gpu2=gpu2, case1=case1, case2=case2, psu1=psu1, psu2=psu2)

@app.route('/products/power-supply', methods=['GET', 'POST'])
def powersupply():
    return render_template('power-supply.html', cpu=cpu, cpu2=cpu2, cooler=cooler, cooler2=cooler2, mobo=mobo, mobo2=mobo2, mem=mem, mem2=mem2, sto=sto, sto2=sto2, gpu=gpu, gpu2=gpu2, case1=case1, case2=case2, psu1=psu1, psu2=psu2)

@app.route('/products/optical-drive', methods=['GET', 'POST'])
def opticaldrive():
    return render_template('optical-drive.html')

@app.route('/products/operating-system', methods=['GET', 'POST'])
def operatingsystem():
    return render_template('operating-system.html')

@app.route('/products/software', methods=['GET', 'POST'])
def software():
    return render_template('software.html')

@app.route('/products/external-storage', methods=['GET', 'POST'])
def externalstorage():
    return render_template('external-storage.html')

if __name__ == '__main__':
	app.run(debug = True)

