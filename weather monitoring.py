#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests

API_KEY = '9b8c1f6995fbaeaf7b936a17d2d25309'  # Make sure this is your actual key
CITY = 'Delhi'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

params = {
    'q': CITY,
    'appid': API_KEY
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error fetching data:", response.status_code, response.json())


# In[5]:


import requests
import time

API_KEY = '9b8c1f6995fbaeaf7b936a17d2d25309'
CITY = 'Delhi'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Parameters for API request
params = {
    'q': CITY,
    'appid': API_KEY
}

# Function to convert Kelvin to Celsius
def kelvin_to_celsius(kelvin_temp):
    return kelvin_temp - 273.15

# Fetch the weather data
response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()

    # Extract required fields
    main_condition = data['weather'][0]['main']  # e.g., Rain, Snow, Clear
    temp_kelvin = data['main']['temp']           # Temperature in Kelvin
    feels_like_kelvin = data['main']['feels_like'] # Feels-like temp in Kelvin
    timestamp = data['dt']                       # Time of data update (Unix timestamp)

    # Convert Kelvin to Celsius
    temp_celsius = kelvin_to_celsius(temp_kelvin)
    feels_like_celsius = kelvin_to_celsius(feels_like_kelvin)

    # Convert Unix timestamp to human-readable date and time
    readable_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))

    # Display the extracted information
    print(f"Weather Condition: {main_condition}")
    print(f"Temperature: {temp_celsius:.2f}°C")
    print(f"Feels Like: {feels_like_celsius:.2f}°C")
    print(f"Data Time: {readable_time}")

else:
    print(f"Error fetching data: {response.status_code}")


# In[6]:


import requests
from datetime import datetime

# Function to fetch weather data for multiple cities
def fetch_weather_data_for_cities(api_key):
    cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
    weather_data = {}

    for city in cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather_condition = data['weather'][0]['main']
            temp_kelvin = data['main']['temp']
            feels_like_kelvin = data['main']['feels_like']
            dt = data['dt']
            
            # Convert temperature from Kelvin to Celsius
            temp_celsius = round(temp_kelvin - 273.15, 2)
            feels_like_celsius = round(feels_like_kelvin - 273.15, 2)
            
            # Convert Unix timestamp to human-readable format
            data_time = datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S')
            
            # Store the data in a dictionary
            weather_data[city] = {
                'weather_condition': weather_condition,
                'temp_celsius': temp_celsius,
                'feels_like_celsius': feels_like_celsius,
                'data_time': data_time
            }
        else:
            print(f"Error fetching data for {city}: {response.status_code}")

    return weather_data

# Replace 'your_api_key_here' with your actual API key
api_key = '9b8c1f6995fbaeaf7b936a17d2d25309'
weather_data = fetch_weather_data_for_cities(api_key)

# Print the weather data for all cities
for city, data in weather_data.items():
    print(f"City: {city}")
    print(f"Weather Condition: {data['weather_condition']}")
    print(f"Temperature: {data['temp_celsius']}°C")
    print(f"Feels Like: {data['feels_like_celsius']}°C")
    print(f"Data Time: {data['data_time']}")
    print()  # Blank line for better readability


# In[7]:


import requests
from datetime import datetime
from collections import defaultdict

# Function to fetch weather data for multiple cities
def fetch_weather_data_for_cities(api_key):
    cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
    weather_data = defaultdict(list)  # To store data grouped by date

    for city in cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather_condition = data['weather'][0]['main']
            temp_kelvin = data['main']['temp']
            dt = data['dt']
            
            # Convert temperature from Kelvin to Celsius
            temp_celsius = round(temp_kelvin - 273.15, 2)
            data_time = datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d')

            # Store the data in a daily structure
            weather_data[data_time].append({
                'city': city,
                'weather_condition': weather_condition,
                'temp_celsius': temp_celsius
            })
        else:
            print(f"Error fetching data for {city}: {response.status_code}")

    return weather_data

