# Politico_v2\ 
Description of requirements to run the office,party and user endpoints on postman

        User sign up
        {
	"first_name": "liinet",
	"last_name": "murugi",
	"email":"line@gmail.com", 
	"phone_number":"0720243803", 
	"username":"nimolo", 
	"password":"klo",
	"confirm_password":"klo"
	   } 

       User login
        {
	"username":"nimolo", 
	"confirm_password":"klo"
	   } 

       Office
       {
            
        "name": governor",
        "age": "18",
        "office_type":"state", 
        "education":"olevel",  
        }
        Party
          {
            
        "name": "governor",
        "abbreviations": "18",
        "chairperson":"state", 
        "members":"olevel", 
        "address":"olevel", 
        "logoUrl:"olevel",  
        }

## Tools Used

* Flask Restful - framework for python
* Virtual Environment - used to create an isolated python environment

## Endpoints
|   METHOD       |    URL                    | FUNCTION
|  ------------  | ----------                |  ---------
|   POST         | /api/v2/offices           |  create an office 
|   POST         | /api/v2/parties           |  create a party
|   GET          | /api/v2/offices           |  find all offices
|   GET          | /api/v2/parties           |  find all parties
|   GET          | /api/v2/offices/office_id |  find a specific office with the office_id
|   GET          | /api/v2/parties/party_id  |  find a specific party with the party_id
|   DELETE       | /api/v2/offices/office_id |  delete a specific office with the office_id
|   DELETE       | /api/v2/parties/party_id  |  delete a specific party with  the party_id
|   POST         | /api/v2/auth/signup       |  create an account or sign up
|   POST         | /api/v2/auth/login        |  user log in


## Getting Started

* Clone the repository:
        
        `git clone https://github.com/murugilinet/Politico_v2.git`
* Change directory to the cloned folder:

        `cd Politico_v2`
* If you do not have a virtual environment installed run this to install:

        `pip install virtualenv`
* Create a virtual environment:

        `virtualenv env`
* Activate your virtual environment:

        `source env/bin/activate`

* Install application dependencies:

        `pip install -r requirements.txt`

* Install postgreSQL:

        `sudo apt-get install postgresql`

* create a user account postgres and switch over to it:

        `sudo -u postgres psql`

* create a database:

        `create database politico`

## Running the app

    export DATABASE_URL ="your DATABASE_URL here"


* Connect to database:
         
        export FLASK_APP="run.py"
        export debug="True"
        export APP_SETTINGS="development"

## Open terminal and run:

     `flask run`

        