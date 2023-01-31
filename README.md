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
  
  
 api/v1.0/precipitation
/api/v1.0/stations
/api/v1.0/tobs
/api/v1.0/start
/api/v1.0/start/end















Remember to close your session at the end of your notebook.

