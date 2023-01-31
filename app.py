import numpy as np
import sqlalchemy
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify 

# Create connection to Hawaii.sqlite file
#################################################

# Create an engine for the Hawaii.sqlite database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect Database into ORM classes
# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

#references to the measurement and station tables in the database
Measurement = Base.classes.measurement
Station = Base.classes.station

# Initialize Flask
#################################################
app = Flask(__name__)

#Question 1.

# Create root route  (Start at HomePage)
@app.route("/")
def welcome():
    # Question 1. All available api routes
    return (
      
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
       
        
    )


# Question 2.
#  
# Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a 
# dictionary using date as the key and prcp as the value. Return the JSON representation of your dictionary.

@app.route("/api/v1.0/precipitation") 
def precipitation():
    # Make session (link) from Python to the DB
    session = Session(engine)

    #  Last 12 months of data
    one_year_ago=dt.date(2017,8,23)-dt.timedelta(days=365)
   
    #  Query to retrieve date and precipitation scores
    results = session.query(Measurement.prcp, Measurement.date).filter(Measurement.date>=one_year_ago).all()

    # Close session
    session.close()

    # Create a dictionary from the row use "date" as the key and "prcp" as the value.
    prcp_data=[]
    for date, prcp in results:
        prcp_dict={}
        prcp_dict["date"]=date
        prcp_dict["precipitation"]=prcp
        prcp_data.append(prcp_dict)

    #return JSON format of your new list 
    return jsonify(prcp_data) 



#Question 3.

#Return a JSON list of stations from the dataset.
# Create a route that returns a JSON list of stations from the database
@app.route("/api/v1.0/stations")
def station(): 

    session = Session(engine)

    """Return a list of stations from the database""" 
    station_results = session.query(Station.station,Station.id).all()

    session.close()  
    
    stations_values = []
    for station, id in station_results:
        stations_dict = {}
        stations_dict['station'] = station
        stations_dict['id'] = id
        stations_values.append(stations_dict)
    return jsonify (stations_values) 

#Question 4


# Create a route that queries the dates and temp observed for the most active station for the last year of data and returns a 
# JSON list of the temps observed for the last year

@app.route("/api/v1.0/tobs") 
def tobs():
    session = Session(engine)
    
    """Return a list of dates and temps observed for the most active station for the last year of data from the database""" 
    # Create query to find the last date in the database
    
    last_year_results = session.query(Measurement.date).\
        order_by(Measurement.date.desc()).first() 

    print(last_year_results)
    # last_year_date returns row ('2017-08-23',), use this to create a date time object to find start query date 
    
    # check to see if last year was correctly returned by creating dictionary to return last year value to browser in JSON format
    last_year_query_values = []
    for date in last_year_results:
        last_year_dict = {}
        last_year_dict["date"] = date
        last_year_query_values.append(last_year_dict) 
    print(last_year_query_values)
    # returns: [{'date': '2017-08-23'}]

    # Create query_start_date by finding the difference between date time object of "2017-08-23" - 365 days
    query_start_date = dt.date(2017, 8, 23)-dt.timedelta(days =365) 
    print(query_start_date) 
    # returns: 2016-08-23 

    # Create query to find most active station in the database 

    

    active_station= session.query(Measurement.station, func.count(Measurement.station)).\
        order_by(func.count(Measurement.station).desc()).\
        group_by(Measurement.station).first()
    most_active_station = active_station[0] 

    session.close() 
     # active_station returns: ('USC00519281', 2772), index to get the first position to isolate most active station number
    print(most_active_station)
    # returns: USC00519281  
    #'USC00519281'

    # Create a query to find dates and tobs for the most active station (USC00519281) within the last year (> 2016-08-23)

    dates_tobs_last_year_query_results = session.query(Measurement.date, Measurement.tobs, Measurement.station).\
        filter(Measurement.date > query_start_date).\
        filter(Measurement.station == most_active_station) 
    

    # Create a list of dates,tobs,and stations that will be appended with dictionary values for date, tobs, and station number queried above
    dates_tobs_last_year_query_values = []
    for date, tobs, station in dates_tobs_last_year_query_results:
        dates_tobs_dict = {}
        dates_tobs_dict["date"] = date
        dates_tobs_dict["tobs"] = tobs
        dates_tobs_dict["station"] = station
        dates_tobs_last_year_query_values.append(dates_tobs_dict)
        
    return jsonify(dates_tobs_last_year_query_values) 



