from numpy import NaN
import pandas as pd
from IPython.display import display
import gspread
import pandas as pd
from fastapi import FastAPI
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = FastAPI()

@app.get("/get-data")
def hello():
  scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

  creds = ServiceAccountCredentials.from_json_keyfile_name(r'/app/gsheet-test-connect-0b0a5e44aec0.json', scope)

  client = gspread.authorize(creds)

  sheet = client.open('RB Bangalore Oil Change')

  sheet_instance = sheet.get_worksheet(4) 

  records_data = sheet_instance.get_all_values()

  main_sheet = pd.DataFrame.from_dict(records_data)
  new_header = main_sheet.iloc[0]
  main_sheet = main_sheet[1:]
  main_sheet.columns = new_header

  # display(main_sheet)
  # main_sheet = pd.read_excel(r'C:\Users\soumi\Desktop\RB\VHM-Requirement\RB Bangalore Oil Change.xlsx','Main sheet')
  # vehicle_parts_schedule = pd.read_excel(r'C:\Users\soumi\Desktop\RB\VHM-Requirement\OEM Service Details.xlsx', 'Schduled parts change sheet')

  enabled_vehicles = main_sheet.query("Status == 'enabled'")

  activa_dio_bs6 = {
    "Name": ['Activa 6G', 'Dio (BS6)'],
    "Kms schedule": [1000, 6000, 12000, 18000, 24000, 30000, 36000, 42000, 48000, 54000, 60000, 66000, 72000], 
    "Period ( days)": [45, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72], 
    "Air cleaner element": [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1], 
    "Spark Plug": [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 
    "Engine Oil": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    "Drive Belt": [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], 
    "Final Drive Oil": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  }

  sr160_sr_storm125 = {
    "Name" : ['SR 160', 'SR 160 ABS (BS6)', 'SR 125'],
    "Kms schedule": [750, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000, 27000, 30000, 33000, 36000], 
    "Period ( days)": [30, 90, 180, 270, 360, 450, 540, 630, 720, 810, 900, 990, 1080], 
    "Engine Oil": [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 
    "Gear Box oil": [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
    "Spark Plug": [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], 
    "Drive Belt": [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
    "Fuel filter": [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0], 
    "Air filter element": [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]
  }

  avenger = {
    "Name": ["Avenger Cruise 220 (BS6)"],
    "Kms schedule": [750, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000], 
    "Period ( days)" : [45, 240, 360, 480, 600, 720, 840, 960, 1080, 1200, 1320, 1440, 1560], 
    "Engine oil": [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 
    "Air cleaner element": [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1], 
    "Spark Plug": [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]
  }

  maestro = {
    "Name": ["Maestro"],
    "Kms schedule": [500, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000, 27000, 30000, 33000, 36000], 
    "Period ( days)": [60, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200], 
    "Air cleaner element": [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0], 
    "Spark Plug": [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0], 
    "Engine Oil": [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 
    "Final Drive Oil": [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]
  }

  duke = {
    "Name": ["Duke 200 (BS 6)", "Duke 250 (BS6)", "Duke 200 (ABS)"],
    "Kms schedule": [1000, 7500, 15000, 22500, 30000, 37500, 45000, 52500, 60000, 67500, 75000, 82500, 90000], 
    "period ( days)": [45, 150, 240, 330, 420, 510, 600, 690, 780, 870, 960, 1050, 1140], 
    "Engine oil": [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    "Oil filter": [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    "Air filter element": [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    "Spark Plug": [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 
    "Fuel filter": [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    "Brake Oil replacement": [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  }

  pulsar = {
    "Name": ["Pulsar 250F (BS6)", "Pulsar 250N (BS6)"],
    "Kms schedule": [750, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000], 
    "Period ( days)": [45, 240, 360, 480, 600, 720, 840, 960, 1080, 1200, 1320, 1440, 1560], 
    "Engine Oil": [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 
    "Engine Oil filter": [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 
    "Air cleaner element": [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], 
    "Spark Plug": [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]
  }

  xpulse = {
    "Name": ["X-Pulse (BS6)"],
    "Kms schedule": [500, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000, 27000, 30000, 33000, 36000], 
    "Air cleaner element": [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], 
    "Spark Plug": [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], 
    "Engine oil": [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
  }

  xblade_hornet = {
    "Name": ["X-Blade", "X-Blade (BS6)", "Hornet 2.0"],
    "Kms schedule": [1000, 6000, 12000, 18000, 24000, 30000, 36000, 42000, 48000, 54000, 60000, 66000, 72000], 
    "Period ( days)": [30, 180, 360, 540, 720, 900, 1080, 1260, 1440, 1620, 1800, 1980, 2160], 
    "Air cleaner element": [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1], 
    "Spark Plug": [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 
    "Engine Oil": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    "Brake fluid": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  }

  fz = {
    "Name":["FZ V3 (BS 6)", "FZ", "FZ V3"],
    "Kms schedule": [1000, 4000, 7000, 10000, 13000, 16000, 19000, 22000, 25000, 28000, 31000, 34000, 37000], 
    "period ( days)": [30, 150, 270, 390, 510, 630, 750, 870, 990, 1110, 1230, 1350, 1470], 
    "Spark Plug": [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
    "Air filter element": [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
    "Brake fluid": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    "Front fork oil": [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    "Engine oil": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    "Oil filter": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
  }

  himalayan = {
    "Name": ["Himalayan", "Himalayan Gravel Grey", "Himalayan Pine Green", "Himalayan BS6 (Tourer Edition)", "Himalayan Scram 411", "Himalayan (BS 6)"],
    "Kms schedule": [500, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000], 
    "Days": [45, 180, 365, 545, 725, 905, 1085, 1265, 1445, 1625, 1805, 1985, 2165], 
    "Engine oil": [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 
    "Front fork oil": [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], 
    "Brake fluid": [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], 
    "Engine Oil filter elemen": [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 
    "Spark Plug": [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1], 
    "Air filter element": [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
  }

  apache = {
    "Name": ["Apache RTR 180 (BS6)", "Apache RTR 180"],
    "Kms schedule": [750, 2500, 5000, 85000, 11500, 14500, 17500, 20500, 23500, 26500, 29500, 32500, 35500], 
    "Period schedule": [30, 90, 180, 240, 360, 0, 0, 0, 0, 0, 0, 0, 0], 
    "Air cleaner element": [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1], 
    "Spark Plug": [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 
    "Engine Oil": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    "Drive Belt": [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], 
    "Final Drive Oil": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  }

  access = {
    "Name": ["Access 125", "Access 125 (BS6)"],
    "Kms schedule": [750, 3500, 5500, 7500, 9500, 11500, 13500, 15500, 17500, 19500, 21500, 23500, 25500], 
    "Period schedule": [30, 90, 140, 190, 240, 290, 340], 
    "Air cleaner element": [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1], 
    "Spark Plug": [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1], 
    "Engine Oil": [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1], 
    "Drive Belt": [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1], 
    "Oil filter": [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  }

  enabled_activa_dio = enabled_vehicles.query("BikeModel == 'Activa 6G' or BikeModel == 'Dio (BS6)' and (Odo != '' or Odo != 'NaN')")
  enabled_sr160_sr_storm125 = enabled_vehicles.query("BikeModel == 'SR 160' or BikeModel == 'SR 160 ABS (BS6)' or BikeModel == 'SR 125' and (Odo != '' or Odo != 'NaN')")
  enabled_avenger = enabled_vehicles.query("BikeModel == 'Avenger Cruise 220 (BS6)' and (Odo != '' or Odo != 'NaN')")
  enabled_maestro = enabled_vehicles.query("BikeModel == 'Maestro' and (Odo != '' or Odo != 'NaN')")
  enabled_duke = enabled_vehicles.query("BikeModel == 'Duke 200 (BS 6)' or BikeModel == 'Duke 250 (BS6)' or BikeModel == 'Duke 200 (ABS)' and (Odo != '' or Odo != 'NaN')")
  enabled_pulsar = enabled_vehicles.query("BikeModel == 'Pulsar 250F (BS6)' or BikeModel == 'Pulsar 250N (BS6)' and (Odo != '' or Odo != 'NaN')")
  enabled_xpulse = enabled_vehicles.query("BikeModel == 'X-Pulse (BS6)' and (Odo != '' or Odo != 'NaN')")
  enabled_xblade_hornet = enabled_vehicles.query( "BikeModel == 'X-Blade' or BikeModel == 'X-Blade (BS6)' or BikeModel == 'Hornet 2.0' and (Odo != '' or Odo != 'NaN')")
  enabled_fz = enabled_vehicles.query("BikeModel == 'FZ V3 (BS 6)' or BikeModel == 'FZ' or BikeModel == 'FZ V3' and (Odo != '' or Odo != 'NaN')")
  enabled_himalayan = enabled_vehicles.query("BikeModel == 'Himalayan' or BikeModel == 'Himalayan Gravel Grey' or BikeModel == 'Himalayan Pine Green' or BikeModel == 'Himalayan BS6 (Tourer Edition)' or BikeModel == 'Himalayan Scram 411' or BikeModel == 'Himalayan (BS 6)' and (Odo != '' or Odo != 'NaN')")
  enabled_apache = enabled_vehicles.query("BikeModel == 'Apache RTR 180 (BS6)' or BikeModel == 'Apache RTR 180' and (Odo != '' or Odo != 'NaN')")
  enabled_access = enabled_vehicles.query("BikeModel == 'Access 125' or BikeModel == 'Access 125 (BS6) ' and (Odo != '' or Odo != 'NaN')")
  # print(enabled_sr160_sr_storm125)
  # print(enabled_activa_dio)
  # print(enabled_avenger, enabled_maestro)
  # print(enabled_duke)
  # print(enabled_pulsar)
  # print(enabled_xpulse)
  # print(enabled_xblade_hornet)
  # print(enabled_fz, enabled_himalayan, enabled_apache)
  # print(enabled_access)
  service_bikes = []
  # print(enabled_vehicles.count())
  # print(enabled_access.count())
  # print(enabled_activa_dio.count())
  # print(enabled_apache.count())
  # print(enabled_avenger.count())
  # print(enabled_xblade_hornet.count())
  # print(enabled_xpulse.count())
  # print(enabled_duke.count())
  # print(enabled_fz.count())
  # print(enabled_himalayan.count())
  # print(enabled_maestro.count())
  # print(enabled_pulsar.count())
  # print(enabled_sr160_sr_storm125.count())
  #activa and dio
  for index, row in enabled_activa_dio.iterrows():
    for index, km in enumerate(activa_dio_bs6["Kms schedule"]):
      if int(row['Odo']) != NaN and int(row['Odo']) >= km-300 and int(row['Odo']) <= km+300:
        if row['Oil Changed on'] == '' or (int(row['Oil Changed on']) <= km-500 or int(row['Oil Changed on']) >= km + 500):
          service = activa_dio_bs6["Air cleaner element"][index] * 187 + activa_dio_bs6["Spark Plug"][index] * 154 + activa_dio_bs6["Engine Oil"][index] * 275 + activa_dio_bs6["Drive Belt"][index] * 377.4 + activa_dio_bs6["Final Drive Oil"][index] * 0
          bike = {
            "Vehicle No": row["Registration No"],
            "Model": row["BikeModel"],
            "Odo": row["Odo"],
            "Service Cost": service,
            "Service Type": index+1
          }
          service_bikes.append(bike)

  #aprilia sr
  for index, row in enabled_sr160_sr_storm125.iterrows():
    for index, km in enumerate(sr160_sr_storm125["Kms schedule"]):
      if (row['Odo'] != NaN or row['Odo'] != '') and int(row['Odo']) >= km-300 and int(row['Odo']) <= km+300:
        if row['Oil Changed on'] == '' or (int(row['Oil Changed on']) <= km-500 or int(row['Oil Changed on']) >= km + 500):
          service = sr160_sr_storm125["Engine Oil"][index] * 1 + sr160_sr_storm125["Gear Box oil"][index] * 1 + sr160_sr_storm125["Spark Plug"][index] * 1 + sr160_sr_storm125["Drive Belt"][index] * 1 + sr160_sr_storm125["Fuel filter"][index] * 1 + sr160_sr_storm125["Air filter element"][index] * 1
          bike = {
            "Vehicle No": row["Registration No"],
            "Model": row["BikeModel"],
            "Odo": row["Odo"],
            "Service Cost": service,
            "Service Type": index+1
          }
          service_bikes.append(bike)

  #avenger
  for index, row in enabled_avenger.iterrows():
    for index, km in enumerate(avenger["Kms schedule"]):
      if row['Odo'] != NaN and int(row['Odo']) >= km-300 and int(row['Odo']) <= km+300:
        if row['Oil Changed on'] == '' or (int(row['Oil Changed on']) <= km-500 or int(row['Oil Changed on']) >= km + 500):
          service = avenger["Engine oil"][index] * 1 + avenger["Air cleaner element"][index] * 1 + avenger["Spark Plug"][index] * 1
          bike = {
            "Vehicle No": row["Registration No"],
            "Model": row["BikeModel"],
            "Odo": row["Odo"],
            "Service Cost": service,
            "Service Type": index+1
          }
          service_bikes.append(bike)

  #maestro
  for index, row in enabled_maestro.iterrows():
    for index, km in enumerate(maestro["Kms schedule"]):
      if row['Odo'] != NaN and int(row['Odo']) >= km-300 and int(row['Odo']) <= km + 300:
        if row['Oil Changed on'] == '' or (int(row['Oil Changed on']) <= km-500 or int(row['Oil Changed on']) >= km + 500):
          service = maestro["Air cleaner element"][index] * 1 + maestro["Spark Plug"][index] * 1 + maestro["Engine Oil"][index] * 1 + maestro["Final Drive Oil"][index] * 1
          bike = {
            "Vehicle No": row["Registration No"],
            "Model": row["BikeModel"],
            "Odo": row["Odo"],
            "Service Cost": service,
            "Service Type": index+1
          }
          service_bikes.append(bike)

  #duke
  for index, row in enabled_duke.iterrows():
    for index, km in enumerate(duke["Kms schedule"]):
      if row['Odo'] != NaN and int(row['Odo']) >= km-300 and int(row['Odo']) <= km+300:
        if row['Oil Changed on'] == '' or (int(row['Oil Changed on']) <= km-500 or int(row['Oil Changed on']) >= km + 500):
          service = duke["Engine oil"][index] * 1 + duke["Oil filter"][index] * 1 + duke["Air filter element"][index] * 1 + duke["Spark Plug"][index] * 1 + duke["Fuel filter"][index] * 1 + duke["Brake Oil replacement"][index] * 1
          bike = {
            "Vehicle No": row["Registration No"],
            "Model": row["BikeModel"],
            "Odo": row["Odo"],
            "Service Cost": service,
            "Service Type": index+1
          }
          service_bikes.append(bike)

  #pulsar
  for index, row in enabled_pulsar.iterrows():
    for index, km in enumerate(pulsar["Kms schedule"]):
      if row['Odo'] != NaN and int(row['Odo']) >= km-300 and int(row['Odo']) <= km+300:
        if row['Oil Changed on'] == '' or (int(row['Oil Changed on']) <= km-500 or int(row['Oil Changed on']) >= km + 500):
          service = pulsar["Engine Oil"][index] * 1 + pulsar["Engine Oil filter"][index] * 1 + pulsar["Air cleaner element"][index] * 1 + pulsar["Spark Plug"][index] * 1
          bike = {
            "Vehicle No": row["Registration No"],
            "Model": row["BikeModel"],
            "Odo": row["Odo"],
            "Service Cost": service,
            "Service Type": index+1
          }
          service_bikes.append(bike)

  #xpulse
  for index, row in enabled_xpulse.iterrows():
    for index, km in enumerate(xpulse["Kms schedule"]):
      if row['Odo'] != NaN and int(row['Odo']) >= km-300 and int(row['Odo']) <= km+300:
        if row['Oil Changed on'] == '' or (int(row['Oil Changed on']) <= km-500 or int(row['Oil Changed on']) >= km + 500):
          service = xpulse["Air cleaner element"][index] * 1 + xpulse["Spark Plug"][index] * 1 + xpulse["Engine oil"][index] * 1
          bike = {
            "Vehicle No": row["Registration No"],
            "Model": row["BikeModel"],
            "Odo": row["Odo"],
            "Service Cost": service,
            "Service Type": index+1
          }
          service_bikes.append(bike)

  #xblade hornet
  for index, row in enabled_xblade_hornet.iterrows():
    for index, km in enumerate(xblade_hornet["Kms schedule"]):
      if row['Odo'] != NaN and int(row['Odo']) >= km-300 and int(row['Odo']) <= km+300:
        if row['Oil Changed on'] == '' or (int(row['Oil Changed on']) <= km-500 or int(row['Oil Changed on']) >= km + 500):
          service = xblade_hornet["Air cleaner element"][index] * 1 + xblade_hornet["Spark Plug"][index] * 1 + xblade_hornet["Engine Oil"][index] * 1 + xblade_hornet["Brake fluid"][index] * 1
          bike = {
            "Vehicle No": row["Registration No"],
            "Model": row["BikeModel"],
            "Odo": row["Odo"],
            "Service Cost": service,
            "Service Type": index+1
          }
          service_bikes.append(bike)

  #fz
  for index, row in enabled_fz.iterrows():
    for index, km in enumerate(fz["Kms schedule"]):
      if int(row['Odo']) != NaN and int(row['Odo']) >= km-300 and int(row['Odo']) <= km+300:
        if row['Oil Changed on'] == '' or (int(row['Oil Changed on']) <= km-500 or int(row['Oil Changed on']) >= km + 500):
          service = fz["Spark Plug"][index] * 1 + fz["Air filter element"][index] * 1 + fz["Brake fluid"][index] * 1 + fz["Front fork oil"][index] * 1 + fz["Engine oil"][index] * 1 + fz["Oil filter"][index] * 1
          bike = {
            "Vehicle No": row["Registration No"],
            "Model": row["BikeModel"],
            "Odo": row["Odo"],
            "Service Cost": service,
            "Service Type": index+1
          }
          service_bikes.append(bike)

  #himalayan
  for index, row in enabled_himalayan.iterrows():
    for index, km in enumerate(himalayan["Kms schedule"]):
      if int(row['Odo']) != NaN and int(row['Odo']) >= km-300 and int(row['Odo']) <= km+300:
        if row['Oil Changed on'] == '' or (int(row['Oil Changed on']) <= km-500 or int(row['Oil Changed on']) >= km + 500):
          service = himalayan["Engine oil"][index] * 1 + himalayan["Front fork oil"][index] * 1 + himalayan["Brake fluid"][index] * 1 + himalayan["Engine Oil filter elemen"][index] * 1 + himalayan["Spark Plug"][index] * 1 + himalayan["Air filter element"][index] * 1
          bike = {
            "Vehicle No": row["Registration No"],
            "Model": row["BikeModel"],
            "Odo": row["Odo"],
            "Service Cost": service,
            "Service Type": index+1
          }
          service_bikes.append(bike)

  #apache
  for index, row in enabled_apache.iterrows():
    for index, km in enumerate(apache["Kms schedule"]):
      if int(row['Odo']) != NaN and int(row['Odo']) >= km-300 and int(row['Odo']) <= km+300:
        if row['Oil Changed on'] == '' or (int(row['Oil Changed on']) <= km-500 or int(row['Oil Changed on']) >= km + 500):
          service = apache["Air cleaner element"][index] * 1 + apache["Spark Plug"][index] * 1 + apache["Engine Oil"][index] * 1 + apache["Drive Belt"][index] * 1 + apache["Final Drive Oil"][index] * 1
          bike = {
            "Vehicle No": row["Registration No"],
            "Model": row["BikeModel"],
            "Odo": row["Odo"],
            "Service Cost": service,
            "Service Type": index+1
          }
          service_bikes.append(bike)

  #access
  for index, row in enabled_access.iterrows():
    for index, km in enumerate(access["Kms schedule"]):
      if (row['Odo'] == ''):
        continue
      else:
        # print(type(row["Odo"]))
        if int(row['Odo']) >= km-300 and int(row['Odo']) <= km+300:
          if (row['Oil Changed on'] == '') or (int(row['Oil Changed on']) <= km-500 or int(row['Oil Changed on']) >= km + 500):
            service = access["Air cleaner element"][index] * 1 + access["Spark Plug"][index] * 1 + access["Engine Oil"][index] * 1 + access["Drive Belt"][index] * 1 + access["Oil filter"][index] * 1
            bike = {
              "Vehicle No": row["Registration No"],
              "Model": row["BikeModel"],
              "Odo": row["Odo"],
              "Service Cost": service,
              "Service Type": index+1
            }
            service_bikes.append(bike)

  df = pd.DataFrame(service_bikes)
  new_header = ["Vehicle No", "Model", "Odo", "Service Cost", "Service Type"]
  df = df[1:]
  df.columns = new_header
  # print(df.columns)
  df.drop_duplicates(subset="Vehicle No", keep="last")

  # display(df)
  # print(df.to_json())
  # return df.to_json()
  return(df.to_json())


#DONE: test google sheets integration 
#TODO: frontend