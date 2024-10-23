# **Weather Monitoring System with Email Alerts**

### **Introduction**
This project implements a real-time weather monitoring system that periodically fetches weather data from multiple cities using the OpenWeatherMap API. It monitors temperature thresholds and sends email alerts when the temperature exceeds a user-defined threshold. The system also visualizes the data and calculates weather statistics like average, minimum, and maximum temperatures for the cities being monitored.

---

### **System Features**
1. **Weather Data Fetching:**
   - Fetches weather data for six major cities: Delhi, Mumbai, Chennai, Bangalore, Kolkata, and Hyderabad.
   - Retrieves temperature and weather conditions in real-time using OpenWeatherMap API.

2. **Temperature Threshold Alerts:**
   - Compares the fetched temperatures to a user-configurable threshold.
   - Sends an automatic email alert to the specified recipient if the temperature exceeds the threshold.

3. **Data Aggregation and Summarization:**
   - Provides daily weather summaries, including the average, maximum, and minimum temperatures.
   - Identifies the dominant weather condition among the monitored cities.

4. **Visualization:**
   - Visualizes the temperature data for the cities using a bar plot.
   - Highlights temperatures exceeding the threshold with a red dashed line.

5. **Automated Repetition:**
   - Periodically updates weather data every two minutes for continuous monitoring.

---

### **Technologies Used**
- **Programming Language:** Python
- **Libraries:**
   - `requests`: For fetching weather data from OpenWeatherMap API.
   - `datetime`: For handling time-related data.
   - `smtplib`: For sending email notifications.
   - `matplotlib`: For visualizing the weather data.
   - `pandas`: For managing and analyzing data in tabular form.
   - `time`: For setting periodic intervals between data fetches.

---

### **Code Overview**

#### 1. **Global Configurations**
```python
TEMP_THRESHOLD = 40.0  # Temperature threshold for alerts in Celsius
EMAIL_ADDRESS = 'fproject383@gmail.com'  # Email address for sending alerts
EMAIL_PASSWORD = 'xzwggeysykmogcse'  # Password for the email account
TO_EMAIL = 'b21ec009@kitsw.ac.in'  # Recipient email address
```
These variables define the threshold for sending temperature alerts, email credentials, and recipient information.

#### 2. **Email Alert Function**
```python
def send_email_alert(city, temp_celsius):
    subject = f"Temperature Alert for {city}"
    body = f"ALERT: Temperature in {city} has exceeded {TEMP_THRESHOLD}°C."
    ...
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, TO_EMAIL, msg.as_string())
```
This function sends an email notification if the temperature in a city exceeds the configured threshold.

#### 3. **Fetching Weather Data**
```python
def fetch_weather_data_for_cities(api_key):
    cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
    for city in cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)
        ...
        check_temperature_alert(city, temp_celsius)
```
This function fetches weather data for a list of cities, processes the data, and checks for temperature thresholds.

#### 4. **Temperature Alert Trigger**
```python
def check_temperature_alert(city, temp_celsius):
    if temp_celsius > TEMP_THRESHOLD:
        send_email_alert(city, temp_celsius)
```
This function checks if the temperature of any city exceeds the threshold and sends an alert if necessary.

#### 5. **Data Visualization**
```python
def visualize_weather_data(df):
    plt.bar(df['City'], df['Temperature (°C)'], color=colors[:len(df)])
    plt.axhline(y=TEMP_THRESHOLD, color='r', linestyle='--', label='Threshold')
    ...
    plt.show()
```
This function visualizes the temperature data for different cities using a bar plot.

#### 6. **Main Execution Loop**
```python
while True:
    weather_df = fetch_weather_data_for_cities(api_key)
    visualize_weather_data(weather_df)
    time.sleep(120)  # Fetch new data every 2 minutes
```
This loop fetches new weather data, visualizes it, and repeats every two minutes to ensure real-time monitoring.

---

### **Execution Flow**
1. The system fetches weather data for multiple cities.
2. It checks whether the temperature in any city exceeds the threshold.
3. If the threshold is exceeded, an email alert is sent.
4. The weather data is stored in a DataFrame and visualized.
5. The system repeats this process every two minutes.

---

### **Conclusion**
This weather monitoring system provides a comprehensive approach to tracking weather conditions across multiple cities. The system offers real-time alerts, detailed visualizations, and flexible monitoring intervals. It is a reliable solution for users who need continuous updates and alerts based on specific temperature thresholds.

# Github Link
https://github.com/sainishitha27/Weather-Monitoring-System-API.git
