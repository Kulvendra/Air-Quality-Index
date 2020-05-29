import os
import glob

import  pandas as pd 
pd.options.mode.chained_assignment = None

def get_size(pollutant):
    length = len([1 for i in pollutant if i > 0])
    if(length==0):
        length = 1   
    
    return length

PM25=[]
PM10=[]
NO2=[]
SO2=[]
O3=[]
CO=[]

PM25_BL=[]
PM10_BL=[]
NO2_BL=[]
SO2_BL=[]
O3_BL=[]
CO_BL=[]


path =  os.getcwd() + "/csv/"
extension = 'csv'
os.chdir(path)
result = [i for i in glob.glob('*.{}'.format(extension))]

print("Your all CSV file are listed here => ",result,"\n")

# Getting the Lockdown Date as input from User
lockdown_date = input("Enter the Lockdown Starting Date (Example = 2020-03-24) : ")
date1 = input("Enter the date before lockdown (Exampe : 2020-03-05)    : ")
print("\n")

for city in result:
    # reading the CSV Historical Data of AQI
    
    df = pd.read_csv('./'+city)

    df = df.rename(columns={" pm25":"pm25",
                            " pm10":"pm10",
                            " o3":"o3",
                            " no2":"no2",
                            " so2":"so2",
                            " co":"co"})
    # print(df.columns)

    # converting the date field from String to Date
    df['date'] = pd.to_datetime(df.date)

    # ---------------------------------------------------------After Lockdown---------------------------------------------------------------------------

  

    df_lockdown = df.loc[df['date']>lockdown_date]                  # Geting the required data after the lockdown date
    df_lockdown =df_lockdown.sort_values(by= 'date')                # Sorting that data by Dates 

    df_lockdown.replace(' ','0',inplace=True)                       # Replacing the empty data with 0
    # print(df_lockdown)

    pm25 =  df_lockdown.get('pm25',"0") 
    pm10 = df_lockdown.get('pm10',"0")
    no2 = df_lockdown.get('no2',"0")
    so2 = df_lockdown.get('so2',"0")
    o3 = df_lockdown.get('o3',"0")
    co = df_lockdown.get('co',"0")

    pm25 = [int(i) for i in pm25]                                   # Converting the fields from String to Int
    pm10 = [int(i) for i in pm10]
    no2 = [int(i) for i in no2]
    so2 = [int(i) for i in so2]
    o3 = [int(i) for i in o3]
    co = [int(i) for i in co]


    pm25_AVG = sum(pm25)/len(pm25)                                  # Calculating the Average 
    pm10_AVG = sum(pm10)/len(pm10)
    no2_AVG = sum(no2)/len(no2)
    so2_AVG = sum(so2)/len(so2)
    o3_AVG = sum(o3)/len(o3)
    co_AVG = sum(co)/len(co)


    print("Average values AFTER LOCKDOWN =>",city,"=> PM2.5 = ",pm25_AVG," || PM10 = ",pm10_AVG," || NO2 = ",no2_AVG," || SO2 = ",so2_AVG," || O3 = ",o3_AVG," || CO = ",co_AVG)
    PM25.append(pm25_AVG)
    PM10.append(pm10_AVG)
    NO2.append(no2_AVG)
    SO2.append(so2_AVG)
    O3.append(o3_AVG)
    CO.append(co_AVG)

    # ---------------------------------------------------------Before Lockdown---------------------------------------------------------------------------


    mask = (df['date'] >= date1) & (df['date']< lockdown_date)      # Getting the data btw input date and lockdown date
    before_lockdown = df.loc[mask]
    before_lockdown.replace(' ','0',inplace=True)

    # print(before_lockdown)

    pm25_bl = before_lockdown.get('pm25',"0") 
    pm10_bl = before_lockdown.get('pm10',"0")
    no2_bl = before_lockdown.get('no2',"0")
    so2_bl = before_lockdown.get('so2',"0")
    o3_bl = before_lockdown.get('o3',"0")
    co_bl = before_lockdown.get('co',"0")


    pm25_bl = [int(i) for i in pm25_bl]
    pm10_bl = [int(i) for i in pm10_bl]
    no2_bl = [int(i) for i in no2_bl]
    so2_bl = [int(i) for i in so2_bl]
    o3_bl = [int(i) for i in o3_bl]
    co_bl = [int(i) for i in co_bl]



    pm25_AVG_bl = sum(pm25_bl)/len(pm25_bl)
    pm10_AVG_bl = sum(pm10_bl)/len(pm10_bl)
    no2_AVG_bl = sum(no2_bl)/len(no2_bl)
    so2_AVG_bl = sum(so2_bl)/len(so2_bl)
    o3_AVG_bl = sum(o3_bl)/len(o3_bl)
    co_AVG_bl = sum(co_bl)/len(co_bl)


    print("Average values BEFORE LOCKDOWN =>",city,"=> PM2.5 = ",pm25_AVG_bl," || PM10 = ",pm10_AVG_bl," || NO2 = ",no2_AVG_bl," || SO2 = ",so2_AVG_bl," || O3 = ",o3_AVG_bl," || CO = ",co_AVG_bl)

    print("\n")
    PM25_BL.append(pm25_AVG_bl)
    PM10_BL.append(pm10_AVG_bl)
    NO2_BL.append(no2_AVG_bl)
    SO2_BL.append(so2_AVG_bl)
    O3_BL.append(o3_AVG_bl)
    CO_BL.append(co_AVG_bl)

# print(PM25,PM10,NO2)
# print(PM25_BL,PM10_BL,NO2_BL)

PM25_AVG = sum(PM25)/get_size(PM25)
PM10_AVG = sum(PM10)/get_size(PM10)
NO2_AVG = sum(NO2)/get_size(NO2)
SO2_AVG = sum(SO2)/get_size(SO2)
O3_AVG = sum(O3)/get_size(O3)
CO_AVG = sum(CO)/get_size(CO)
# CO_AVG = sum(CO)/len([1 for i in CO if i > 0])



PM25_AVG_BL = sum(PM25_BL)/get_size(PM25_BL)
PM10_AVG_BL = sum(PM10_BL)/get_size(PM10_BL)
NO2_AVG_BL = sum(NO2_BL)/get_size(NO2_BL)
SO2_AVG_BL = sum(SO2_BL)/get_size(SO2_BL)
O3_AVG_BL = sum(O3_BL)/get_size(O3_BL)
CO_AVG_BL = sum(CO_BL)/get_size(CO_BL)



print("\nOverall Average values AFTER LOCKDOWN => PM2.5 = ",PM25_AVG," || PM10 = ",PM10_AVG," || NO2 = ",NO2_AVG," || SO2 = ",SO2_AVG," || O3 = ", O3_AVG," || CO = ",CO_AVG)
print("Overall Average values BEFORE LOCKDOWN => PM2.5 = ",PM25_AVG_BL," || PM10 = ",PM10_AVG_BL," || NO2 = ",NO2_AVG_BL," || SO2 = ",SO2_AVG_BL," || O3 = ", O3_AVG_BL," || CO = ",CO_AVG_BL)







