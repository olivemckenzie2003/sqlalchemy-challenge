SQLALCHEMY CHALLENGE

In this challenge a basic climate analysis and data exploration of the climate database is carried out with the of use Python and SQLAlchemy. SQLAlchemy ORM is used for quering the database and Panda and Matplotlib are used for displaying the results.

hawaii.sqlite is the database.

All dependencies are imported at start of climate_starter.ipynb

climate_starter.ipynb contains the SQLAlchemy code used to:

   Create_engine() function to connect to your SQLite database 
   
      # create engine to hawaii.sqlite
       engine = create_engine("sqlite:///Resources/hawaii.sqlite")
       
   
  Display the c the database
    
      # reflect an existing database into a new model
      Base = automap_base()
        output: sqlalchemy.ext.automap.Base
        
      
  Display the tables into classes of the database
      
      # reflect the tables
      Base.prepare(engine, reflect=True)
        output:['measurement', 'station']
  
  
  Save references to the classes named station and measurement     
        
       # Save references to each table
       Measurement = Base.classes.measurement
       Station = Base.classes.station
   
  Link Python to the database by creating a SQLAlchemy session. 
  
      # Create our session (link) from Python to the DB
      session = Session(engine)
      
     

The rest of the code in climate_starter.ipynb is used to query the database 
 
Most recent date in the data set
   
Output: '2017-08-23


Date 12 months go from most recent date

Output: datetime.datetime(2016, 8, 23, 0, 0)





Data and precipitation scores

Output:







Query results as a Pandas DataFrame and set the index to the date column



Last 12 months of precipitation data and plot the results





Summary statistics for the precipitation data using a pandas dataframe

Output:







Exploratory Station Analysis


Output: The total number of stations in this data set is: 9


Most active stations using a pandas dataframe

Output:




Station id with the greatest number of observations

Output: 'USC00519281'


The most active station id from the previous query, calculate the lowest, highest, and average temperature.

Output: [(54.0, 71.66378066378067, 85.0)]


Last 12 months of temperature observation data for this station and plot the results as a histogram



Then session is closed

Code: session.close()

File app.py contains a Climate App using a Flask API to create your routes which are as follows:

Create root route Start at HomePage
@app.route("/")
def welcome():

All available API routes

f"/api/v1.0/precipitation<br/>"
f"/api/v1.0/stations<br/>"
f"/api/v1.0/tobs<br/>"
f"/api/v1.0/start<br/>"
f"/api/v1.0/start/end<br/>"

Call to the routes

Route that returns a JSON Precipitation analysis
@app.route("/api/v1.0/precipitation") 
def precipitation():

Route that returns a JSON list of stations from the database
@app.route("/api/v1.0/stations")
def station():



Route that returns JSON list of the temperatures observed for the last year for the most active station 
@app.route("/api/v1.0/tobs") 
def tobs():


@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def start_date_two(start=None,end=None):

.

Compile without debugging app.py file 


Host computer http address
Paste http://127.0.0.1:5000/ into chrome browser

 Output:    
    

Precipitation
Paste http://127.0.0.1:5000/api/v1.0/precipitation into chrome browser

 Output:



Stations
Paste http://127.0.0.1:5000/api/v1.0/stations into chrome browser
Output:





Start Date 
Paste http://127.0.0.1:5000/api/v1.0/2016-08-02 into chrome browser
Output:





Start Date and End date

Paste http://127.0.0.1:5000/api/v1.0/2016-08-02/2016-10-01 into chrome browser

Output:



