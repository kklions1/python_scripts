import csv
import json


def main(): 
    filename = input("Please enter the filename: ")
    with open(filename, newline='') as file: 
        keys = ['vehicle_name','vin', 'timezone', 'start_time', 'end_time',
         'odometer', 'power_drawn', 'energy_added', 'start_range', 'end_range', 
         'range_added', 'duration', 'supercharging', 'supercharger', 'max_charge_power', 
         'fast_charger_present','connector_type', 'location', 'coordinates', 'user_charge_location', 
         'cost', 'temperature']
        data = csv.DictReader(file, fieldnames=keys)
        next(data) # discard the first row
        charge_added_total = 0
        total_cost = 0
        
        for row in data: 
            if row['supercharging'] == 'false' and filter_address(row['user_charge_location']):
                charge_added_total += float(row['energy_added'])
                total_cost += float(row['cost'])


        # total_cost = round(charge_added_total * .12, 2)

        print("Total Charged (kwh): ", charge_added_total)
        print("Total Cost @ 12 cents/kwh: $", total_cost)

            
def filter_address(address): 
    print(address)
    return address == "Near 1226 Cheviot Ct"

def filterLocation(location): 
    coordinates = location.split(',')
    latitude = float(coordinates[0])
    longitude = float(coordinates[1])

    return round(latitude, 3) == 40.061 and round(longitude, 3) == -83.052

if __name__ == "__main__":
    main() 