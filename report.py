import csv
import json


def main(): 
    filename = input("Please enter the filename: ")
    with open(filename, newline='') as file: 
        keys = ['vehicle_name','vin', 'timezone', 'start_time', 'end_time',
         'odometer', 'energy_added', 'start_range', 'end_range', 
         'range_added', 'duration', 'supercharging', 'supercharger', 'max_charge_power', 
         'location', 'coordinates', 'temperature', 'comments']
        data = csv.DictReader(file, fieldnames=keys)
        next(data) # discard the first row
        charge_added_total = 0
        
        for row in data: 
            if row['supercharging'] == 'false' and filterLocation(row['coordinates']):
                charge_added_total += float(row['energy_added'])


        total_cost = round(charge_added_total * .12, 2)

        print("Total Charged (kwh): ", charge_added_total)
        print("Total Cost @ 12 cents/kwh: $", total_cost)

            
def filterLocation(location): 
    coordinates = location.split(',')
    latitude = float(coordinates[0])
    longitude = float(coordinates[1])

    return round(latitude, 3) == 40.061 and round(longitude, 3) == -83.052

if __name__ == "__main__":
    main() 