#Question 5

#/api/v1.0/<start> and /api/v1.0/<start>/<end>
#Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

#Question 5A

#Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

@app.route("/api/v1.0/<start>")
# Define function, set "start" date 
def start_date(start):
    session = Session(engine) 

    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start date."""

    # Create query for minimum, average, and max tobs where query date is greater than or equal to the date 
    start_date_tobs_results = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).\
        filter(Measurement.date==start).all()
    
    session.close() 

    # Create a list of min,max,and average temps that will be appended with dictionary values for min, max, and avg tobs queried above
    start_date_tobs_values =[]
    for min, avg, max in start_date_tobs_results:
        start_date_tobs_dict = {}
        start_date_tobs_dict["min_temp_start_date"] = min
        start_date_tobs_dict["average_temp_start_date"] = avg
        start_date_tobs_dict["max_temp_start_date"] = max
        start_date_tobs_values.append(start_date_tobs_dict)
    
    return jsonify(start_date_tobs_values)



#Question 5B
@app.route("/api/v1.0/<start>")
# Define function, set "start" date 
def start_date_two(start):
    session = Session(engine) 

    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start date."""

    # Create query for minimum, average, and max tobs where query date is greater than or equal to the date 
    start_date_tobs_results = session.query(func.Tmin(Measurement.tobs),func.Tavg(Measurement.tobs),func.Tmax(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
    
    session.close() 

    # Create a list of min,max,and average temps that will be appended with dictionary values for Tmin, Tavg, and Tmax tobs queried above
    start_date_tobs_values_GTE =[]
    for Tmin, Tavg, Tmax in start_date_tobs_results:
        start_date_tobs_dict = {}
        start_date_tobs_dict["Tmin_temp_date_GTE"] = Tmin
        start_date_tobs_dict["Tavg_temp_date_GTE"] = Tavg
        start_date_tobs_dict["Tmax_temp_date_GTE"] = Tmax
        start_date_tobs_values_GTE.append(start_date_tobs_dict)
    
    return jsonify(start_date_tobs_values_GTE)


#Question 5C
#For a specified start date and end date, calculate Tmin, Tavg, and Tmax for the dates from the start date to the end date, inclusive.
app.route("/api/v1.0/<start>/<end>")


# Define function, set start and end dates 
def Start_end_date(start, end):
    session = Session(engine)

    """Return a list of min, avg and max tobs between start and end dates entered"""
    
    # Create query for minimum, average, and max tobs where query date is greater than or equal to the start date and less than or equal to end date 

    start_end_date_tobs_results = session.query(func.Tmin(Measurement.tobs), func.Tavg(Measurement.tobs), func.Tmax(Measurement.tobs)).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()

    session.close()


# Create a list of min,max,and average temps that will be appended with dictionary values for min, max, and avg tobs queried above
    start_end_tobs_date_values = []
    for Tmin, Tavg, Tmax in start_end_date_tobs_results:
        start_end_tobs_date_dict = {}
        start_end_tobs_date_dict["Tmin_temp_date_range"] = Tmin
        start_end_tobs_date_dict["Tavg_temp_date_range"] = Tavg
        start_end_tobs_date_dict["Tmax_temp_date_range"] = Tmax
        start_end_tobs_date_values.append(start_end_tobs_date_dict) 
    

    return jsonify(start_end_tobs_date_values)
   
if __name__ == '__main__':
    app.run(debug=True) 
        













