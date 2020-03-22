import pandas as pd
import numpy as np
import datetime
from datetime import date, timedelta, datetime
import getpass
import random
import sys


location2 = r'C:\Users\achie\Github\COVID-19\csse_covid_19_data\csse_covid_19_time_series'

url = location2 +r'\time_series_19-covid-Confirmed.csv'
Cases = pd.read_csv(url, header=0, index_col=0)

