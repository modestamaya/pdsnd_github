import time
import pandas as pd
import numpy as np



cities = { 'chicago': 'chicago.csv',
           'new york': 'new_york_city.csv',
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
    print('We have Chicago, Washington and New York City available for you to explore.')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    def city_choice():
        while True:
            try:
                city = input('\nPlease choose Chicago, Washington or New York: \n').lower()
                if city in cities:
                    print('\n{} is a great choice! Let\'s check it out! \n'.format(city.title()))
                    return city
            except:
                print('\nSorry, there is no {} in this list. \n'.format(city.title()))
    # TO DO: get user input for month (all, january, february, ... , june)
    def time_choice():
        while True:
            try:
                time_choice = int(float(input('\nIf you would like to see specific month enter it as a number from 1 to 6 or enter "0" for all: \n')))
                if (0 <= time_choice <= 6):
                    return time_choice
                    print('\nGood choice! Next, let\'s choose the day! \n')
                    break
                else:
                    print('\n{} does not represent a month, try numbers from 0-6.\n'.format(time_choice))
            except ValueError:
                print('\nThis is not a number. Please try again with numbers 0-6.\n')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    def day_choice():
        while True:
            try:
                day_choice = input('\nPlease specify the day of the week or 0 to apply no filter: \n').title()
                day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday', 'Saturday', 'Sunday', '0']
                if day_choice in day_list:
                    return day_choice
                    print('\nFollowing is data filltered according to {}: \n'.format(day_choice.title()))
                    break
                else:
                    print ('\n{} is not a day. \n'.format(day_choice))
            except ValueError:
                print('\nThis is not a day. Please try again naming the day of a week you would like to filter by. \n')

    print('-'*40)
    return city_choice(), time_choice(), day_choice()

def raw():
    df = load_data(city, month, day)
    raw_data = input('\nWould you like to see raw data? \nEnter yes or no: \n').lower()
    if raw_data in ('yes', 'y'):
        i = 0
        while True:
            print(df.iloc[i:i+5])
            i += 5
            more_data = input('\nWould you like to see more data? \nEnter yes or no:\n').lower()
            if more_data not in ('yes', 'y'):
                break



def load_data(city,month,day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - number of the month to filter by, or "0" to apply no month filter
        (str) day - number of the day of week to filter by, or "0" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(cities[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 0:
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != '0':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]
    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_week_day = df['day_of_week'].mode()[0]
    print('\nMost Popular Day of Week:', popular_week_day)

    # TO DO: display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('\nMost Popular Month:', popular_month)

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('\nMost Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)





def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_station = df['Start Station'].mode()[0]
    print('\nMost Popular Start Station:', popular_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('\nMost Popular End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()/60
    print('\nTotal Travel Time in Minutes:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()/60
    print('\nAverage Travel Time in Minutes:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender

    if  city in ('chicago', 'new york'):
        gender_counts = df['Gender'].value_counts()
        print( '\nUsers according to gender:\n',gender_counts)

        # TO DO: Display earliest, most recent, and most common year of birth

        youngest = df['Birth Year'].max()
        oldest = df ['Birth Year'].min()

        print('\nThe youngest user was born in {}.\n'.format(int(youngest)))
        print('\nThe oldest user was born in {}.\n'.format(int(oldest)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

city, month, day = get_filters()
df = load_data(city, month, day)

def main():
    while True:

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw()

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
