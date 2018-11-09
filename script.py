import os
import os.path
import csv
import string
import sys

Hotel=[]
def Lecture():

    with open('/usr/local/nagios/scripts/Devices_list.csv')as csvfile:
        cr = csv.reader(csvfile, delimiter = ';')
        for line in cr:
            Hotel.append(line)
    return Hotel



def Analyse(CodeH):

    
    if os.path.exists('/usr/local/nagios/etc/routers/'+CodeH+'.cfg'):
        return 1
    else: 
        return 0


def Ecriture(CodeH,adress):
    
    creation = os.system('cp /usr/local/nagios/scripts/Temp.cfg /usr/local/nagios/etc/routers/'+CodeH+'.cfg')
    new = open("/usr/local/nagios/etc/routers/"+CodeH+'.cfg','r+')
    contenu = new.read().replace('$CODE',CodeH).replace('$ADDRESS',adress)
    new.seek(0)
    new.write(contenu) 
    new.close()

           


def Main():
    
    Hotel = Lecture() 
    for line in Hotel:      
        if Analyse(line[0]):
            print ('Fichier Existant')
            Ecriture(line[0],line[1])
        else:
            Ecriture(line[0],line[1])
            print ('Fichier Creer')


Main()
