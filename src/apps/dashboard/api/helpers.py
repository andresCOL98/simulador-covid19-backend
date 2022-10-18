import csv
from datetime import date 
from datetime import timedelta
from operator import ge 
from pathlib import Path
import os

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


def readCsvGeneralData(name_country):
    confirmed = 0
    deaths = 0
    DirPath = Path(__file__).resolve().parent.parent
    DirFileOptional = 'static/Temp'
    fecha = 'time_series_covid19_vaccine_global'
    typeExt = '.csv'
    defaultFile = fecha + typeExt
    FullPath = os.path.join(DirPath, DirFileOptional, defaultFile)

    with open(FullPath) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if(row[3] == name_country):
                confirmed += int(row[7])
                deaths += int(row[8])
    return confirmed, deaths

def readCsvVaccunes(fullPathFile , name_country):
    vaccunes = 0.0
    with open(fullPathFile) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if(row[3] == name_country):
                vaccunes += int(row[4])
    return vaccunes

def getDataCovid(name_country):

    values = getPathFileOrDefault()
    fullPathFile = values[0]
    generalData = readCsvGeneralData(name_country)
    vaccunes = readCsvVaccunes(name_country)
    currentDate = values[1]
    

    return generalData[0], generalData[1], currentDate , vaccunes

