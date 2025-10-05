import os
import requests

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from dotenv import load_dotenv


load_dotenv()

endpoint = os.getenv("FORECAST_ENDPOINT")
response = requests.get(endpoint)
json = response.json()

WEEK_METADATA = json['forecast']['forecastday']


def plot(df, columns, labels, ylabel, title):
    plt.figure(figsize=(10, 5))
    x = df['time']

    lines = tuple(zip(columns, labels))
    for col, label in lines:
        y = df[col]
        plt.plot(x, y, label=label)

    if len(lines) > 1:        
        for idx, value in enumerate(x[df['above_threshold']]):
            line_arguments = {'x': value, 'color': 'red', 'linestyle': '--', 'alpha': 0.7, 'zorder': 0}
            if idx == 0:
                plt.axvline(**line_arguments, label='Alert')
            plt.axvline(**line_arguments)
    else:        
        plt.scatter(x[df['above_threshold']], y[df['above_threshold']], color='red', zorder=5, label='Alert')


    plt.title(title)
    plt.xlabel("Time (hour)")
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    plt.legend()
    plt.tight_layout()
    plt.show()