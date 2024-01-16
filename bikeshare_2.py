import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

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
        city = input("Primero, vamos a seleccionar una ciudad. ¿Qué ciudad te interesa? "+ 
                     "in: Chicago, New York City o Washington?\n\n")
        
        city = city.lower()

        if city not in ('chicago', 'new york city', 'washington'):
            print("Por favor, ingresa una ciudad valida.")
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("¿Qué mes te gustaría analizar para " + city.title() + 
                      "? Puedes elegir entre January, February, March, April " +
                      "May and June o escribir all si no deseas elegir un mes.\n\n")
        
        month = month.lower()

        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("Por favor, ingresar un mes válido")
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("¡Excelente elección! Ahora vamos a elegir un día de la semana." +
                    "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday " +
                     "Sunday o ingresa all si no quieres especificar un dia.\n\n")
        
        day = day.lower()

        if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 
                       'saturday', 'sunday', 'all'):
            print("Por favor, ingresa un día válido")
            continue
        else:
            break

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
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Weekday'] = df['Start Time'].dt.weekday
    df['Hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month = MONTH_DATA.index(month)

        df = df[df['Month'] == month]
    
    if day != 'all':
        day = DAY_DATA.index(day)
        df = df[df['Weekday'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['Month'].mode()[0]
    print("El mes más común es: " + MONTH_DATA[common_month].title())
    
    # display the most common day of week
    common_day = df['Weekday'].mode()[0]
    print("El día más común de la semana es: " + DAY_DATA[common_day].title())

    # display the most common start hour
    common_start_hour = df['Hour'].mode()[0]
    print("La hora más común es: " + str(common_start_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("La estación de inicio más común es: " + common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("La estación de fin más común es: " + common_end_station)

    # display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("La combinación de estaciones más frecuente es: " + str(frequent_combination.split("||")))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("El tiempo total de viaje es: " + str(total_travel_time))
    
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("El tiempo real de viaje es: " + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("La cantidad por tipos de usuarios es la siguiente: \n\n" + user_types.to_string())

    if city == 'chicago' or city == 'new_york_city':
    # Display counts of gender
        gender = df['Gender'].value_counts()
        print("La cantidad de usuarios por género es la siguiente: \n" + gender.to_string())

    # Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]
        print("El año de nacimiento más antiguo en la data obtenida es: {:n}\n".format(earliest_birth))
        print("El año de nacimiento más reciente de la data obtenida es: {:n}\n" .format(most_recent_birth))
        print("El año de nacimiento más común de la data obtenida es: {:n}\n" .format(most_common_birth))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
