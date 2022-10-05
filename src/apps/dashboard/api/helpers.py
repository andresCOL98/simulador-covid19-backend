import csv
from datetime import date 
from datetime import timedelta 
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
        fecha = '09-26-2022'
        defaultFile = fecha + typeExt
        FullPath = os.path.join(DirPath, DirFileOptional, defaultFile)

    return FullPath, fecha

def readCsv(name_country):

    confirmed = 0
    deaths = 0
    values = getPathFileOrDefault()
    FullPathFile = values[0]
    CurrentDate = values[1]

    with open(FullPathFile) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if(row[3] == name_country):
                confirmed += int(row[7])
                deaths += int(row[8])

    return confirmed, deaths, CurrentDate

