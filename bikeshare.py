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
            if city == "exit":
                print("Goud Bye...")                      
                return -1;   
            elif city in city_list:
                print("City entered successfully...", city)
                break;
            elif city != "exit":
                print("Please Tray Again, the city should be selecteted from this list (chicago, new york city, washington)")   
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
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
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
    common_month =  df['month'].mode()[0]
    print('Most common month:', common_month)

    # display the most common day of week
    common_day_of_week =  df['day_of_week'].mode()[0]
    print('Most common day of week:', common_day_of_week)

    # display the most common start hour

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most common hour (from 0 to 23)
    common_hour =  df['hour'].mode()[0]
        
    print('Most common Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station =  df['Start Station'].mode()[0]
    print('The most common Start Station is:', common_start_station)


    # display most commonly used end station
    common_end_station =  df['End Station'].mode()[0]
    print('The most common End Station is:', common_end_station)

    # display most frequent combination of start station and end station trip
    tupple =  df['End Station','station trip'].mode()[0]
    print('The most ccombination of start station and end station trip is:', tupple)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is:', total_travel_time)

    # display mean travel time
    avg = df['Trip Duration'].describe()[1]
    print('The Average trip duration is:', avg)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    cout_user_Subscriber = df['User Type'].value_counts()[0] 
    print('The total count for Subscribers:', cout_user_Subscriber) 

    cout_user_Customers = df['User Type'].value_counts()[1] 
    print('The total count for Customers:', cout_user_Customers)

    # Display counts of gender
    cout_gender_Male = df['Gender'].value_counts()[0] 
    print('The total count for User gender Male:', cout_gender_Male) 

    cout_gender_Female = df['Gender'].value_counts()[1] 
    print('The total count for User gender Femele:', cout_gender_Female)

    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        
        #if get_filters() == -1 :
         #   return 
        try :
            city, month, day = get_filters()

            df = load_data(city, month, day)

            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break
        except Exception  as e:
            print(str(e))
            break;
        


if __name__ == "__main__":
	main()
