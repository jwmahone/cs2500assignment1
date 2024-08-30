#define functions

def most_annual_precip(dict):
    """ Given a dictionary with weather data, return the month that had
the most precipitation across all years and the average precip in that month
Arguments:
dict: the dictionary for a single region
Return:
a tuple of (month_number, avg precip for that month across all years)
for the month with highest precip
"""
def create_merged_csv(region1_dict,region2_dict, filename):
    """
Merge the data from both regions into a single .csv file
with format
date region1_tmin, region2_tmin, region1_tmax, region2_tmax,
region1_tavg, region2_tavg, region1_precip, region2_precip
Arguments: region1_dict: dictionary for first region
region2_dict: dictionary for second region
filename: name of csv file to be created
"""
def compare_monthly_avg_temps(region1_dict, region2_dict, month, filename):
    """Create a file of average monthly temperature (avg of avg) across all years
Comparing two regions
if day does not exist in both dictionaries, it is ommitted
make no assumption about order of data
Arguments: region1_dict: dictionary for first region
region2_dict: dictionary for second region
month: specified month to avg
filename: name of file to write monthly avgs to
"""
    with open(filename, "a") as file:
        file.write("Date Region1 Region2 Difference")
        
    
def month_int_to_name(num):
    """Convert month number to name
Arguments: month number (1-January, etc)
Return: Month name
"""
    # make sure num is an integer
    num = int(num)
    match num:
        case 1:
            return "January"
        case 2:
            return "February"
        case 3:
            return "March"
        case 4:
            return "April"
        case 5:
            return "May"
        case 6:
            return "June"
        case 7:
            return "July"
        case 8:
            return "August"
        case 9:
            return "September"
        case 10:
            return "October"
        case 11:
            return "November"
        case 12:
            return "December"
    
def load_file_into_dict(dict, filename, key):
    """
Given a CSV file that has year, data as first 2 items on a line
load them into provided dictionary
Arguments: dict - dictionary to be loaded
filename - file that contains data
key - key value in dictionary
"""
    with open(filename, "r") as file:
        #skip the first 5 lines of headers in each file to get to the data
        for i in range (5):
            next(file)
        for i in range(3):
            #separate lines at commas and set variables
            line  = next(file)
            fields = line.split(",")

            # Ensure there are at least two fields: date and data
            if len(fields) < 2:
                continue  # Skip lines that don't have enough data

            date = fields[0].strip()
            data = fields[1].strip()

            # Convert data to float if possible
            try:
                data = float(data)
            except ValueError:
                pass  # Keep data as string if it cannot be converted
                
            # Update the dictionary
            if date in dict:
                dict[date][key] = data
            else:
                dict[date] = {key: data}
    file.close()

me_precip_file = "maineCSVs/mePrecip.csv"
me_tmin_file = "maineCSVs/meMinTemp.csv"
me_tmax_file = "maineCSVs/meMaxTemp.csv"
me_tavg_file = "maineCSVs/meAveTemp.csv"
wa_precip_file = "washingtonCSVs/waPrecip.csv"
wa_tmin_file = "washingtonCSVs/waMinTemp.csv"
wa_tmax_file = "washingtonCSVs/waMaxTemp.csv"
wa_tavg_file = "washingtonCSVs/waAveTemp.csv"

def main():
    region1_dict = {}
    load_file_into_dict(region1_dict, me_precip_file, "PRECIP")
    load_file_into_dict(region1_dict, me_tmin_file, "TMIN")
    load_file_into_dict(region1_dict, me_tmax_file, "TMAX")
    load_file_into_dict(region1_dict, me_tavg_file, "TAVG")
    print('Region1 dict:')
    print(region1_dict)
    region2_dict = {}
    load_file_into_dict(region2_dict, wa_precip_file, "PRECIP")
    load_file_into_dict(region2_dict, wa_tmin_file, "TMIN")
    load_file_into_dict(region2_dict, wa_tmax_file, "TMAX")
    load_file_into_dict(region2_dict, wa_tavg_file, "TAVG")
    print('Region2 dict:')
    print(region2_dict)
    compare_monthly_avg_temps(region1_dict, region2_dict, '01',
    "Monthly data comp.txt")
    #create_merged_csv(region1_dict,region2_dict, "ME WA Weather Data.csv")
    #month, precip = most_annual_precip(region1_dict)
    #print(f'In Region1, historically {month_int_to_name(month)} ' +
    #f'has had the most precipation with avg of {precip:.2f} inches')
    #month, precip = most_annual_precip(region2_dict)
    #print(f'In Region2, historically {month_int_to_name(month)} ' +
    #f'has had the most precipation with avg of {precip:.2f} inches')
if __name__ == '__main__':
    main()