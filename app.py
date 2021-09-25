##################################
#Set Up the Flask Weather App
##################################
import datetime as dt
import numpy as np
import pandas as pd
# Get dependencies needed for SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
# Add the code to import the dependcies from Flask
from flask import Flask, jsonify

###############################
# Set Up the Database
###############################
# Access the SQLite database -- engine = create_engine()
engine = create_engine("sqlite:///hawaii.sqlite")
# Reflect the database into our classes 
Base = automap_base()
# Reflect the tables
Base.prepare()
# Reflect the database
Base.prepare(engine, reflect=True)
# Save references to each table
measurement = Base.classes.measurement
Station = Base.classes.station
# Create a session link
session = Session(engine)

###############################
# Set Up Flask
###############################
app = Flask(__name__)

###############################
# Create the Welcome Route
###############################
# Define the welcome route (Version 1)
@app.route("/")
# Add routing information
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')


##########################
# Precipitation Route
##########################
# Define the Precipitation Route
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(measurement.date, measurement.prcp).\
     filter(measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

##########################
# Stations Route
##########################
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

##########################
# Temperature Route
##########################
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(measurement.tobs).\
        filter(measurement.station == 'USC00519281').\
        filter(measurement.date >= prev_year).all()
    temps = list(np.ravel(results))    
    return jsonify(temps=temps)

###############################
# Summary Statistics Route
##############################
#Start and End Date
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)]
    if not end:
        results = session.query(*sel).\
            filter(measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)
    
    results = session.query(*sel).\
        filter(measurement.date >= start).\
        filter(measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

############################
# 6. Define main behavior
############################
if __name__ == "__main__":
    app.run(debug=True)


