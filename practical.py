import pandas as pd

# Creating dictionary with vehicle records
vehicle_data = [
    {"REG_NO": "GJ01AB1234", "OWNER_NAME": "Jash Patel", "VEHICLE_TYPE": "Car", "MODEL_YEAR": 2020, "CITY": "Ahmedabad", "REGISTRATION_DATE": "2022-03-15"},
    {"REG_NO": "GJ02CD5678", "OWNER_NAME": "Rahul Shah", "VEHICLE_TYPE": "Bike", "MODEL_YEAR": 2017, "CITY": "Surat", "REGISTRATION_DATE": "2019-06-10"},
    {"REG_NO": "GJ03EF9012", "OWNER_NAME": "Priya Mehta", "VEHICLE_TYPE": "Car", "MODEL_YEAR": 2019, "CITY": "Ahmedabad", "REGISTRATION_DATE": "2021-11-25"},
    {"REG_NO": "GJ04GH3456", "OWNER_NAME": "Amit Kumar", "VEHICLE_TYPE": "Truck", "MODEL_YEAR": 2015, "CITY": "Vadodara", "REGISTRATION_DATE": "2018-07-30"},
    {"REG_NO": "GJ05IJ7890", "OWNER_NAME": "Neha Joshi", "VEHICLE_TYPE": "Scooter", "MODEL_YEAR": 2021, "CITY": "Ahmedabad", "REGISTRATION_DATE": "2023-01-12"},
    {"REG_NO": "GJ06KL2345", "OWNER_NAME": "Ravi Verma", "VEHICLE_TYPE": "Car", "MODEL_YEAR": 2018, "CITY": "Rajkot", "REGISTRATION_DATE": "2020-09-05"},
    {"REG_NO": "GJ07MN6789", "OWNER_NAME": "Sneha Desai", "VEHICLE_TYPE": "Bike", "MODEL_YEAR": 2022, "CITY": "Ahmedabad", "REGISTRATION_DATE": "2024-02-18"},
    {"REG_NO": "GJ08OP1122", "OWNER_NAME": "Karan Patel", "VEHICLE_TYPE": "Car", "MODEL_YEAR": 2016, "CITY": "Surat", "REGISTRATION_DATE": "2017-04-22"},
    {"REG_NO": "GJ09QR3344", "OWNER_NAME": "Pooja Shah", "VEHICLE_TYPE": "Scooter", "MODEL_YEAR": 2023, "CITY": "Ahmedabad", "REGISTRATION_DATE": "2023-08-10"},
    {"REG_NO": "GJ10ST5566", "OWNER_NAME": "Manish Singh", "VEHICLE_TYPE": "Truck", "MODEL_YEAR": 2019, "CITY": "Vadodara", "REGISTRATION_DATE": "2022-05-19"}
]

df = pd.DataFrame(vehicle_data)
print(df)

df.to_csv("vehicle_data.csv",index=False)
print("csv file is ready")

# df_loaded = pd.read_csv("vehicle_data.csv")
# print(df_loaded)

ahmedabad_vehicles = df[df["CITY"] == "Ahmedabad"]
print("\nVehicles in Ahmedabad:\n", ahmedabad_vehicles)

model_after_2018 = df[df["MODEL_YEAR"] > 2018]
print(f"\nvehical After 2018 is \n {model_after_2018}")

recent_ragistrastion = df[df["REGISTRATION_DATE"] > "2022_01_01"]
print(f"\n vehical after 2022 is \n {recent_ragistrastion}")