# Function to calculate daily aggregates
def calculate_daily_summary(weather_data):
    daily_summaries = {}

    for date, records in weather_data.items():
        temperatures = [record['temp_celsius'] for record in records]
        conditions = [record['weather_condition'] for record in records]

        # Calculate aggregates
        avg_temp = sum(temperatures) / len(temperatures)
        max_temp = max(temperatures)
        min_temp = min(temperatures)

        # Dominant weather condition (the one that occurs most frequently)
        dominant_condition = max(set(conditions), key=conditions.count)

        # Store the summary
        daily_summaries[date] = {
            'average_temperature': round(avg_temp, 2),
            'maximum_temperature': max_temp,
            'minimum_temperature': min_temp,
            'dominant_weather_condition': dominant_condition
        }

    return daily_summaries

# Replace 'your_api_key_here' with your actual API key
api_key = '9b8c1f6995fbaeaf7b936a17d2d25309'
weather_data = fetch_weather_data_for_cities(api_key)
daily_summaries = calculate_daily_summary(weather_data)

# Print daily summaries
for date, summary in daily_summaries.items():
    print(f"Date: {date}")
    print(f"Average Temperature: {summary['average_temperature']}°C")
    print(f"Maximum Temperature: {summary['maximum_temperature']}°C")
    print(f"Minimum Temperature: {summary['minimum_temperature']}°C")
    print(f"Dominant Weather Condition: {summary['dominant_weather_condition']}")
    print()


# In[8]:


import requests
from datetime import datetime

# User-configurable threshold
TEMP_THRESHOLD = 35.0  # in degrees Celsius
consecutive_alert_count = 0

# Function to fetch weather data for multiple cities
def fetch_weather_data_for_cities(api_key):
    cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
    weather_data = {}

    for city in cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather_condition = data['weather'][0]['main']
            temp_kelvin = data['main']['temp']
            dt = data['dt']
            
            # Convert temperature from Kelvin to Celsius
            temp_celsius = round(temp_kelvin - 273.15, 2)
            data_time = datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S')
            
            # Store the data in a dictionary
            weather_data[city] = {
                'weather_condition': weather_condition,
                'temp_celsius': temp_celsius,
                'data_time': data_time
            }
            
            # Check if the temperature exceeds the threshold
            check_temperature_alert(city, temp_celsius)

        else:
            print(f"Error fetching data for {city}: {response.status_code}")

    return weather_data

# Function to check temperature against threshold and trigger alert
def check_temperature_alert(city, temp_celsius):
    global consecutive_alert_count

    if temp_celsius > TEMP_THRESHOLD:
        consecutive_alert_count += 1
        if consecutive_alert_count == 2:
            print(f"ALERT: Temperature in {city} has exceeded {TEMP_THRESHOLD}°C for two consecutive updates!")
    else:
        consecutive_alert_count = 0  # Reset counter if below threshold

# Replace 'your_api_key_here' with your actual API key
api_key = '9b8c1f6995fbaeaf7b936a17d2d25309'
weather_data = fetch_weather_data_for_cities(api_key)

# Print the weather data for all cities
for city, data in weather_data.items():
    print(f"City: {city}")
    print(f"Weather Condition: {data['weather_condition']}")
    print(f"Temperature: {data['temp_celsius']}°C")
    print(f"Data Time: {data['data_time']}")
    print()  # Blank line for better readability


# In[9]:


import requests
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

# User-configurable threshold
TEMP_THRESHOLD = 35.0  # in degrees Celsius
consecutive_alert_count = 0

# Email configuration
EMAIL_ADDRESS = 'fproject383@gmail.com'
EMAIL_PASSWORD = 'xzwggeysykmogcse'
TO_EMAIL = 'b21ec009@kitsw.ac.in'  # Replace with the recipient's email

