## Libraries: import all necessary packages and functions
import csv
import pprint
import datetime
import time
import re
from collections import Counter
import calendar
import pandas as pd
import numpy as np

## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')

    correcto = False
    selection = None
    while not correcto:
        # TODO: handle raw input and complete function
        if city.strip().lower() == 'chicago':
            correcto = True #this loop will only execute if the conditional is right.
            selection = chicago #the selection will be the return of this function.
        elif city.strip().lower() == 'new york':
            correcto = True #this loop will only execute if the conditional is right.
            selection = new_york_city
        elif city.strip().lower() == 'washington':
            correcto = True #this loop will only execute if the conditional is right.
            selection = washington
        else:
            city = input('\nSorry. Your selection is not a valid one. Please try again!\n'
                     'Would you like to see data for Chicago, New York, or Washington?\n')
    return selection

def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')
    # TODO: handle raw input and complete function

    correcto = False
    time_period_1 = None
    while not correcto:
        if time_period.strip().lower() == 'month':
            correcto = True
            time_period_1 = get_month()
        elif time_period.strip().lower() == 'day':
            correcto = True
            time_period_1 = get_day()
        elif time_period.strip().lower() == 'none':
            correcto = True
            time_period_1 = (datetime.datetime(2017,1,1,0,0,0),datetime.datetime(2017,6,30,0,0,0))
        else:
            time_period = input('\nSorry. Your selection is not a valid one. Please try again!\n'
                     'Would you like to filter data for month, day, or none?\n')

    return time_period_1

def ask_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    month = input('\nWhich month? January, February, March, April, May, or June?\n')
    # TODO: handle raw input and complete function

    correcto=False
    m = month.strip().lower()
    while not correcto:
        if m == 'january' or m == 'february' or m == 'march' or m == 'april' or m == 'may' or m == 'june' :
            correcto=True #this loop will only execute if the input is equal to the months available.
        else:
            month = input('\nSorry. Your selection is not a valid one. Please try again!\n'
                     'Please enter the correct month\n')
            m = month.strip().lower()
    return m

def get_month():
    '''Takes the function ask_month and provide the start time and end time of that month

    Args:
        none.
    Returns:
        TODO: fill out the filter: start time - end time
    '''
    month=ask_month()
    if month == 'january':
        correcto=True
        filter = (datetime.datetime(2017,1,1,0,0,0),datetime.datetime(2017,2,1,0,0,0))
    elif month == 'february':
        correcto=True
        filter = (datetime.datetime(2017,2,1,0,0,0),datetime.datetime(2017,3,1,0,0,0))
    elif month == 'march':
        correcto = True
        filter = (datetime.datetime(2017,3,1,0,0,0),datetime.datetime(2017,4,1,0,0,0))
    elif month == 'april':
        correcto = True
        filter = (datetime.datetime(2017,4,1,0,0,0),datetime.datetime(2017,5,1,0,0,0))
    elif month == 'may':
        correcto = True
        filter = (datetime.datetime(2017,5,1,0,0,0),datetime.datetime(2017,6,1,0,0,0))
    elif month == 'june':
        correcto = True
        filter = (datetime.datetime(2017,6,1,0,0,0),datetime.datetime(2017,7,1,0,0,0))
    return filter

def get_day():
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    days_of_month = {"january":31,"february":28,"march":31,"april":30,"may":31,"june":30}

    month=ask_month()
    days_of_this_month=days_of_month[month]
    '''With this, days_of_this_month will provide us the days that the month selected has'''
    m = None
    if month == "january":
        m = 1
    elif month == "february":
        m = 2
    elif month == "march":
        m = 3
    elif month == "april":
        m = 4
    elif month == "may":
        m = 5
    elif month == "june":
        m = 6

    day = input('\nWhich day? Please type your response as an integer.\n')
    # TODO: handle raw input and complete function

    '''If d=int(day) get error, it won't execute. It prevents from introducing strings or floats, instead of int.'''
    ''' Se pone pass para que no se produzca un error sintáctico por no haber ninguna instruccion en un bloque'''
    correcto = False
    filter = None
    while not correcto:
        try:
            d = int(day)

            if d >= 1 and d <= days_of_this_month:
                correcto = True
                filter = (datetime.datetime(2017,m,d,0,0,0),datetime.datetime(2017,m,d,23,59,59))
        except Exception as e:
            pass

        if not correcto:
            day = input('\nSorry. Your selection is not a valid one. Please try again!\n'
                     'Please enter the correct day\n')

    return filter

