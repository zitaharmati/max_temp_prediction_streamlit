import joblib
import streamlit as st
import pandas as pd

import sys
import os
from pathlib import Path
# # Adding the below path to avoid module not found error
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

# # Then perform import
from prediction_model.config import config 
from prediction_model.processing.data_handling import load_pipeline

temp_max_pred_pipeline = load_pipeline(config.MODEL_NAME)

def prediction(cloud_cover_10day,cloud_cover_9day,  cloud_cover_8day, cloud_cover_7day,cloud_cover_6day,cloud_cover_5day, cloud_cover_4day,
               cloud_cover_3day, cloud_cover_2day, cloud_cover_1day,
               humidity_10day, humidity_9day, humidity_8day,humidity_7day,humidity_6day, humidity_5day, humidity_4day,humidity_3day,
               humidity_2day,humidity_1day,
               pressure_10day,pressure_9day,pressure_8day, pressure_7day,pressure_6day,pressure_5day,pressure_4day, pressure_3day,
               pressure_2day,pressure_1day,
               precipitation_10day, precipitation_9day, precipitation_8day,precipitation_7day,
               precipitation_6day,precipitation_5day, precipitation_4day,precipitation_3day,precipitation_2day,precipitation_1day,
               sunshine_10day,sunshine_9day,sunshine_8day,sunshine_7day,sunshine_6day,sunshine_5day,sunshine_4day, sunshine_3day,
                sunshine_2day,sunshine_1day,
               temp_min10day, temp_min9day, temp_min8day,temp_min7day, temp_min6day,temp_min5day,temp_min4day,
               temp_min3day, temp_min2day,temp_min1day,
               temp_max10day, temp_max9day,temp_max8day,temp_max7day,temp_max6day,temp_max5day,temp_max4day,
              temp_max3day,temp_max2day,temp_max1day,
                temp_mean10day,temp_mean9day,temp_mean8day,temp_mean7day,temp_mean6day,temp_mean5day,temp_mean4day,
                temp_mean3day,temp_mean2day, temp_mean1day,
                BBQW_10day, BBQW_9day,BBQW_8day, BBQW_7day,BBQW_6day,BBQW_5day,BBQW_4day,
                BBQW_3day, BBQW_2day,BBQW_1day, MONTH, WEEK,DAY):
     
    data={'cloud_cover--10_day': cloud_cover_10day,
    'cloud_cover--9_day':cloud_cover_9day,
    'cloud_cover--8_day':cloud_cover_8day,
    'cloud_cover--7_day':cloud_cover_7day,
    'cloud_cover--6_day':cloud_cover_6day,
    'cloud_cover--5_day':cloud_cover_5day,
    'cloud_cover--4_day':cloud_cover_4day,
    'cloud_cover--3_day':cloud_cover_3day,
    'cloud_cover--2_day':cloud_cover_2day,
    'cloud_cover--1_day':cloud_cover_1day,
    'humidity--10_day':humidity_10day,
    'humidity--9_day':humidity_9day,
    'humidity--8_day':humidity_8day,
    'humidity--7_day':humidity_7day,
    'humidity--6_day':humidity_6day,
    'humidity--5_day':humidity_5day,
    'humidity--4_day':humidity_4day,
    'humidity--3_day':humidity_3day,
    'humidity--2_day':humidity_2day,
    'humidity--1_day':humidity_1day,
    'pressure--10_day': pressure_10day,
    'pressure--9_day': pressure_9day,
    'pressure--8_day': pressure_8day,
    'pressure--7_day': pressure_7day,
    'pressure--6_day': pressure_6day,
    'pressure--5_day': pressure_5day,
    'pressure--4_day': pressure_4day,
    'pressure--3_day': pressure_3day,
    'pressure--2_day': pressure_2day,
    'pressure--1_day': pressure_1day,
    'precipitation--10_day': precipitation_10day,
    'precipitation--9_day': precipitation_9day,
    'precipitation--8_day': precipitation_8day,
    'precipitation--7_day': precipitation_7day,
    'precipitation--6_day': precipitation_6day,
    'precipitation--5_day': precipitation_5day,
    'precipitation--4_day': precipitation_4day,
    'precipitation--3_day': precipitation_3day,
    'precipitation--2_day': precipitation_2day,
    'precipitation--1_day': precipitation_1day,
    'sunshine--10_day': sunshine_10day,
    'sunshine--9_day': sunshine_9day,
    'sunshine--8_day': sunshine_8day,
    'sunshine--7_day': sunshine_7day,
    'sunshine--6_day': sunshine_6day,
    'sunshine--5_day': sunshine_5day,
    'sunshine--4_day': sunshine_4day,
    'sunshine--3_day': sunshine_3day,
    'sunshine--2_day': sunshine_2day,
    'sunshine--1_day': sunshine_1day,
    'temp_min--10_day':temp_min10day,
    'temp_min--9_day':temp_min9day,
    'temp_min--8_day':temp_min8day,
    'temp_min--7_day':temp_min7day,
    'temp_min--6_day':temp_min6day,
    'temp_min--5_day':temp_min5day,
    'temp_min--4_day':temp_min4day,
    'temp_min--3_day':temp_min3day,
    'temp_min--2_day':temp_min2day,
    'temp_min--1_day':temp_min1day,
    'temp_max--10_day':temp_max10day,
    'temp_max--9_day':temp_max9day,
    'temp_max--8_day':temp_max8day,
    'temp_max--7_day':temp_max7day,
    'temp_max--6_day':temp_max6day,
    'temp_max--5_day':temp_max5day,
    'temp_max--4_day':temp_max4day,
    'temp_max--3_day':temp_max3day,
    'temp_max--2_day':temp_max2day,
    'temp_max--1_day':temp_max1day,
    'temp_mean--10_day':temp_mean10day,
    'temp_mean--9_day':temp_mean9day,
    'temp_mean--8_day':temp_mean8day,
    'temp_mean--7_day':temp_mean7day,
    'temp_mean--6_day':temp_mean6day,
    'temp_mean--5_day':temp_mean5day,
    'temp_mean--4_day':temp_mean4day,
    'temp_mean--3_day':temp_mean3day,
    'temp_mean--2_day':temp_mean2day,
    'temp_mean--1_day':temp_mean1day,
    'BBQ_weather--10_day': BBQW_10day,
    'BBQ_weather--9_day': BBQW_9day,
    'BBQ_weather--8_day': BBQW_8day,
    'BBQ_weather--7_day': BBQW_7day,
    'BBQ_weather--6_day': BBQW_6day,
    'BBQ_weather--5_day': BBQW_5day,
    'BBQ_weather--4_day': BBQW_4day,
    'BBQ_weather--3_day': BBQW_3day,
    'BBQ_weather--2_day': BBQW_2day,
    'BBQ_weather--1_day': BBQW_1day,
    'DATE MONTH':MONTH,
    'DATE WEEK':WEEK,
    'DATE DAY':DAY}
    df = pd.DataFrame(data, index=[0])
    prediction = temp_max_pred_pipeline.predict(df)
    print(print(prediction))

    return prediction   
    
