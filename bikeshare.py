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
    city_list = ['chicago', 'new york city', 'washington']
    month_list = ['January', 'February', 'March','April','May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    day_list = ['Monday', 'Tuesday', 'Wednesday ', 'Thursday', 'Friday', 'Saturday' ,'Sunday']

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = str(input("Please entre the city from this list (chicago, new york city, washington), OR For exiting the app, please enter (exit) \n:"))
            if city in city_list:
                print("City entered successfully...", city)
                break;
            elif city != "exit":
                print("Please Tray Again, the city should be selecteted from this list (chicago, new york city, washington)")   
            else:
                print("Goud Bye...")                      
                return -1;   
        except ValueError:
            print("Provide a valide string value!...")
            continue
    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = str(input("Please entre the month Ex: (January, February, March, ...), OR For exiting the app, please enter (exit) \n:"))
            if month in month_list:
                print("month entered successfully...", month)
                break;
            elif month != "exit":
                print("Please Tray Again, the city should be selecteted from the Month of the year like (January, February, March, ...)")
            else:
                print("Goud Bye...")
                return -1;    
        except ValueError:
            print("Provide a valide string value!...")
            continue

    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True :
        try:
            day = str(input("Please entre the day Ex: (Monday, Tuesday, Wednesday, ...), OR For exiting the app, please enter (exit) \n:"))
            if day in day_list:
                print("day entered successfully...", day)
                break;
            elif month != "exit":
                print("Please Tray Again, the city should be selecteted from the day of the week like (Monday, Tuesday, Wednesday, ...)")         
            else:
                print("Goud Bye...") 
                return -1;  
        except ValueError:
            print("Provide a valide string value!...")
            continue

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
  
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    # Notice that i'm using day_name() instead of weekday_name !
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month_list = ['January', 'February', 'March','April','May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        month = month_list.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        
        if get_filters() == -1 :
            return 
        city, month, day = get_filters()
      
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
