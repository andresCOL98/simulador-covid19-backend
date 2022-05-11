import csv
from datetime import date 
from datetime import timedelta

def readCsv(name_country):
    today = date.today()
    yesterday = today - timedelta(days = 1)
    file_name = str(yesterday.strftime('%m-%d-%Y'))+'.csv'

    confirmed = 0
    deaths = 0
    
    with open('C:/Users/User/Documents/AndresCamiloCortes/Semestre10p1/Tesis/SimuladorCovid19/backEnd/src/apps/dashboard/static/GLOBAL/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/'+file_name) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if(row[3] == name_country):
                confirmed += int(row[7])
                deaths += int(row[8])
                print(deaths)

    return confirmed, deaths

