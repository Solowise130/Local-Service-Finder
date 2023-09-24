                    Local-Service-Finder

This is a collaborative project put up by a team of four vibrant ALX Software Engineering trainees to showcase the skills acquired in our one-year intensive training in the ALX Cohort 9 2022/23 Session.


Project Overview;

Local Service Finder is a dynamic web application designed to bridge the gap between service providers and service seekers within a local community. The platform offers a seamless experience for users to discover, explore, and engage with various local offerings and services while allowing service providers to showcase their and build their reputation through user reviews and ratings.


Target Audience;

This product is designed to ease the stress involved in locating local service professionals when certain needs arise in domestic settings that require professional attention. Hence, the product is meant for the general public, thus; both the service seekers and the service providers.


Front-End Contributors 

+ Solomon Iniodu

+ Oluwatosin Dowo

Back-End Contributors

+ Aganze Felicite

+ Olakunle Olorunfemi


Learning Objectives

+ To create a web application that is responsive on all devices.

+ To learn how to debug and troubleshoot issues in both the front-end and back-end of the application.

+ To create a portfolio piece that showcases the skills we've gathered throughout the training period.


Technologies Used


+ Frontend                                  

+ Html                               

+ CSS

+ Bootstrap

+ React


Backend

+ Flask

+ Mysql


Deployment

+ Heroku

+ Netlify

+ vercel


Testing

+ Postman

+ Manual Testing


Challenges

In the course of developing this application, we were confronted with the following challenges;

+ Inconsistent Power Supply

+ Internet Connectivity

+ Clash in team member’s schedules.

Way forward

Through diplomatic dialogue and compromise, we were able to overcome the above listed challenges.


# Service-Provider-Finder Installation process




## Installation

Install Service-Provider-Finder on your system


# ON LINUX SYSTEM
# ================


  #### Step 1

  create a Folder Open your terminal and type the following
  

  ```
  mkdir folderName
  ```
  
  #### step 2
  On Windows :  
  create a folder and name it accordingly

  

  ```
  cd folderName
  ```
  #### step 3
  create a virtual environment name it accordingly for this installation process
  i will name mine env as shown bellow

  
  ```
  python3 -m venv env
  ```
  #### step 4
  Activate your virtual env as shown bellow
  ```
  source env/bin/activate
  ```

  #### step 5
  clone the github repository as shown bellow
  ```
  git clone https://github.com/Solowise130/Local-Service-Finder.git
  ```
  #### step 6
  move into the project directory
  ```
  cd Local-Service-Finder
  ```

  #### step 7
  Install all the different dependencies into your environment
  ```
  pip install requiremets.txt
  ```

  #### step 8
  Move into the directory named backend
  ```
  cd backend
  ```

  #### step 9
  create the database by 

  ```
  cat database_setup.sql | mysql -uroot -p
  ```
  put your root user password
  this will create the database for you

  #### step 9
  in the terminal type
  ```
  export FLASK_APP=run.py
  ```

  #### step 10
  then run the server like this
  ```
  flask run
  ```

# ON A WINDOWS SYSTEM
# ======================

Create a folder on your Windows system ,accordingly then navigate into that folder.
Next create the virtual environment depeding on your python version
Open your CMD or git bash in that folder and do this
```
python3 -m venv env
```
Activate the virtual environment
```
.\env\Scripts\activate
```
Clone the virtual the github repository

```
git clone https://github.com/Solowise130/Local-Service-Finder.git
```

move into the project folder  and install the requirement file
Open the terminal in the project folder

```
pip install -r requirements.txt
```


This will install all the project dependencies 
Move into the folder named backend 

in that folder open your cmd and 
do this

```
set FLASK_APP=run.py

```
Before running the server create the Database and the dbuser
open your mysql work bench and past into the mysql cli the content of 
database_setup.sql to create the  dabases and users


Then run the server by doing 
```
flask run
```

Open the api into your brownser and  do the different activities on the web site
    

    