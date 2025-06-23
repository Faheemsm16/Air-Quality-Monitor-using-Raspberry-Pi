# Air Quality Monitor using Raspberry Pi

## Overview

This project implements a **real-time air quality monitoring system** using a **Raspberry Pi**. It measures:
- Gas concentration (via GPIO-connected sensor)
- Temperature
- Humidity  
The results are displayed on both the **terminal** and a **16x2 LCD screen**.

> Ideal for indoor air quality tracking, educational labs, and Raspberry Pi learning!

## Hardware Components

| Component        | Function                          |
|------------------|-----------------------------------|
| Raspberry Pi     | Core processing unit              |
| DHT22 Sensor     | Measures temperature & humidity   |
| MQ-series Gas Sensor | Detects gas presence          |
| 16x2 LCD (I2C or Parallel) | Displays IP & timestamp |
| Breadboard & Wires | Circuit connections             |

## Features

- Real-time data logging via terminal output
- Humidity & temperature monitoring using **Adafruit_DHT**
- Gas presence alert via GPIO pin input
- LCD shows current **timestamp** and **IP address**
- Modular code for sensor and LCD handling

## Code Structure

### 1. `Air_Quality_Monitor.py`
- **Reads data** from:
  - DHT22 (temperature & humidity)
  - GPIO-connected gas sensor (digital HIGH/LOW)
- Displays status messages:
  ```plaintext
  GAS SENSOR
  GAS DETECTED

  HUMIDITY SENSOR
  TEMP=29.4*C HUM=50.1%
  ```

### 2. `LCD_Setup.py`
- Displays:
  - **Current Date & Time**
  - **Device's Local IP Address**
- Refreshes every 2 seconds

## Sample Output

### Terminal Output:
```
AIR QUALITY MONITOR
RASPBERRY PI

GAS SENSOR
COOL ENVIRONMENT

HUMIDITY SENSOR
TEMP=29.1*C HUM=49.7%
```

### LCD Output:
```
Jun 23 12:01:15
IP 192.168.1.12
```

## How to Run

### Setup
1. Connect DHT22 to GPIO4
2. Connect Gas sensor output to GPIO17
3. Connect 16x2 LCD to GPIO pins (per wiring in `LCD_Setup.py`)

### Install Required Libraries
```bash
sudo apt-get update
sudo apt-get install python3-pip
pip3 install adafruit-circuitpython-charlcd Adafruit_DHT
```

### Run the Programs
```
# Terminal monitoring
python3 Air_Quality_Monitor.py

# LCD display
python3 LCD_Setup.py
```

## Troubleshooting

- Ensure GPIO pin numbers match your wiring
- For LCD: make sure you’re using **correct GPIO pinout**
- If `Adafruit_DHT.read_retry()` returns `None`, check power/data pins and pull-up resistor

## Future Enhancements

- Add **PM2.5 sensor** for particulate monitoring
- Log data to **CSV** or **cloud dashboard**
- Alert via **email/SMS** if gas is detected
- Add **buzzer or LED** for audible/visual warnings

## Author
**Mohammed Farhan S M**  
 `faheemproject20@gmail.com`

## 📄 License
This project is licensed under the [MIT License](LICENSE).