def popular_month(time_period,city):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular month for start time?
    '''
    # TODO: complete function
    df1 = pd.read_csv(city)
    start_time = df1['Start Time'].tolist()

    months = []
    for month in start_time:
        months.append(month[5:7])

    mode_month = Counter(months).most_common(1)
    extract_mode_month = mode_month[0]

    if extract_mode_month[0] == '01':
        pop_month = 'January'
    elif extract_mode_month[0] == '02':
        pop_month = 'February'
    elif extract_mode_month[0] == '03':
        pop_month = 'March'
    elif extract_mode_month[0] == '04':
        pop_month = 'April'
    elif extract_mode_month[0] == '05':
        pop_month = 'May'
    elif extract_mode_month[0] == '06':
        pop_month = 'June'
    else:
        pop_month = '-'

    print ('\nThe most popular month for start time is {}\n'.format(pop_month))

def popular_day(city, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    '''
    df3 = pd.read_csv(city)
    start_time = df3['Start Time'].tolist()

    start_period = time_period[0]
    end_period = time_period[1]

    days=[]
    for day in start_time:
        year = int(day[:4])
        month = int(day[5:7])
        d= int(day[8:10])
        hour = int (day[11:13])
        minute = int (day[14:16])
        second = int (day[17:20])
        duration_period=datetime.datetime(year,month,d,hour,minute,second)
        if duration_period > start_period and duration_period < end_period:
            days.append((datetime.datetime(year,month,d,hour,minute,second).weekday()))

    mode_days = Counter(days).most_common(1)

    Extract_mode_days = mode_days[0]

    if Extract_mode_days[0] == 0:
        popular_day = 'Monday'
    elif Extract_mode_days[0] == 1:
        popular_day = 'Tuesday'
    elif Extract_mode_days[0] == 2:
        popular_day = 'Wednesday'
    elif Extract_mode_days[0] == 3:
        popular_day = 'Thursday'
    elif Extract_mode_days[0] == 4:
        popular_day = 'Friday'
    elif Extract_mode_days[0] == 5:
        popular_day = 'Saturday'
    elif Extract_mode_days[0] == 6:
        popular_day = 'Sunday'

    print ('\nThe most popular day of week for start time is {}\n'.format(popular_day))

