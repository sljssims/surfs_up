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
# 6. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
