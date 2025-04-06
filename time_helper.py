from datetime import datetime, timedelta

#if the parameter for range is negative we are subtracting dates 

def find_date_range(type, range):
    type_lowered = type.lower()
    current_date = datetime.now()
    result = None
    date_math = None
    
    if (type_lowered == 'days'):
        date_math = current_date + timedelta(days=range)
        print(f"from: {current_date} \nto: {date_math}")
        result = compare_dates(current_date, date_math)
        
        
    elif (type_lowered == 'weeks'):
        
        date_math = current_date + timedelta(weeks=range)
        print(f"from: {current_date} \nto: {result}")
        result = compare_dates(current_date, date_math)
        
        
    elif (type_lowered == 'years'):
        # converted_weeks = year_to_week(range)
        # date_math = current_date + timedelta(weeks=converted_weeks)
        
        # print(f"from: {current_date} \nto: {result}")
        # result = compare_dates(current_date, date_math)
        # print(result)
        return None
        
    
        
    
    return result


def compare_dates(date1, date2):
    print(f"Date1: {date1} \nDate2: {date2}")
    return [f"{date1.year}-{date1.month}-{date1.day}", f"{date2.year}-{date2.month}-{date2.day}"] if date2 > date1 else [f"{date2.year}-{date2.month}-{date2.day}", f"{date1.year}-{date1.month}-{date1.day}"] 


def year_to_week(years):
    return 52 * years

find_date_range("Day", 7)