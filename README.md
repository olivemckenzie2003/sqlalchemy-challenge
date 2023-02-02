# sqlalchemy-challenge

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


  Date 12 months ago from most recent date
  Output: datetime.datetime(2016, 8, 23, 0, 0)

  Data and precipitation scores

![Screenshot (1185)](https://user-images.githubusercontent.com/115945473/216275343-b302f584-4bb6-475f-966d-4ad7aca05f88.png)

Query results as a Pandas DataFrame and set the index to the date column

![1](https://user-images.githubusercontent.com/115945473/216276140-f89685af-0112-49c8-ad4a-603ec93a0c41.jpg)

Last 12 months of precipitation data plotted results

![output](https://user-images.githubusercontent.com/115945473/216272921-2296a4f6-ca33-4978-8842-7af7b0b39196.png)


Summary statistics for the precipitation data using a pandas dataframe
Output:


![2](https://user-images.githubusercontent.com/115945473/216273814-5e439802-3078-4a42-8ff2-062fc7f69ded.jpg)



Exploratory Station Analysis


Output: The total number of stations in this data set is: 9

Most active stations using a pandas dataframe
Output:

![3](https://user-images.githubusercontent.com/115945473/216272910-5424abb3-7c67-4c0b-a140-c82a708b9fac.jpg)

Station id with the greatest number of observations

Output: 'USC00519281'


The most active station id from the previous query, calculate the lowest, highest, and average temperature.

Output: [(54.0, 71.66378066378067, 85.0)]


Last 12 months of temperature observation data for this station and plot the results as a histogram

![output2](https://user-images.githubusercontent.com/115945473/216272849-fc1d5bb3-7a78-463c-88a9-063264aae136.png)

Close session

code: session.close()






 
File app.py contains a Climate App using a Flask API to create routes which are as follows:

Create root route Start at HomePage
@app.route("/")
def welcome():

All available API routes

f"/api/v1.0/precipitation"

f"/api/v1.0/stations"

f"/api/v1.0/tobs"

f"/api/v1.0/start"

f"/api/v1.0/start/end"


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


Routes that returns JSON list of information for start date and start and end date

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def start_date_two(start=None,end=None):

All routes return a JSON format list based on query and after database is queried the session is closed

Compile without debugging app.py file 


Host computer http address
Paste http://127.0.0.1:5000/ into chrome browser

 Output:   
![Screenshot (1193)](https://user-images.githubusercontent.com/115945473/216206773-00ddb980-6e4b-4b88-9195-20a0420f547f.png)
   
Precipitation
Paste http://127.0.0.1:5000/api/v1.0/precipitation into chrome browser

 Output:
![Screenshot (1194)](https://user-images.githubusercontent.com/115945473/216206794-995a235b-88ee-4874-889d-c05f92a44bf2.png)
   
   
Stations
Paste http://127.0.0.1:5000/api/v1.0/stations into chrome browser
Output:

![Screenshot (1195)](https://user-images.githubusercontent.com/115945473/216206804-d3d8c2fd-d951-4820-b7d9-6f9c963cf25d.png)  
   
   
 Paste http://127.0.0.1:5000/api/v1.0/tobs into chrome browser
 Output:  
 ![Screenshot (1198)](https://user-images.githubusercontent.com/115945473/216272600-4b013c56-d912-49f7-b1fb-6113a18a3d4a.png)
   
Start Date 
Paste http://127.0.0.1:5000/api/v1.0/2016-08-02 into chrome browser
Output: ![Screenshot (1196)](https://user-images.githubusercontent.com/115945473/216206754-9fe46abf-bc3b-40cd-81a3-e2e2b21566fa.png) 

 
Start Date and End date
Paste http://127.0.0.1:5000/api/v1.0/2016-08-02/2016-10-01 into chrome browser
Output:
![Screenshot (1197)](https://user-images.githubusercontent.com/115945473/216206719-2161e04e-96c0-41fd-882a-949de993175a.png)



Resources Folder contains hawaii.sqlite, hawaii_measurements.csv and hawaii_stations.csv

   
   







