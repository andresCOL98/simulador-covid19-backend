import csv
from datetime import date 
from datetime import timedelta
from operator import ge 
from pathlib import Path
import os
from unicodedata import name

def getPathFileOrDefault():
    
    today = date.today()
    yesterday = today - timedelta(days = 1)
    fecha = str(yesterday.strftime('%m-%d-%Y'))
    DirFile = 'static/GLOBAL/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports'
    typeExt = '.csv'
    DirPath = Path(__file__).resolve().parent.parent
    file_name = fecha + typeExt
    FullPath = os.path.join(DirPath, DirFile, file_name)
    IsCorrect = os.path.exists(FullPath)

    if (not IsCorrect):
        DirFileOptional = 'static/Temp'
        fecha = '10-17-2022'
        defaultFile = fecha + typeExt
        FullPath = os.path.join(DirPath, DirFileOptional, defaultFile)

    return FullPath, fecha


def readCsvGeneralData(fullPathFile, name_country):
    confirmed = 0
    deaths = 0

    with open(fullPathFile) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if(row[3] == name_country):
                confirmed += int(row[7])
                deaths += int(row[8])
    return confirmed, deaths

def readCsvVaccunes(name_country):
    vaccunes = 0
    DirPath = Path(__file__).resolve().parent.parent
    DirFileOptional = 'C:/Users/User/Documents/AndresCamiloCortes/Semestre10p1/Tesis/SimuladorCovid19/backEnd/src/apps/dashboard/static/Temp'
    fecha = 'vaccinations'
    typeExt = '.csv'
    defaultFile = fecha + typeExt
    FullPath = os.path.join(DirPath, DirFileOptional, defaultFile)

    with open(FullPath) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if(row[0] == name_country):
                print(row[0])
                print(name_country)
                if(row[3]):
                    print(row[3])
                    vaccunes = int(float(row[3]))
    return vaccunes

def getDataCovid(name_country):

    values = getPathFileOrDefault()
    fullPathFile = values[0]
    generalData = readCsvGeneralData(fullPathFile, name_country)
    vaccunes = readCsvVaccunes(name_country)
    currentDate = values[1]
    

    return generalData[0], generalData[1], currentDate , vaccunes