def popular_hour(city, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular hour of day for start time?
    '''
    # TODO: complete function

    df = pd.read_csv(city)
    start_time = df['Start Time'].tolist()

    start_period = time_period[0]
    end_period = time_period[1]

    hours = []
    for hour in start_time:
        year = int(hour[:4])
        month = int(hour[5:7])
        day= int(hour[8:10])
        h = int(hour[11:13])
        minute = int(hour[14:16])
        second = int(hour[17:20])
        duration_period = datetime.datetime(year,month,day,h,minute,second)

        if duration_period > start_period and duration_period < end_period:
            hours.append(h)


    mode_hour = Counter(hours).most_common(1)

    Extract_mode_hour = mode_hour[0]
    popular_hour = Extract_mode_hour[0]
    print ('\nThe most popular hour of day for start time is {}\n'.format(popular_hour))

def trip_duration(city,time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the total trip duration and average trip duration?
    '''

    df = pd.read_csv(city)
    start_time = df['Start Time'].tolist()
    duration = df['Trip Duration'].tolist()

    a = zip(start_time,duration)

    start_period = time_period[0]
    end_period = time_period[1]

    durations = []
    for hour in a:
        start_time_1 = hour[0]
        year = int(start_time_1[:4])
        month = int(start_time_1[5:7])
        day = int(start_time_1[8:10])
        h = int(start_time_1[11:13])
        minute = int(start_time_1[14:16])
        second = int(start_time_1[17:20])
        duration_period = datetime.datetime(year, month, day, h, minute, second)

        if duration_period > start_period and duration_period < end_period:
            durations.append(hour[1])

    sum_durations = sum(durations)
    mean = sum_durations/len(durations)

    print ('\nThe total trip duration is {} and the average trip duration is {}\n'.format(sum,mean))

def popular_stations(city, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular start station and most popular end station?
    '''
    # TODO: complete function

    df = pd.read_csv(city)
    start_time = df['Start Time'].tolist()
    start_station = df['Start Station'].tolist()
    end_station = df['End Station'].tolist()

    a = zip(start_time,start_station,end_station)

    start_period = time_period[0]
    end_period = time_period[1]

    start_stations = []
    end_stations = []
    for hour in a:
        start_time_1 = hour[0]
        year = int(start_time_1[:4])
        month = int(start_time_1[5:7])
        day = int(start_time_1[8:10])
        h = int(start_time_1[11:13])
        minute = int(start_time_1[14:16])
        second = int(start_time_1[17:20])
        duration_period = datetime.datetime(year,month,day,h,minute,second)

        if duration_period > start_period and duration_period < end_period:
            start_stations.append(hour[1])
            end_stations.append(hour[2])

    mode_start_stations = pd.Series(start_stations).mode()
    mode_end_stations = pd.Series(end_stations).mode()

    print ('\nThe most popular start station is {} and most popular end station is {}\n'.format(mode_start_stations[0],mode_end_stations[0]))

def popular_trip(city, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular trip?
    '''
    # TODO: complete function

    df = pd.read_csv(city)
    start_time = df['Start Time'].tolist()
    start_station = df['Start Station'].tolist()
    end_station = df['End Station'].tolist()

    start_period = time_period[0]
    end_period = time_period[1]

    trips = []
    for hour in zip(start_time,start_station,end_station):
        start_time_1 = hour[0]
        year = int(start_time_1[:4])
        month = int(start_time_1[5:7])
        day = int(start_time_1[8:10])
        h = int(start_time_1[11:13])
        minute = int(start_time_1[14:16])
        second = int(start_time_1[17:20])
        duration_period = datetime.datetime(year,month,day,h,minute,second)

        if duration_period>start_period and duration_period<end_period:
            b = hour[1]
            c = hour[2]
            trips.append("{} to {}".format(b,c))

    mode_trips = pd.Series(trips).mode()

    print ('\nThe most popular trip is {}\n'.format(mode_trips[0]))

def users(city, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of each user type?
    '''
    # TODO: complete function
    df = pd.read_csv(city)
    start_time = df['Start Time'].tolist()
    user_type = df['User Type'].tolist()

    start_period = time_period[0]
    end_period = time_period[1]

    users = []
    for hour in zip(start_time,user_type):
        start_time_1 = hour[0]
        year = int(start_time_1[:4])
        month = int(start_time_1[5:7])
        day = int(start_time_1[8:10])
        h = int(start_time_1[11:13])
        minute = int(start_time_1[14:16])
        second = int(start_time_1[17:20])
        duration_period = datetime.datetime(year,month,day,h,minute,second)

        if duration_period>start_period and duration_period<end_period:
            user = hour[1]
            users.append(user)

    dependent = users.count('Dependent')
    subscriber = users.count('Subscriber')
    customer = users.count('Customer')

    print ('\n"There are:\n\n{} - Users that are Dependent\n{} - Users that are Subscriber\n{} - Users that are Customer\n'.format(dependent,subscriber,customer))

def gender(city, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of gender?
    '''
    # TODO: complete function
    df = pd.read_csv(city)
    start_time = df['Start Time'].tolist()
    gender = df['Gender'].tolist()

    start_period = time_period[0]
    end_period = time_period[1]

    genders = []
    for hour in zip(start_time,gender):
        start_time_1 = hour[0]
        year = int(start_time_1[:4])
        month = int(start_time_1[5:7])
        day = int(start_time_1[8:10])
        h = int(start_time_1[11:13])
        minute = int(start_time_1[14:16])
        second = int(start_time_1[17:20])
        duration_period = datetime.datetime(year,month,day,h,minute,second)

        if duration_period > start_period and duration_period < end_period:
            gender_1 = hour[1]
            genders.append(gender_1)

    male = genders.count('Male')
    female = genders.count('Female')

    print('\nThere are:\n\n{} - Users that are male\n{} - Users that are female\n'.format(male,female,))

def birth_years(city, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?
    '''

    df = pd.read_csv(city)
    start_time = df['Start Time'].tolist()
    birth_year = df['Birth Year'].tolist()

    start_period = time_period[0]
    end_period = time_period[1]

    years = []
    for hour in zip(start_time,birth_year):
        start_time_1 = hour[0]
        year = int(start_time_1[:4])
        month = int(start_time_1[5:7])
        day = int(start_time_1[8:10])
        h = int(start_time_1[11:13])
        minute = int(start_time_1[14:16])
        second = int(start_time_1[17:20])
        duration_period = datetime.datetime(year,month,day,h,minute,second)

        if duration_period>start_period and duration_period<end_period:
            birth_year_1 = hour[1]
            years.append(birth_year_1)

    mode_years = pd.Series(years).mode()
    min_years = pd.Series(years).min()
    max_years = pd.Series(years).max()

    print('\nThe oldest user was born in {}, the younger user was born in {} and the more popular year of birth of the users is {}'.format(min_years,max_years,mode_years[0]))

def display_data(city,n,time_period):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.
start_time','end_time','trip_duration','start_station','end_station','user_type','gender','birth_year'
    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
    # TODO: handle raw input and complete function

    data = pd.read_csv(city)
    start_time = data['Start Time'].tolist()
    end_times = data['End Time'].tolist()
    trip_durations = data['Trip Duration'].tolist()
    origin = data['Start Station'].tolist()
    destination = data['End Station'].tolist()
    user_types = data['User Type'].tolist()

    if city == chicago or city == new_york_city:
        genders = data['Gender'].tolist()
        birth_year = data['Birth Year'].tolist()

    start_period = time_period[0]
    end_period = time_period[1]


    if display.lower() == "yes":
        displays = []

        if city == chicago or city == new_york_city:
            for z in zip(start_time,end_times,trip_durations,origin,destination,user_types,genders,birth_year):
                start_time_1 = z[0]
                year = int(start_time_1[:4])
                month = int(start_time_1[5:7])
                day = int(start_time_1[8:10])
                h = int(start_time_1[11:13])
                minute = int(start_time_1[14:16])
                second = int(start_time_1[17:20])
                duration_period = datetime.datetime(year,month,day,h,minute,second)

                if duration_period>start_period and duration_period<end_period:
                    a = z[0]
                    b = z[1]
                    c = z[2]
                    d = z[3]
                    e = z[4]
                    f = z[5]
                    g = z[6]
                    h = z[7]

                    displays.append([a,b,c,d,e,f,g,h])

        elif city == washington:
            for z in zip(start_time,end_times,trip_durations,origin,destination,user_types):
                start_time_1 = z[0]
                year = int(start_time_1[:4])
                month = int(start_time_1[5:7])
                day = int(start_time_1[8:10])
                h = int(start_time_1[11:13])
                minute = int(start_time_1[14:16])
                second = int(start_time_1[17:20])
                duration_period = datetime.datetime(year,month,day,h,minute,second)

                if duration_period>start_period and duration_period<end_period:
                    a = z[0]
                    b = z[1]
                    c = z[2]
                    d = z[3]
                    e = z[4]
                    f = z[5]

                    displays.append([a,b,c,d,e,f])

        for a,item in enumerate(displays):
            if a < n and a >= (n-5):
                print(item)


        display_data(city,n+5,time_period)


    elif display.lower()=='no':
    return


def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()

    # Filter by time period (month, day, none)
    time_period = get_time_period()

    print('\nCalculating the first statistic...')

    none = datetime.datetime(2017,1,1,0,0,0),datetime.datetime(2017,6,30,0,0,0)
    m1 = datetime.datetime(2017,1,1,0,0,0),datetime.datetime(2017,2,1,0,0,0)
    m2 = datetime.datetime(2017,2,1,0,0,0),datetime.datetime(2017,3,1,0,0,0)
    m3 = datetime.datetime(2017,3,1,0,0,0),datetime.datetime(2017,4,1,0,0,0)
    m4 = datetime.datetime(2017,4,1,0,0,0),datetime.datetime(2017,5,1,0,0,0)
    m5 = datetime.datetime(2017,5,1,0,0,0),datetime.datetime(2017,6,1,0,0,0)
    m6 = datetime.datetime(2017,6,1,0,0,0),datetime.datetime(2017,7,1,0,0,0)


    # What is the most popular month for start time?
    if time_period == none:
        start_time = time.time()
        pm = popular_month(time_period,city)

        #TODO: call popular_month function and print the results

        print("That took %s seconds." % (time.time() - start_time))
        print("\nCalculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?


    if time_period == none or time_period == m1 or time_period == m2 or time_period == m3 or time_period == m4 or time_period == m5 or time_period == m6:
        start_time = time.time()
        pd = popular_day(city, time_period)
        # TODO: call popular_day function and print the results

        print("That took %s seconds." % (time.time() - start_time))
        print("\nCalculating the next statistic...")

    start_time = time.time()
    ph = popular_hour(city, time_period)
    # What is the most popular hour of day for start time?
    # TODO: call popular_hour function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")

    start_time = time.time()
    tp = trip_duration(city, time_period)
    # What is the total trip duration and average trip duration?
    # TODO: call trip_duration function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()
    ps = popular_stations(city, time_period)
    # What is the most popular start station and most popular end station?
    # TODO: call popular_stations function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()
    pt = popular_trip(city, time_period)
    # What is the most popular trip?
    # TODO: call popular_trip function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()
    u = users(city, time_period)
    # What are the counts of each user type?
    # TODO: call users function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")

    if city == chicago or city == new_york_city:
        start_time = time.time()
        g = gender(city, time_period)
        # What are the counts of gender?
        # TODO: call gender function and print the results

        print("That took %s seconds." % (time.time() - start_time))

    if city == chicago or city == new_york_city:
        print("\nCalculating the next statistic...")
        start_time = time.time()
        by = birth_years(city, time_period)
        # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
        # most popular birth years?
        # TODO: call birth_years function and print the results

        print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to

    dd = display_data(city,5,time_period)

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()



