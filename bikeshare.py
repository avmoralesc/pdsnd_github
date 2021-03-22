import time
import pandas as pd
import numpy as np
  
CITY_DATA = { 'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv',
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

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #cities = ['Chicago', 'New York City', 'Washington']
    while True:
        city = input('Which of these cities do you want to explore : Chicago, New York City or Washington?').lower()
        if city in CITY_DATA:
            break
    # get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input('What month do you want: january, february, march, april, may, june?').lower()
        if month in months:
            break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    while True:
        day = input('What day do you want: sunday,monday,tuesday,wednesday,thursday,friday,saturday?').lower()
        if day in days:
            break
    
    print('-'*40)
    return city, month, day

    city, month, day = get_filters()
    
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

    # Create a dataframe with the chosen city
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('The common month is:',common_month)

    # display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    common_day_of_week = df['day_of_week'].mode()[0]
    print('The common day of week is:',common_day_of_week)

    # display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The common hour is:',common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('The most commonly used start station is:', common_start)

    # display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('The most commonly used start station is:', common_end)

    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_combination = df['combination'].mode()[0]
    print('The most frequent combination of start station and end station trip:',common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print('Total travel time is:', total_travel)

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('Mean travel time is:', mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The counts of user type are:',user_types)

    # Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print('The counts of gender is:',gender)
    else:
            print("This city has not information about gender.")

    # Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        earliest = df['Birth_Year'].min()
        print('The earliest year of birth is:', earliest)
        recent = df['Birth_Year'].max()
        print('The recent year of birth is:', recent)
        common_birth = df['Birth Year'].mode()[0]
        print('The common year of birth is:', common_birth)
    else:
        print("This city has not information about birth year.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #Asking the user about the raw data
        count1=0 
        count2=5
        while True:
          rw = input("Would you like to see the raw data? Please Enter Yes or Not?")
          rw=rw.lower() 
          if rw == "yes":
            print(df.iloc[count1:count2])
            count1+=5
            count2+=5            
          else:
            break
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
