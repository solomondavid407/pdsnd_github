import time
import pandas as pd
import numpy as np

class color:
  
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'



CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze."""
    
    print( color.BOLD + 't\  Hello! Let\'s explore some US bikeshare data!'+ color.END )
   
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
       # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
                        
    print(color.UNDERLINE + '\t\t ***city of interest*** '+ color.END )  
    cities = ['chicago', 'new york city', 'washington'] # a python list of cities
    city = None
    city = input("Please enter your chosen city (chicago, new york city, washington): ").casefold()
    print('So you are interested in {} eeeh!'.format(city))
    while city not in cities: # execute this loop while the city variable does not have a value that exists in the cities list
        print("invalid input")
        print('Data for {} city is not yet available!'.format(city))
        city = input("you should choose from (chicago, new york city, washington): ").casefold() # capture user input
        
   
    # get user input for month (all, january, february, ... , june)
    
    print(color.UNDERLINE +'\t\t ***month of interest*** '+ color.END)     
    months= ['all','january','february','march','april','may','june'] # a python list of months
    month = None
    month = input('please enter either  all,january, february, ...,june ,or"all" to apply no month filter:').casefold()
    while month not in months: # execute this loop while the month variable does not have a value that exists in the months list
        month = input('please enter either  all,january, february, ...,june ,or"all" to apply no month filter:').casefold()
        print('invalid input')  # if the month variable does not take the all value
       
    
    print(color.UNDERLINE +'\t\t ***Day of interest*** '+ color.END)  
    days= ['all','sunday','monday','tuesday','wednesday' ,'thursday','friday','saturday']# a python list of days
    day = None
    day = input('please  enter name of the day to filter by, or "all" to apply no day filter:').casefold()# capture user input
    while day not in days: # execute this loop while the day variable does not have a value that exists in the dayslist
            day = input('please  enter name of the day to filter by, or "all" to apply no day filter:').casefold()# capture user input 
            print('invalid input') # if the day variable does not take the all value
                    

    print('The data processed is for {} in month of {} on day of {}' .format(city, month, day).title())
    print('-'*40)       
    print( city, month, day)
    print('-'*40)       
    return city,month,day

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
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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
    #filter by user type if applicable
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
   
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is ',common_month)
    # display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of week is' ,common_day_of_week)
    # display the most common start hour
    common_start_hour = df['Start Time'].dt.hour.mode()[0]
    print('The most common start hour is ',common_start_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Arg:(str)- Start station column and End station in the data frame
    Returns:(str) - The Most Frequent start station and End stations of Travel filtered by month , day and hour"""
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is ',common_start_station)
    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most commonly used End station is ',common_end_station)
    # display most frequent combination of start station and end station trip
    common_trip= df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('The most commonly travelled trip is ',common_trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    Total_Travel_Time = df['Trip Duration'].mean()* df['Trip Duration'].count()
    print('The Total time of travel  is ',Total_Travel_Time)
    # display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('The Mean time of travel  is ',Mean_Travel_Time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
   

def user_stats(df):
    """Displays statistics on bikeshare users. """
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    #User Type.reset_index()
    #df_value_counts.columns = ['User Type', 'counts']
    User_Type_counts = df['User Type'].value_counts()
    print('The number of user sorted by type is ',User_Type_counts)
    
    # filter by gender and birth year if applicable
    cities = ['chicago', 'new york city', 'washington']
    
    #for city in cities:
        #if ( city == 'chicago') or (city =='new york city'):
    Gender_counts = df['Gender'].count() # Display counts per gender
            # Display earliest, most recent, and most common year of birth
    Youngest_user = df['Birth Year'].max() 
    Oldest_User= df['Birth Year'].min()
    common_User_age = df['Birth Year'].mode() 
            
        #else:
    print('Gender and Birth year are not applicable to washington city')  #if city == washington:
              
    print('\nThe number of users sorted by gender  is:\n ',Gender_counts)   
    print('\nThe oldest user was born in:\n' ,Oldest_User) 
    print('\nThe youngest user was born in:\n ',Youngest_user) 
    print('\nThe common users of the bikeshare programm were born in:\n ',common_User_age) 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def Five_rows(df):
    """Displays five rows of data  on bikeshare users from dataframe. """
    
    print('\npreparing 5 rows of data...\n')
    see = input('\nWould you like to see 5 rows of data? Enter yes or no.\n')
    start_loc = 0
    analyse= True
    while analyse:

        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        see = input("Do you wish to continue?: ").lower()
        if see == "no":
            analyse = False
        #if see.casefold() == 'yes':
        #print(df.iloc[0:5] for i in range(len(df))
        #else:
           # print('Thank you for asking . I am exiting')
                 # break
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        Five_rows(df)
       
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.casefold() != 'yes':
            print('=\\='*96)
            break


if __name__ == "__main__":
        main()
