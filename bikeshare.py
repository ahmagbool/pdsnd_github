# Explore US Bikeshare Data Project

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    check = 0
    while check == 0:
        city = input('Select a city (Chicago, New York City, Washington): ').lower()
        if city == 'chicago' or city == 'new york city' or city == 'washington':
            check = 1
        else:
            print('Sorry, you have enterd invalid city name')


    # TO DO: get user input for month (all, january, february, ... , june)
    check = 0
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'all']
    while check == 0:
        month = input('Select a month (all, January, February, March, ... ): ').lower()
        if month in months:
            check = 1
        else:
            print('Sorry, you have enterd invalid month name')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    check = 0
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','all']
    while check == 0:
        day = input('Select a day (all, Sunday, Monday, ...): ').lower()
        if day in days:
            check = 1
        else:
            print('Sorry, you have enterd invalid day name')


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    count_common_month = df['month'].value_counts().max()
    print('The most common month is: ', common_month, ' count: ', count_common_month)


    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    count_common_day = df['day_of_week'].value_counts().max()
    print('The most common day of the week is: ', common_day, ' count: ', count_common_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    count_common_hour = df['hour'].value_counts().max()
    print('The most common start hour is: ', common_hour ,' count: ', count_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    count_start_station = df['Start Station'].value_counts().max()
    print('The most common start station is: ', common_start_station, ' count: ', count_start_station)


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    count_end_station = df['Start Station'].value_counts().max()
    print('The most common end station is: ', common_end_station, ' count: ', count_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['start_end_station'] = '\nStart station: ' + df['Start Station'] + '\nEnd station:' + df['End Station']
    common_start_end_station = df['start_end_station'].mode()[0]
    count_start_end_station = df['start_end_station'].value_counts().max()
    print('The most most frequent combination of start station and end station trip is: ', common_start_end_station, ' count: ', count_start_end_station)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    total_dur = (df['End Time'] - df['Start Time']).sum()
    total_days = total_dur.days
    total_hours, remainder = divmod(total_dur.seconds, 3600)
    total_minutes, total_seconds = divmod(remainder, 60)

    print('The total travel time is ',total_days, ' days ,',total_hours, ' hours ,',total_minutes, ' minutes ,', total_seconds, ' seconds.')



    # TO DO: display mean travel time
    mean_travel = (df['End Time'] - df['Start Time']).mean()
    mean_days = mean_travel.days
    mean_hours, remainder = divmod(mean_travel.seconds, 3600)
    mean_minutes, mean_seconds = divmod(remainder, 60)

    print('The total travel time is ',mean_days, ' days ,',mean_hours, ' hours ,',mean_minutes, ' minutes ,', mean_seconds, ' seconds.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types:')
    user_types = df['User Type'].value_counts()
    print(user_types)


    # TO DO: Display counts of gender
    if 'Gender' in df.keys():
        print('Counts of user genders:')
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print('No gender information.')



    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.keys():
       earliest_birth = df['Birth Year'].min()
       print('The earliest year of birth is: ', earliest_birth)

       most_recent_birth = df['Birth Year'].max()
       print('The most recent year of birth is: ', most_recent_birth)

       most_common_birth = df['Birth Year'].mode()[0]
       count_common_birth = df['Birth Year'].value_counts().max()
       print('The most common year of birth is: ', most_common_birth, ' Count: ', count_common_birth)

    else:
       print('No date of birth information.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# The main code is here

def main():
    pd.set_option('display.max_columns', None)
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        if df.empty:
            print('No records for the selected period')
        else:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

        check = 0
        i = 0
        while check == 0:
             raw_data = input('\nWould you like to see the raw data? Enter yes or no.\n').lower()
             if raw_data == 'no':
                 check = 1
             elif raw_data == 'yes':
                 if i+5 < len(df):
                    print(df.iloc[i:i+5, :-4])
                    i = i+5
                 else:
                    print(df.iloc[i:, :-4])
                    check = 1
             else:
                 print('Sorry, you have enterd invalid option.')





        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