def main():
    # Front end
    st.title("Welcome to maximum temperature prediction in Budapest")
    st.header("Please enter the data of the previous 10 days")
    
    cloud_cover_10day = st.number_input("Cloud cover 10 days before - number between 0 and 8")
    cloud_cover_9day= st.number_input("Cloud cover 9 days before - number between 0 and 8")
    cloud_cover_8day= st.number_input("Cloud cover 8 days before - number between 0 and 8") 
    cloud_cover_7day = st.number_input("Cloud cover 7 days before - number between 0 and 8")
    cloud_cover_6day = st.number_input("Cloud cover 6 days before - number between 0 and 8")
    cloud_cover_5day = st.number_input("Cloud cover 5 days before - number between 0 and 8") 
    cloud_cover_4day = st.number_input("Cloud cover 4 days before - number between 0 and 8")
    cloud_cover_3day = st.number_input("Cloud cover 3 days before - number between 0 and 8") 
    cloud_cover_2day = st.number_input("Cloud cover 2 days before - number between 0 and 8") 
    cloud_cover_1day = st.number_input("Cloud cover 1 days before - number between 0 and 8")
    humidity_10day = st.number_input("Humidity percentage 10 days before - number between 0 and 1") 
    humidity_9day = st.number_input("Humidity percentage 9 days before - number between 0 and 1") 
    humidity_8day = st.number_input("Humidity percentage 8 days before - number between 0 and 1")
    humidity_7day = st.number_input("Humidity percentage 7 days before - number between 0 and 1")
    humidity_6day = st.number_input("Humidity percentage 6 days before - number between 0 and 1") 
    humidity_5day = st.number_input("Humidity percentage 5 days before - number between 0 and 1") 
    humidity_4day = st.number_input("Humidity percentage 4 days before - number between 0 and 1")
    humidity_3day = st.number_input("Humidity percentage 3 days before - number between 0 and 1")
    humidity_2day = st.number_input("Humidity percentage 2 days before - number between 0 and 1")
    humidity_1day = st.number_input("Humidity percentage 1 days before - number between 0 and 1")
    pressure_10day = st.number_input("Air pressure in Bar 10 days before")
    pressure_9day = st.number_input("Air pressure in Bar 9 days before")
    pressure_8day = st.number_input("Air pressure in Bar 8 days before") 
    pressure_7day = st.number_input("Air pressure in Bar 7 days before")
    pressure_6day = st.number_input("Air pressure in Bar 6 days before")
    pressure_5day = st.number_input("Air pressure in Bar 5 days before")
    pressure_4day = st.number_input("Air pressure in Bar 4 days before") 
    pressure_3day = st.number_input("Air pressure in Bar 3 days before")
    pressure_2day = st.number_input("Air pressure in Bar 2 days before")
    pressure_1day = st.number_input("Air pressure in Bar 1 days before")
    precipitation_10day = st.number_input("Precipitation in mm 10 days before") 
    precipitation_9day = st.number_input("Precipitation in mm 9 days before") 
    precipitation_8day = st.number_input("Precipitation in mm 8 days before")
    precipitation_7day = st.number_input("Precipitation in mm 7 days before")
    precipitation_6day = st.number_input("Precipitation in mm 6 days before")
    precipitation_5day = st.number_input("Precipitation in mm 5 days before") 
    precipitation_4day = st.number_input("Precipitation in mm 4 days before")
    precipitation_3day = st.number_input("Precipitation in mm 3 days before")
    precipitation_2day = st.number_input("Precipitation in mm 2 days before")
    precipitation_1day = st.number_input("Precipitation in mm 1 days before")
    sunshine_10day = st.number_input("Sunshine in hour 10 days before")
    sunshine_9day = st.number_input("Sunshine in hour 9 days before")
    sunshine_8day = st.number_input("Sunshine in hour 8 days before")
    sunshine_7day = st.number_input("Sunshine in hour 7 days before")
    sunshine_6day = st.number_input("Sunshine in hour 6 days before")
    sunshine_5day = st.number_input("Sunshine in hour 5 days before")
    sunshine_4day = st.number_input("Sunshine in hour 4 days before") 
    sunshine_3day = st.number_input("Sunshine in hour 3 days before")
    sunshine_2day = st.number_input("Sunshine in hour 2 days before")
    sunshine_1day = st.number_input("Sunshine in hour 1 days before")
    temp_min10day = st.number_input("Minimum temperature in Celsius 10 days before") 
    temp_min9day = st.number_input("Minimum temperature in Celsius 9 days before")
    temp_min8day = st.number_input("Minimum temperature in Celsius 8 days before")
    temp_min7day = st.number_input("Minimum temperature in Celsius 7 days before") 
    temp_min6day = st.number_input("Minimum temperature in Celsius 6 days before")
    temp_min5day = st.number_input("Minimum temperature in Celsius 5 days before")
    temp_min4day = st.number_input("Minimum temperature in Celsius 4 days before")
    temp_min3day = st.number_input("Minimum temperature in Celsius 3 days before") 
    temp_min2day = st.number_input("Minimum temperature in Celsius 2 days before")
    temp_min1day = st.number_input("Minimum temperature in Celsius 1 days before")
    temp_max10day = st.number_input("Maximum temperature in Celsius 10 days before") 
    temp_max9day = st.number_input("Maximum temperature in Celsius 9 days before")
    temp_max8day = st.number_input("Maximum temperature in Celsius 8 days before")
    temp_max7day = st.number_input("Maximum temperature in Celsius 7 days before") 
    temp_max6day = st.number_input("Maximum temperature in Celsius 6 days before")
    temp_max5day = st.number_input("Maximum temperature in Celsius 5 days before")
    temp_max4day = st.number_input("Maximum temperature in Celsius 4 days before")
    temp_max3day = st.number_input("Maximum temperature in Celsius 3 days before")
    temp_max2day = st.number_input("Maximum temperature in Celsius 2 days before")
    temp_max1day = st.number_input("Maximum temperature in Celsius 1 days before")
    temp_mean10day = st.number_input("Mean temperature in Celsius 10 days before")
    temp_mean9day = st.number_input("Mean temperature in Celsius 9 days before")
    temp_mean8day = st.number_input("Mean temperature in Celsius 8 days before")
    temp_mean7day = st.number_input("Mean temperature in Celsius 7 days before")
    temp_mean6day = st.number_input("Mean temperature in Celsius 6 days before")
    temp_mean5day = st.number_input("Mean temperature in Celsius 5 days before")
    temp_mean4day = st.number_input("Mean temperature in Celsius 4 days before")
    temp_mean3day = st.number_input("Mean temperature in Celsius 3 days before")
    temp_mean2day = st.number_input("Mean temperature in Celsius 2 days before") 
    temp_mean1day = st.number_input("Mean temperature in Celsius 1 days before")
    BBQW_10day = st.selectbox("Was the weather nice 10 day before? Select True if there were no precipitation and maximum tempreature was above 16 Celsius :", ("True", "False"))
    BBQW_10day_bool = BBQW_10day == "True"
    BBQW_9day = st.selectbox("Was the weather nice 9 day before? Select True if there were no precipitation and maximum tempreature was above 16 Celsius :", ("True", "False"))
    BBQW_9day_bool = BBQW_9day == "True"
    BBQW_8day = st.selectbox("Was the weather nice 8 day before? Select True if there were no precipitation and maximum tempreature was above 16 Celsius :", ("True", "False")) 
    BBQW_8day_bool = BBQW_8day == "True"
    BBQW_7day = st.selectbox("Was the weather nice 7 day before? Select True if there were no precipitation and maximum tempreature was above 16 Celsius :", ("True", "False"))
    BBQW_7day_bool = BBQW_7day == "True"
    BBQW_6day = st.selectbox("Was the weather nice 6 day before? Select True if there were no precipitation and maximum tempreature was above 16 Celsius :", ("True", "False"))
    BBQW_6day_bool = BBQW_6day == "True"
    BBQW_5day = st.selectbox("Was the weather nice 5 day before? Select True if there were no precipitation and maximum tempreature was above 16 Celsius :", ("True", "False"))
    BBQW_5day_bool = BBQW_5day == "True"
    BBQW_4day = st.selectbox("Was the weather nice 4 day before? Select True if there were no precipitation and maximum tempreature was above 16 Celsius :", ("True", "False"))
    BBQW_4day_bool = BBQW_4day == "True"
    BBQW_3day = st.selectbox("Was the weather nice 3 day before? Select True if there were no precipitation and maximum tempreature was above 16 Celsius :", ("True", "False")) 
    BBQW_3day_bool = BBQW_3day == "True"
    BBQW_2day = st.selectbox("Was the weather nice 2 day before? Select True if there were no precipitation and maximum tempreature was above 16 Celsius :", ("True", "False"))
    BBQW_2day_bool = BBQW_2day == "True"
    BBQW_1day = st.selectbox("Was the weather nice 1 day before? Select True if there were no precipitation and maximum tempreature was above 16 Celsius :", ("True", "False")) 
    BBQW_1day_bool = BBQW_1day == "True"
    MONTH = st.number_input("Month in number for predicted day"), 
    WEEK = st.number_input("Week of the year in number for predicted day"),
    DAY = st.number_input("Day of the month in number for predicted day")

    if st.button("Predict"):
        result = prediction(cloud_cover_10day,cloud_cover_9day,  cloud_cover_8day, cloud_cover_7day,cloud_cover_6day,cloud_cover_5day, cloud_cover_4day,
               cloud_cover_3day, cloud_cover_2day, cloud_cover_1day,
               humidity_10day, humidity_9day, humidity_8day,humidity_7day,humidity_6day, humidity_5day, humidity_4day,humidity_3day,
               humidity_2day,humidity_1day,
               pressure_10day,pressure_9day,pressure_8day, pressure_7day,pressure_6day,pressure_5day,pressure_4day, pressure_3day,
               pressure_2day,pressure_1day,
               precipitation_10day, precipitation_9day, precipitation_8day,precipitation_7day,
               precipitation_6day,precipitation_5day, precipitation_4day,precipitation_3day,precipitation_2day,precipitation_1day,
               sunshine_10day,sunshine_9day,sunshine_8day,sunshine_7day,sunshine_6day,sunshine_5day,sunshine_4day, sunshine_3day,
                sunshine_2day,sunshine_1day,
               temp_min10day, temp_min9day, temp_min8day,temp_min7day, temp_min6day,temp_min5day,temp_min4day,
               temp_min3day, temp_min2day,temp_min1day,
               temp_max10day, temp_max9day,temp_max8day,temp_max7day,temp_max6day,temp_max5day,temp_max4day,
              temp_max3day,temp_max2day,temp_max1day,
                temp_mean10day,temp_mean9day,temp_mean8day,temp_mean7day,temp_mean6day,temp_mean5day,temp_mean4day,
                temp_mean3day,temp_mean2day, temp_mean1day,
                BBQW_10day_bool, BBQW_9day_bool, BBQW_8day_bool, BBQW_7day_bool, BBQW_6day_bool, BBQW_5day_bool,
                BBQW_4day_bool, BBQW_3day_bool, BBQW_2day_bool, BBQW_1day_bool, MONTH, WEEK,DAY)
        
        st.info(f"Predicted maximum temperature for {MONTH}.{DAY}: {result}")
        

if __name__ == "__main__":
    main()
