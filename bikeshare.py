import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
city_list = ['chicago', 'new york city', 'washington']
month_list = ['january', 'february', 'march','april','may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ,'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = str(input("Please entre the city from this list (chicago, new york city, washington), OR For exiting the app, please enter (exit) \n:").lower())
            if city == "exit":
                print("Good Bye...")                      
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
            month = str(input("Please entre the month Ex: (january, february, ... , june), OR For exiting the app, please enter (exit) \n:").lower())
            if month in month_list:
                print("month entered successfully...", month)
                break;
            elif month != "exit":
                print("Please Tray Again, the city should be selecteted from the Month of the year like (january, february, ... , june)")
            else:
                print("Good Bye...")
                return -1;    
        except ValueError:
            print("Provide a valide string value!...")
            continue

    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True :
        try:
            day = str(input("Please entre the day Ex: (monday, tuesday, ... sunday), OR For exiting the app, please enter (exit) \n:").lower())
            if day in day_list:
                print("day entered successfully...", day)
                break;
            elif month != "exit":
                print("Please Tray Again, the city should be selecteted from the day of the week like (monday, tuesday, ... sunday)")         
            else:
                print("Good Bye...") 
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
    common_month_txt = month_list[common_month-1]
    print('Most common month:', common_month_txt)

    # display the most common day of week
    common_day_of_week =  df['day_of_week'].mode()[0]
    print('Most common day of week:', common_day_of_week)

    # display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
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
    df['concat_traval_station'] = 'FROM---> ' + df['Start Station'] + ' TO---> ' + df['End Station']
    common_trip_station =  df['concat_traval_station'].mode()[0]
    print('The most most frequent combination of start station and end station trip is:', common_trip_station)

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

def Show_Data(df):
    """This function is for asking the user whether he wants to see 5 rows of data. 
    We will show the first 5 rows and after submitting and other question: " Do you want to see the next 5 rows of data?"
    until he say no or total row exided the limt of data """

    view_data = str(input('\nWould you like to view 5 rows of individual trip data? Enter (yes or no)\n').lower())
    start_loc = 0
    total_row = df.shape[0] - 1

    while (view_data == 'yes' and start_loc <= total_row):
        # i put here a double check to indicate to the user that he rich the limit of the data
        if(start_loc <= total_row):
            print(df.iloc[start_loc:start_loc + 5])
            start_loc += 5
            view_data = input("Do you wish to continue? (yes or no): ").lower()
        else:
            print("Data out of range! (exiding the limit of data)")
            break

def user_stats(df):
    """Displays statistics on bikeshare users."""
    try:
        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # Display counts of user types
        counts_of_user_types = df['User Type'].value_counts(dropna=False) 
        if counts_of_user_types.empty == False:  
            print('The total counts of user types is:\n', counts_of_user_types) 
        else:
            print('The total counts of user types is: No data to compute\n')
    
        
        # # Display counts of gender
        if ('Gender' in df.columns):
            counts_of_gender = df['Gender'].value_counts(dropna=False)
            if counts_of_gender.empty == False:
                print('\nThe total counts of gender:\n', counts_of_gender) 
            else:
                print('\nThe total counts of gender: No data to compute\n')
        else:
            print('\nThere is No Gender columns is this data set\n')

        # Display earliest, most recent, and most common year of birth
        if ('Birth Year' in df.columns):
            earliest_year_birth = df['Birth Year'].describe()[3]
            if earliest_year_birth != np.NaN:
                print('\nThe earliest year of birth is:', earliest_year_birth) 
            else:
                print('\nThe earliest year of birth is: No data to compute')

            most_recent  = df['Birth Year'].describe()[7] 
            if most_recent != np.NaN:
                print('The most recent year of birth is:', most_recent)
            else:
                print('The most recent year of birth is: No data to compute')

            most_common_year_of_birth = df['Birth Year'].mode()[0]
            if most_common_year_of_birth != np.NaN:
                print('The most common year of birth is:', most_common_year_of_birth) 
            else:
                print('The most common year of birth is: No data to compute')
        else:
            print('\nThere is No Birth Year columns is this data set\n')

    except Exception as e:
        print(str(e))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def main():
    while True:
        try :
            city, month, day = get_filters()

            df = load_data(city, month, day)
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

            restart = str(input('\nWould you like to go throuth showing data\n').lower())
            if restart.lower() != 'yes':
                print("Good Bye...")      
                break
            else:
                Show_Data(df)
                print("Good Bye...")      
                break
        
        except Exception  as e:
            break;
        


if __name__ == "__main__":
	main()