# Function to send email notification
def send_email_alert(city, temp_celsius):
    subject = f"Temperature Alert for {city}"
    body = f"ALERT: Temperature in {city} has exceeded {TEMP_THRESHOLD}°C. Current Temperature: {temp_celsius}°C"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL

    # Send email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, TO_EMAIL, msg.as_string())
            print(f"Email alert sent for {city}!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to fetch weather data for multiple cities
def fetch_weather_data_for_cities(api_key):
    cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
    weather_data = {}

    for city in cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather_condition = data['weather'][0]['main']
            temp_kelvin = data['main']['temp']
            dt = data['dt']
            
            # Convert temperature from Kelvin to Celsius
            temp_celsius = round(temp_kelvin - 273.15, 2)
            data_time = datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S')
            
            # Store the data in a dictionary
            weather_data[city] = {
                'weather_condition': weather_condition,
                'temp_celsius': temp_celsius,
                'data_time': data_time
            }
            
            # Check if the temperature exceeds the threshold
            check_temperature_alert(city, temp_celsius)

        else:
            print(f"Error fetching data for {city}: {response.status_code}")

# Function to check temperature against threshold and trigger alert
def check_temperature_alert(city, temp_celsius):
    global consecutive_alert_count

    if temp_celsius > TEMP_THRESHOLD:
        consecutive_alert_count += 1
        if consecutive_alert_count == 2:
            send_email_alert(city, temp_celsius)  # Send email alert when threshold is breached
    else:
        consecutive_alert_count = 0  # Reset counter if below threshold

# Replace 'your_api_key_here' with your actual API key
api_key = '9b8c1f6995fbaeaf7b936a17d2d25309'
weather_data = fetch_weather_data_for_cities(api_key)

# Print the weather data for all cities
for city, data in weather_data.items():
    print(f"City: {city}")
    print(f"Weather Condition: {data['weather_condition']}")
    print(f"Temperature: {data['temp_celsius']}°C")
    print(f"Data Time: {data['data_time']}")
    print()  # Blank line for better readability


# In[11]:


import requests
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

# User-configurable threshold
TEMP_THRESHOLD = 35.0  # in degrees Celsius
consecutive_alert_count = 0

# Email configuration
EMAIL_ADDRESS = 'fproject383@gmail.com'
EMAIL_PASSWORD = 'xzwggeysykmogcse'
TO_EMAIL = 'b21ec009@kitsw.ac.in'  # Replace with the recipient's email

# Function to send email notification
def send_email_alert(city, temp_celsius):
    subject = f"Temperature Alert for {city}"
    body = f"ALERT: Temperature in {city} has exceeded {TEMP_THRESHOLD}°C. Current Temperature: {temp_celsius}°C"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL

    # Send email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, TO_EMAIL, msg.as_string())
            print(f"Email alert sent for {city}!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to fetch weather data for multiple cities
def fetch_weather_data_for_cities(api_key):
    cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
    weather_data = {}

    for city in cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather_condition = data['weather'][0]['main']
            temp_kelvin = data['main']['temp']
            dt = data['dt']
            
            # Convert temperature from Kelvin to Celsius
            temp_celsius = round(temp_kelvin - 273.15, 2)
            data_time = datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S')
            
            # Store the data in a dictionary
            weather_data[city] = {
                'weather_condition': weather_condition,
                'temp_celsius': temp_celsius,
                'data_time': data_time
            }

            print(f"{city}: Current Temperature: {temp_celsius}°C")  # Debug print
            
            # Check if the temperature exceeds the threshold
            check_temperature_alert(city, temp_celsius)

        else:
            print(f"Error fetching data for {city}: {response.status_code}")

    return weather_data

# Function to check temperature against threshold and trigger alert
def check_temperature_alert(city, temp_celsius):
    global consecutive_alert_count

    if temp_celsius > TEMP_THRESHOLD:
        consecutive_alert_count += 1
        if consecutive_alert_count == 2:
            send_email_alert(city, temp_celsius)  # Send email alert when threshold is breached
    else:
        consecutive_alert_count = 0  # Reset counter if below threshold

# Replace 'your_api_key_here' with your actual API key
api_key = '9b8c1f6995fbaeaf7b936a17d2d25309'  # Make sure this is your valid API key
weather_data = fetch_weather_data_for_cities(api_key)

# Print the weather data for all cities
for city, data in weather_data.items():
    print(f"City: {city}")
    print(f"Weather Condition: {data['weather_condition']}")
    print(f"Temperature: {data['temp_celsius']}°C")
    print(f"Data Time: {data['data_time']}")
    print()  # Blank line for better readability


# In[15]:


import requests
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

# User-configurable threshold
TEMP_THRESHOLD = 35.0  # in degrees Celsius
consecutive_alert_count = 0

# Email configuration
EMAIL_ADDRESS = 'fproject383@gmail.com'
EMAIL_PASSWORD = 'xzwggeysykmogcse'
TO_EMAIL = 'b21ec009@Kitsw.ac.in'  # Replace with the recipient's email

# Function to send email notification
def send_email_alert(city, temp_celsius):
    subject = f"Temperature Alert for {city}"
    body = f"ALERT: Temperature in {city} has exceeded {TEMP_THRESHOLD}°C. Current Temperature: {temp_celsius}°C"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL

    # Send email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, TO_EMAIL, msg.as_string())
            print(f"Email alert sent for {city}!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to fetch weather data for multiple cities
def fetch_weather_data_for_cities(api_key):
    cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
    weather_data = {}
    temperatures = []  # List to store temperatures for calculating aggregates
    conditions = {}  # Dictionary to count weather conditions

    for city in cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather_condition = data['weather'][0]['main']
            temp_kelvin = data['main']['temp']
            dt = data['dt']

            # Convert temperature from Kelvin to Celsius
            temp_celsius = round(temp_kelvin - 273.15, 2)
            data_time = datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S')

            # Store the data in a dictionary
            weather_data[city] = {
                'weather_condition': weather_condition,
                'temp_celsius': temp_celsius,
                'data_time': data_time
            }

            # Store temperature for averages
            temperatures.append(temp_celsius)

            # Count weather conditions for dominant weather condition
            if weather_condition in conditions:
                conditions[weather_condition] += 1
            else:
                conditions[weather_condition] = 1
            
            # Check if the temperature exceeds the threshold
            check_temperature_alert(city, temp_celsius)

        else:
            print(f"Error fetching data for {city}: {response.status_code}")

    # Calculate aggregates
    if temperatures:
        avg_temp = sum(temperatures) / len(temperatures)
        max_temp = max(temperatures)
        min_temp = min(temperatures)

        # Determine dominant weather condition
        dominant_condition = max(conditions, key=conditions.get)

        # Print the daily aggregates
        print("Daily Weather Summary:")
        print(f"Average Temperature: {avg_temp:.2f}°C")
        print(f"Maximum Temperature: {max_temp:.2f}°C")
        print(f"Minimum Temperature: {min_temp:.2f}°C")
        print(f"Dominant Weather Condition: {dominant_condition} (Most occurrences)")
        print()

    return weather_data

# Function to check temperature against threshold and trigger alert
def check_temperature_alert(city, temp_celsius):
    global consecutive_alert_count

    if temp_celsius > TEMP_THRESHOLD:
        consecutive_alert_count += 1
        if consecutive_alert_count == 2:
            send_email_alert(city, temp_celsius)  # Send email alert when threshold is breached
    else:
        consecutive_alert_count = 0  # Reset counter if below threshold

# Replace 'your_api_key_here' with your actual API key
api_key = '9b8c1f6995fbaeaf7b936a17d2d25309'
weather_data = fetch_weather_data_for_cities(api_key)

# Print the weather data for all cities
for city, data in weather_data.items():
    print(f"City: {city}")
    print(f"Weather Condition: {data['weather_condition']}")
    print(f"Temperature: {data['temp_celsius']}°C")
    print(f"Data Time: {data['data_time']}")
    print()  # Blank line for better readability


# In[17]:


import requests
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import matplotlib.pyplot as plt
import pandas as pd

# User-configurable threshold
TEMP_THRESHOLD = 35.0  # in degrees Celsius
consecutive_alert_count = 0

# Email configuration
EMAIL_ADDRESS = 'fproject383@gmail.com'
EMAIL_PASSWORD = 'xzwggeysykmogcse'
TO_EMAIL = 'b21ec009@kitsw.ac.in'  # Replace with the recipient's email

# Function to send email notification
def send_email_alert(city, temp_celsius):
    subject = f"Temperature Alert for {city}"
    body = f"ALERT: Temperature in {city} has exceeded {TEMP_THRESHOLD}°C. Current Temperature: {temp_celsius}°C"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL

    # Send email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, TO_EMAIL, msg.as_string())
            print(f"Email alert sent for {city}!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to fetch weather data for multiple cities
def fetch_weather_data_for_cities(api_key):
    cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
    weather_data = {}
    temperatures = []  # List to store temperatures for calculating aggregates
    conditions = {}  # Dictionary to count weather conditions

    for city in cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather_condition = data['weather'][0]['main']
            temp_kelvin = data['main']['temp']
            dt = data['dt']

            # Convert temperature from Kelvin to Celsius
            temp_celsius = round(temp_kelvin - 273.15, 2)
            data_time = datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S')

            # Store the data in a dictionary
            weather_data[city] = {
                'weather_condition': weather_condition,
                'temp_celsius': temp_celsius,
                'data_time': data_time
            }

            # Store temperature for averages
            temperatures.append(temp_celsius)

            # Count weather conditions for dominant weather condition
            if weather_condition in conditions:
                conditions[weather_condition] += 1
            else:
                conditions[weather_condition] = 1
            
            # Check if the temperature exceeds the threshold
            check_temperature_alert(city, temp_celsius)

        else:
            print(f"Error fetching data for {city}: {response.status_code}")

    # Calculate aggregates
    if temperatures:
        avg_temp = sum(temperatures) / len(temperatures)
        max_temp = max(temperatures)
        min_temp = min(temperatures)

        # Determine dominant weather condition
        dominant_condition = max(conditions, key=conditions.get)

        # Print the daily aggregates
        print("Daily Weather Summary:")
        print(f"Average Temperature: {avg_temp:.2f}°C")
        print(f"Maximum Temperature: {max_temp:.2f}°C")
        print(f"Minimum Temperature: {min_temp:.2f}°C")
        print(f"Dominant Weather Condition: {dominant_condition} (Most occurrences)")
        print()

    return weather_data

# Function to check temperature against threshold and trigger alert
def check_temperature_alert(city, temp_celsius):
    global consecutive_alert_count

    if temp_celsius > TEMP_THRESHOLD:
        consecutive_alert_count += 1
        if consecutive_alert_count == 2:
            send_email_alert(city, temp_celsius)  # Send email alert when threshold is breached
    else:
        consecutive_alert_count = 0  # Reset counter if below threshold

# Function to visualize daily weather data
def visualize_weather_data(weather_data):
    cities = list(weather_data.keys())
    temperatures = [data['temp_celsius'] for data in weather_data.values()]
    weather_conditions = [data['weather_condition'] for data in weather_data.values()]

    # Create a DataFrame for better manipulation
    df = pd.DataFrame({
        'City': cities,
        'Temperature (°C)': temperatures,
        'Weather Condition': weather_conditions
    })

    # Bar plot for temperatures
    plt.figure(figsize=(10, 5))
    plt.bar(df['City'], df['Temperature (°C)'], color='skyblue')
    plt.axhline(y=TEMP_THRESHOLD, color='r', linestyle='--', label='Threshold')
    plt.title('Current Temperatures in Different Cities')
    plt.xlabel('Cities')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.show()

# Replace 'your_api_key_here' with your actual API key
api_key = '9b8c1f6995fbaeaf7b936a17d2d25309'
weather_data = fetch_weather_data_for_cities(api_key)

# Print the weather data for all cities
for city, data in weather_data.items():
    print(f"City: {city}")
    print(f"Weather Condition: {data['weather_condition']}")
    print(f"Temperature: {data['temp_celsius']}°C")
    print(f"Data Time: {data['data_time']}")
    print()  # Blank line for better readability

# Visualize the weather data
visualize_weather_data(weather_data)


# In[20]:


import requests
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import matplotlib.pyplot as plt
import pandas as pd

# User-configurable threshold
TEMP_THRESHOLD = 30.0  # in degrees Celsius
consecutive_alert_count = 0

# Email configuration
EMAIL_ADDRESS = 'fproject383@gmail.com'
EMAIL_PASSWORD = 'xzwggeysykmogcse'
TO_EMAIL = 'b21ec009@kitsw.ac.in'  # Replace with the recipient's email

# Function to send email notification
def send_email_alert(city, temp_celsius):
    subject = f"Temperature Alert for {city}"
    body = f"ALERT: Temperature in {city} has exceeded {TEMP_THRESHOLD}°C. Current Temperature: {temp_celsius}°C"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL

    # Send email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, TO_EMAIL, msg.as_string())
            print(f"Email alert sent for {city}!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to fetch weather data for multiple cities
def fetch_weather_data_for_cities(api_key):
    cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
    weather_data = {}
    temperatures = []  # List to store temperatures for calculating aggregates
    conditions = {}  # Dictionary to count weather conditions

    for city in cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather_condition = data['weather'][0]['main']
            temp_kelvin = data['main']['temp']
            dt = data['dt']

            # Convert temperature from Kelvin to Celsius
            temp_celsius = round(temp_kelvin - 273.15, 2)
            data_time = datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S')

            # Store the data in a dictionary
            weather_data[city] = {
                'weather_condition': weather_condition,
                'temp_celsius': temp_celsius,
                'data_time': data_time
            }

            # Store temperature for averages
            temperatures.append(temp_celsius)

            # Count weather conditions for dominant weather condition
            if weather_condition in conditions:
                conditions[weather_condition] += 1
            else:
                conditions[weather_condition] = 1
            
            # Check if the temperature exceeds the threshold
            check_temperature_alert(city, temp_celsius)

        else:
            print(f"Error fetching data for {city}: {response.status_code}")

    # Calculate aggregates
    if temperatures:
        avg_temp = sum(temperatures) / len(temperatures)
        max_temp = max(temperatures)
        min_temp = min(temperatures)

        # Determine dominant weather condition
        dominant_condition = max(conditions, key=conditions.get)

        # Print the daily aggregates
        print("Daily Weather Summary:")
        print(f"Average Temperature: {avg_temp:.2f}°C")
        print(f"Maximum Temperature: {max_temp:.2f}°C")
        print(f"Minimum Temperature: {min_temp:.2f}°C")
        print(f"Dominant Weather Condition: {dominant_condition} (Most occurrences)")
        print()

    return weather_data

# Function to check temperature against threshold and trigger alert
def check_temperature_alert(city, temp_celsius):
    global consecutive_alert_count

    if temp_celsius > TEMP_THRESHOLD:
        consecutive_alert_count += 1
        if consecutive_alert_count == 2:
            send_email_alert(city, temp_celsius)  # Send email alert when threshold is breached
    else:
        consecutive_alert_count = 0  # Reset counter if below threshold

# Function to visualize daily weather data
def visualize_weather_data(weather_data):
    cities = list(weather_data.keys())
    temperatures = [data['temp_celsius'] for data in weather_data.values()]
    weather_conditions = [data['weather_condition'] for data in weather_data.values()]

    # Create a DataFrame for better manipulation
    df = pd.DataFrame({
        'City': cities,
        'Temperature (°C)': temperatures,
        'Weather Condition': weather_conditions
    })

    # Define a color palette for the cities
    colors = ['skyblue', 'lightgreen', 'salmon', 'gold', 'violet', 'lightcoral']  # You can add more colors

    # Create a bar plot for temperatures with different colors for each city
    plt.figure(figsize=(10, 5))
    plt.bar(df['City'], df['Temperature (°C)'], color=colors[:len(df)])  # Use the color list
    plt.axhline(y=TEMP_THRESHOLD, color='r', linestyle='--', label='Threshold')
    plt.title('Current Temperatures in Different Cities')
    plt.xlabel('Cities')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)  # Rotate city names for better readability
    plt.legend()
    plt.tight_layout()  # Adjust layout for better fit
    plt.show()

# Replace 'your_api_key_here' with your actual API key
api_key = '9b8c1f6995fbaeaf7b936a17d2d25309'
weather_data = fetch_weather_data_for_cities(api_key)

# Print the weather data for all cities
for city, data in weather_data.items():
    print(f"City: {city}")
    print(f"Weather Condition: {data['weather_condition']}")
    print(f"Temperature: {data['temp_celsius']}°C")
    print(f"Data Time: {data['data_time']}")
    print()  # Blank line for better readability

# Visualize the weather data
visualize_weather_data(weather_data)


# In[22]:


import requests
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import matplotlib.pyplot as plt
import pandas as pd

# User-configurable threshold
TEMP_THRESHOLD = 40.0  # in degrees Celsius

# Email configuration
EMAIL_ADDRESS = 'fproject383@gmail.com'
EMAIL_PASSWORD = 'xzwggeysykmogcse'
TO_EMAIL = 'b21ec009@kitsw.ac.in'  # Replace with the recipient's email

# Function to send email notification
def send_email_alert(city, temp_celsius):
    subject = f"Temperature Alert for {city}"
    body = f"ALERT: Temperature in {city} has exceeded {TEMP_THRESHOLD}°C. Current Temperature: {temp_celsius}°C"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL

    # Send email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, TO_EMAIL, msg.as_string())
            print(f"Email alert sent for {city}!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to fetch weather data for multiple cities and store in DataFrame
def fetch_weather_data_for_cities(api_key):
    cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
    data_list = []  # List to store weather data

    for city in cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather_condition = data['weather'][0]['main']
            temp_kelvin = data['main']['temp']
            dt = data['dt']

            # Convert temperature from Kelvin to Celsius
            temp_celsius = round(temp_kelvin - 273.15, 2)
            data_time = datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S')

            # Store the data in a list for DataFrame
            data_list.append({
                'City': city,
                'Weather Condition': weather_condition,
                'Temperature (°C)': temp_celsius,
                'Data Time': data_time
            })

            # Check if the temperature exceeds the threshold
            check_temperature_alert(city, temp_celsius)

        else:
            print(f"Error fetching data for {city}: {response.status_code}")

    # Create a DataFrame from the weather data
    df = pd.DataFrame(data_list)

    # Calculate aggregates (average, min, max temperatures)
    avg_temp = df['Temperature (°C)'].mean()
    max_temp = df['Temperature (°C)'].max()
    min_temp = df['Temperature (°C)'].min()

    # Find the dominant weather condition
    dominant_condition = df['Weather Condition'].mode()[0]

    # Print the daily aggregates
    print("Daily Weather Summary:")
    print(f"Average Temperature: {avg_temp:.2f}°C")
    print(f"Maximum Temperature: {max_temp:.2f}°C")
    print(f"Minimum Temperature: {min_temp:.2f}°C")
    print(f"Dominant Weather Condition: {dominant_condition}")
    print()

    return df

# Function to check temperature against threshold and trigger alert per city
def check_temperature_alert(city, temp_celsius):
    if temp_celsius > TEMP_THRESHOLD:
        send_email_alert(city, temp_celsius)  # Send email alert immediately when threshold is breached

# Function to visualize daily weather data
def visualize_weather_data(df):
    # Define a color palette for the cities
    colors = ['skyblue', 'lightgreen', 'salmon', 'gold', 'violet', 'lightcoral']  # Different colors for each city

    # Create a bar plot for temperatures with different colors for each city
    plt.figure(figsize=(10, 5))
    plt.bar(df['City'], df['Temperature (°C)'], color=colors[:len(df)])  # Use the color list
    plt.axhline(y=TEMP_THRESHOLD, color='r', linestyle='--', label='Threshold')
    plt.title('Current Temperatures in Different Cities')
    plt.xlabel('Cities')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)  # Rotate city names for better readability
    plt.legend()
    plt.tight_layout()  # Adjust layout for better fit
    plt.show()

# Replace 'your_api_key_here' with your actual API key
api_key = '9b8c1f6995fbaeaf7b936a17d2d25309'
weather_df = fetch_weather_data_for_cities(api_key)

# Print the DataFrame
print(weather_df)

# Visualize the weather data
visualize_weather_data(weather_df)


# In[ ]:




