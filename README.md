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


  Date 12 months go from most recent date
  Output: datetime.datetime(2016, 8, 23, 0, 0)

  Data and precipitation scores
  
  ![output](https://user-images.githubusercontent.com/115945473/216205690-22186801-b0f8-4821-9d6d-566524faf7c6.png)
  ![output2](https://user-images.githubusercontent.com/115945473/216205694-22b00a49-ad5b-48d5-931e-a79848ab08c8.png)
  
  
 api/v1.0/precipitation
/api/v1.0/stations
/api/v1.0/tobs
/api/v1.0/start
/api/v1.0/start/end






![Screenshot (1193)](https://user-images.githubusercontent.com/115945473/216206773-00ddb980-6e4b-4b88-9195-20a0420f547f.png)



![Screenshot (1197)](https://user-images.githubusercontent.com/115945473/216206719-2161e04e-96c0-41fd-882a-949de993175a.png)





![Screenshot (1196)](https://user-images.githubusercontent.com/115945473/216206754-9fe46abf-bc3b-40cd-81a3-e2e2b21566fa.png)


![Screenshot (1194)](https://user-images.githubusercontent.com/115945473/216206794-995a235b-88ee-4874-889d-c05f92a44bf2.png)

![Screenshot (1195)](https://user-images.githubusercontent.com/115945473/216206804-d3d8c2fd-d951-4820-b7d9-6f9c963cf25d.png)
